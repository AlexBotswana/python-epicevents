import jwt 
import bcrypt
from models.User_Model import UserModel
from views.Flash_View import FlashView
from config import SECRET_KEY
from dotenv import set_key, find_dotenv, load_dotenv, dotenv_values


class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def close_connection(self):
        self.user_model.close_connection()

    @staticmethod
    def update_user_id_in_env(new_user_id):
        try:
            # find .env file
            env_path = find_dotenv('.env')
            # Update .env with variable USER_ID
            set_key(env_path, "USER_ID", str(new_user_id))
            # reload var environnement
            load_dotenv(env_path)
            env_vars = dotenv_values(env_path)
            USER_ID_CONNECTED = env_vars['USER_ID']
            print(USER_ID_CONNECTED)
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def hash_password_auth(password, salt):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            return hashed_password
        except Exception as e:
            FlashView.display_error(str(e))

    def authenticate_user(self, username, password):
        try:
            salt = self.user_model.get_pwd_salt(username)
            hash_pwd = self.hash_password_auth(password, salt)
            success, user_id = self.user_model.authenticate_user(username, hash_pwd)
            if success:
                # Update USER_ID in .env
                self.update_user_id_in_env(user_id)
                # Create JWT token
                token = jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm="HS256")
                return True, token
            else:
                return False, None
        except Exception as e:
            FlashView.display_error(str(e))
            
    def authorize_user(self, token):
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token["user_id"]
            user_job = self.user_model.get_user_permissions(user_id)
            required_jobs = [1, 2, 3, 4]
            if user_job in required_jobs:
                return True, user_job
            else:
                return False, user_job
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def hash_password(password):
        try:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            return hashed_password, salt
        except Exception as e:
            FlashView.display_error(str(e))

    def create_user(self, username, password, job_id):
        try:
            hashed_password, salt = self.hash_password(password)
            success = self.user_model.create_user(username, hashed_password, job_id, salt)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def view_users(self):
        try:
            users_list = self.user_model.view_users()
            return users_list
        except Exception as e:
            FlashView.display_error(str(e))
        
    def update_user(self, username, password, job_id, firstname, lastname):
        try:
            hashed_password, salt = self.hash_password(password)
            success = self.user_model.update_user(username, hashed_password, job_id, firstname, lastname, salt)
            return success
        except Exception as e:
            FlashView.display_error(str(e))
        
    def delete_user(self, username):
        try:
            success = self.user_model.delete_user(username)
            return success
        except Exception as e:
            FlashView.display_error(str(e))
    