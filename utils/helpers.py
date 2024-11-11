from datetime import datetime
import random
import string

def generate_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S_%f")

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def random_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length)) 