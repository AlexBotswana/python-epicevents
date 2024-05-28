from views.Menu_View import MenuView
from views.User_View import UserView
from views.Flash_View import FlashView
from controllers.User_Controller import UserController
from db import migration
import sentry_sdk

sentry_sdk.init(
    dsn="https://4468112989beb7b513b6602eac54ee77@o4507332701192192.ingest.de.sentry.io/4507332712071248",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

print('******************************************************************')
print('********************* EPIC EVENTS CRM ****************************')
print('******************************************************************')

def main():
    migration.create_database()

    # User Manager Creation + create data in Statements and Job table
    migration.load_data_from_sql_file('./db/manager_dataset.sql')

    data_set = 0
    print('\n1 - Upload data set?')
    print('2 - Do nothing')
    data_set = int(input('\n Your choice: '))
    if data_set == 1:
        # create data for testing
        migration.load_data_from_sql_file('./db/dataset.sql')


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

if __name__ == '__main__':
    main()
