import os
import secrets

# generating secret key to be used to create and verify tokens 
def generate_secret_key():
    secret_key = secrets.token_hex(32)

    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(f'SECRET_KEY={secret_key}\n')
    else:
        with open('.env', 'a') as f:
            if 'SECRET_KEY' not in open('.env').read():
                f.write(f'SECRET_KEY={secret_key}\n')