import hashlib
import aiohttp
import asyncio
from nicegui import ui
from typing import Dict, Optional
import sqlite3

DB_PATH = 'cryptkeep.db'
TABLE_NAME = 'vault_accounts'
ID_COLUMN = 'id'
PASSWORD_COLUMN = 'password'
SLEEP_BETWEEN_REQUESTS = 1.2
MAX_RETRIES = 3
BACKOFF_FACTOR = 1.5
USER_AGENT = 'CryptKeepPwnedChecker/1.0'

async def fetch_rows(db_path: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute(f'SELECT {ID_COLUMN}, {PASSWORD_COLUMN} FROM {TABLE_NAME}')
        return cur.fetchall()
    finally:
        conn.close()

async def query_range_async(prefix: str, session: aiohttp.ClientSession) -> str:
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    headers = {'User-Agent': USER_AGENT}
    attempt = 0

    while True:
        try:
            async with session.get(url, headers=headers, timeout=15) as resp:
                if resp.status == 200:
                    return await resp.text()
                elif resp.status in (429, 503):
                    attempt += 1
                    if attempt > MAX_RETRIES:
                        raise RuntimeError(f'API returned {resp.status}')
                    await asyncio.sleep(BACKOFF_FACTOR ** attempt)
                    continue
                else:
                    raise RuntimeError(f'Unexpected response {resp.status}')
        except Exception:
            attempt += 1
            if attempt > MAX_RETRIES:
                raise
            await asyncio.sleep(BACKOFF_FACTOR ** attempt)

def parse_range_response(text: str):
    d = {}
    for line in text.splitlines():
        if not line:
            continue
        parts = line.split(':')
        if len(parts) != 2:
            continue
        suffix, count = parts
        d[suffix.strip().upper()] = int(count.strip())
    return d

async def pwned_count_for_password(password: Optional[str], prefix_cache: Dict[str, Dict[str,int]], session: aiohttp.ClientSession) -> int:
    if password is None:
        return 0
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    if prefix not in prefix_cache:
        text = await query_range_async(prefix, session)
        prefix_cache[prefix] = parse_range_response(text)
        await asyncio.sleep(SLEEP_BETWEEN_REQUESTS)

    return prefix_cache[prefix].get(suffix, 0)

async def breach_checker_async(log, spinner):
    spinner.set_visibility(True)
    rows = await fetch_rows(DB_PATH)
    prefix_cache = {}

    async with aiohttp.ClientSession() as session:
        for row in rows:
            row_id, pw = row
            try:
                count = await pwned_count_for_password(str(pw) if pw else None, prefix_cache, session)
                status = 'COMPROMISED' if count > 0 else 'OK'
            except Exception:
                status = 'ERROR'
                count = -1

            if status == 'COMPROMISED':
                log.push(f'Password from {row_id} was COMPROMISED {count} times.')
            else:
                log.push(f'Password from {row_id} is not compromised.')

    spinner.set_visibility(False)
