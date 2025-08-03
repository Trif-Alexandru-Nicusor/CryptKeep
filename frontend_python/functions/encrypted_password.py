import bcrypt, os
from dotenv import load_dotenv

load_dotenv(dotenv_path = '../.env')

pepper = os.getenv('PEPPER')

def encrypt_password(password):
    
    password_peppered = (password+pepper).encode()
    salt = bcrypt.gensalt(rounds = 12)
    
    hashed = bcrypt.hashpw(password_peppered, salt)
    
    return hashed

def check_password(password, hashed) -> bool:
    
    password_peppered = (password + pepper).encode()
    
    return bcrypt.checkpw(password_peppered, hashed)