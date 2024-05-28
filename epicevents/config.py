import os
from dotenv import load_dotenv, find_dotenv

def load_env_variables():
    load_dotenv(find_dotenv())
    return {
        'DATABASE_NAME': os.getenv('DATABASE_NAME'),
        'SECRET_KEY': os.getenv('SECRET_KEY'),
        'USER_ID': os.getenv('USER_ID')
    }

env_vars = load_env_variables()
DATABASE_NAME = env_vars['DATABASE_NAME']
SECRET_KEY = env_vars['SECRET_KEY']
USER_ID_CONNECTED = env_vars['USER_ID']
