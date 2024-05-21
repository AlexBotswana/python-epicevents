from views.Menu_View import MenuView
from views.User_View import UserView
from views.Display_View import DisplayView
from controllers.User_Controller import UserController
from db import migration

print('******************************************************************')
print('********************* EPIC EVENTS CRM ****************************')
print('******************************************************************')

database_name = './db/epic.db'
secret_key = 'alfacama'

migration.create_database('./db/epic.db')

# User Manager Creation 
migration.load_data_from_sql_file('./db/manager_dataset.sql', './db/epic.db', secret_key)

data_set = 0
print('\n1 - Upload data set?')
print('2 - Do nothing')
data_set = int(input('\n Your choice: '))
if data_set == 1:
    migration.load_data_from_sql_file('./db/dataset.sql', './db/epic.db', secret_key)

print('\n---------------- LOGIN to EPIC EVENTS CRM ---------------------')


user_connection = UserController(database_name, secret_key)
user_view = UserView(database_name, secret_key)

try:
    # Authentification
    username, password = user_view.get_user_credentials()
    authentication_success, token = user_connection.authenticate_user(username, password)
    if authentication_success:
        DisplayView.display_authent_result(authentication_success)
        # Authorization
        # 1 - manager / 2 - gestion / 3 - commercial / 4 - support
        authorization_success, job = user_connection.authorize_user(token)
        if authorization_success:
            DisplayView.display_authorization_result(authorization_success)
            if job == 1:
                MenuView.menu_manager(database_name, secret_key)
            elif job == 2:
                MenuView.menu_administration(database_name, secret_key)
            elif job == 3:
                MenuView.menu_commercial()
            elif job == 4:
                MenuView.menu_support()
        else:
            DisplayView.display_authorization_result(authorization_success)
    else:
        DisplayView.display_authent_result(authentication_success)
except Exception as e:
    DisplayView.display_error(str(e))

user_connection.close_connection()
