#import os
from config import load_dotenv
from views.Menu_View import MenuView
from views.User_View import UserView
from views.Flash_View import FlashView
from controllers.User_Controller import UserController
from db import migration

print('******************************************************************')
print('********************* EPIC EVENTS CRM ****************************')
print('******************************************************************')

migration.create_database()

# User Manager Creation 
migration.load_data_from_sql_file('./db/manager_dataset.sql')

'''
data_set = 0
print('\n1 - Upload data set?')
print('2 - Do nothing')
data_set = int(input('\n Your choice: '))
if data_set == 1:
    migration.load_data_from_sql_file('./db/dataset.sql')
'''

print('\n---------------- LOGIN to EPIC EVENTS CRM ---------------------')


user_connection = UserController()
user_view = UserView()

try:
    # Authentification
    username, password = user_view.get_user_credentials()
    authentication_success, token = user_connection.authenticate_user(username, password)
    if authentication_success:
        FlashView.display_authent_result(authentication_success)
        # Authorization
        # 1 - manager / 2 - gestion / 3 - commercial / 4 - support
        authorization_success, job = user_connection.authorize_user(token)
        if authorization_success:
            FlashView.display_authorization_result(authorization_success)
            if job == 1:
                MenuView.menu_manager()
            elif job == 2:
                MenuView.menu_administration()
            elif job == 3:
                MenuView.menu_commercial()
            elif job == 4:
                MenuView.menu_support()
        else:
            FlashView.display_authorization_result(authorization_success)
    else:
        FlashView.display_authent_result(authentication_success)
except Exception as e:
    FlashView.display_error(str(e))

user_connection.close_connection()
