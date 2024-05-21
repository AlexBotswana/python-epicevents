from models.User_Model import UserModel
from views.Display_View import DisplayView
import jwt 
import bcrypt

class UserController:
    def __init__(self, database_name, secret_key):
        self.user_model = UserModel(database_name)
        self.secret_key = secret_key
        self.current_user = None

    def close_connection(self):
        self.user_model.close_connection()

    @staticmethod
    def hash_password_auth(password, salt):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
    
    def authenticate_user(self, username, password):
        try:
            salt = self.user_model.get_pwd_salt(username)
            hash_pwd = self.hash_password_auth(password, salt)
            success, user_id = self.user_model.authenticate_user(username, hash_pwd)
            if success:
                 # Create JWT token
                self.current_user = user_id
                token = jwt.encode({"user_id": user_id}, self.secret_key, algorithm="HS256")
                return True, token
            else:
                return False, None
        except Exception as e:
            DisplayView.display_error(str(e))
            #return False, None, str(e)

    def authorize_user(self, token):
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            user_id = decoded_token["user_id"]
            user_job = self.user_model.get_user_permissions(user_id)
            required_jobs = [1, 2, 3, 4]
            if user_job in required_jobs:
                return True, user_job
            else:
                return False, user_job
        except Exception as e:
            DisplayView.display_error(str(e))
            #return False, str(e)

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password, salt

    def create_user(self, username, password, job_id):
        try:
            hashed_password, salt = self.hash_password(password)
            success = self.user_model.create_user(username, hashed_password, job_id, salt)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))
            #return False, str(e)

    def view_users(self):
        try:
            users_list = self.user_model.view_users()
            return users_list
        except Exception as e:
            DisplayView.display_error(str(e))
            #return None, str(e)
        
    def update_user(self, username, password, job_id, firstname, lastname):
        try:
            hashed_password, salt = self.hash_password(password)
            success = self.user_model.update_user(username, hashed_password, job_id, firstname, lastname, salt)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))
            #return False, str(e)
        
    def delete_user(self, username):
        try:
            success = self.user_model.delete_user(username)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))
            #return False, str(e)
    