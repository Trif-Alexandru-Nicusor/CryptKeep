import secrets, random, string

_system_random = random.SystemRandom()


def generate_password(length, lower, upper, digits, symbols, generated_password):
    
    special_chars='!@#$%^&*'
    
    chars = []
    
    if lower:
        chars.append(string.ascii_lowercase)
    if upper:
        chars.append(string.ascii_uppercase)
    if digits:
        chars.append(string.digits)
    if symbols:
        chars.append(special_chars)


    password_chars = [secrets.choice(pool) for pool in chars]

    combined = ''.join(chars)

    remaining = length - len(password_chars)
    password_chars += [secrets.choice(combined) for _ in range(remaining)]

    _system_random.shuffle(password_chars)

    generated_password.set_value(''.join(password_chars))
