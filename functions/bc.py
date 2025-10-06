
import sqlite3, hashlib, requests, time
from typing import Dict, Optional
from nicegui import ui

DB_PATH = 'cryptkeep.db'
TABLE_NAME = 'vault_accounts'
ID_COLUMN = 'id'
PASSWORD_COLUMN = 'password'

SLEEP_BETWEEN_REQUESTS = 1.2
MAX_RETRIES = 3
BACKOFF_FACTOR = 1.5
USER_AGENT = 'CryptKeepPwnedChecker/1.0'

def fetch_rows(db_path: str):
    
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    try:
        cur.execute(f'SELECT {ID_COLUMN}, {PASSWORD_COLUMN} FROM {TABLE_NAME}')
        return cur.fetchall()
    
    finally:
        conn.close()

def query_range(prefix: str, session: requests.Session) -> str:
    
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    headers = {'User-Agent': USER_AGENT}
    attempt = 0
    
    while True:
        
        try:
            resp = session.get(url, headers=headers, timeout=15)
            
        except requests.RequestException as e:
            attempt += 1
            
            if attempt > MAX_RETRIES:
                raise
            
            time.sleep(BACKOFF_FACTOR ** attempt)
            continue

        if resp.status_code == 200:
            return resp.text
        
        elif resp.status_code in (429, 503):
            attempt += 1
            if attempt > MAX_RETRIES:
                raise RuntimeError(f'API returned {resp.status_code}')
            time.sleep(BACKOFF_FACTOR ** attempt)
            continue
        
        else:
            raise RuntimeError(f'Unexpected response {resp.status_code}')

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

def pwned_count_for_password(password: Optional[str], prefix_cache: Dict[str, Dict[str,int]], session: requests.Session) -> int:
    
    if password is None:
        return 0
    
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    
    if prefix not in prefix_cache:
        text = query_range(prefix, session)
        prefix_cache[prefix] = parse_range_response(text)
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        
    return prefix_cache[prefix].get(suffix, 0)

def breach_checker(log, spinner):
    
    spinner.set_visibility(True)
    rows = fetch_rows(DB_PATH)
    session = requests.Session()
    prefix_cache = {}

    for row in rows:
        row_id, pw = row
        
        try:
            count = pwned_count_for_password(str(pw) if pw is not None else None, prefix_cache, session)
            status = 'COMPROMISED' if count > 0 else 'OK'
            
        except Exception:
            status = 'ERROR'
            count = -1
            
        if status == 'COMPROMISED':
            log.push(f'Password from {row_id} was COMPROMISED {count} times.')
        else:
            log.push(f'Password from {row_id} is not compromised.')
    spinner.set_visibility(False)

