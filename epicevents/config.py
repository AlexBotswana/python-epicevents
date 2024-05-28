from dotenv import find_dotenv, dotenv_values, load_dotenv

env_path = find_dotenv('.env')
load_dotenv(env_path)
env_vars = dotenv_values(env_path)
DATABASE_NAME = env_vars['DATABASE_NAME']
SECRET_KEY = env_vars['SECRET_KEY']
USER_ID_CONNECTED = env_vars['USER_ID']
