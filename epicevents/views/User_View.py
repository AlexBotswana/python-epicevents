from controllers.User_Controller import UserController
from views.Display_View import DisplayView
import getpass

class UserView:
    def __init__(self, database_name, secret_key) -> None:
        self.user_connection = UserController(database_name, secret_key)

    @staticmethod
    def get_user_credentials():
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        return username, password
    
    @staticmethod
    def create_user(database_name, secret_key):
        user_connection = UserController(database_name, secret_key)
        try:
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            job_id = input("Enter job_id (2-Gestion / 3-Commercial / 4-Support): ")
            success = user_connection.create_user(username, password, job_id)
            DisplayView.display_creation_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))
    
    @staticmethod
    def update_user(database_name, secret_key):
        user_connection = UserController(database_name, secret_key)
        try:
            username = input("Enter username to be updated: ")
            new_pwd = getpass.getpass("Enter new password: ")
            new_job_id = input("Enter new job_id (2-Gestion / 3-Commercial / 4-Support): ")
            firstname = input("Enter firstname: ")
            lastname = input("Enter lastname: ")
            success = user_connection.update_user(username, new_pwd, new_job_id, firstname, lastname)
            DisplayView.display_update_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))

    @staticmethod
    def delete_user(database_name, secret_key):
        user_connection = UserController(database_name, secret_key)
        try:
            username = input("Enter username to be deleted: ")
            success = user_connection.delete_user(username)
            DisplayView.display_delete_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))

    @staticmethod
    def view_users(database_name, secret_key):
        user_connection = UserController(database_name, secret_key)
        list_users = user_connection.view_users()
        print(list_users)
