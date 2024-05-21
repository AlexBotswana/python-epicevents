from views.User_View import UserView
from views.Customer_View import CustomerView
from views.Contract_View import ContractView
from views.Event_View import EventView

class MenuView:
    def __init__(self) -> None:
        pass

    def menu_manager(database_name, secret_key) -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
            try:
                # Menu selection
                print('\n\n---------------- EPIC Events Manager Menu ----------------\n')
                print(' 1 - Users menu')
                print(' 2 - Customer menu')
                print(' 3 - Contract menu')
                print(' 4 - Event menu')
                print(' 0 - Exit')
                menu_choice = int(input(' Choice : '))
                # Menu to manage users
                if int(menu_choice) == 1:
                    user_view = UserView(database_name, secret_key)
                    menu_choice_user = 1
                    while int(menu_choice_user) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Manager Menu ----------------\n')
                        print('----------------------- Users Menu -----------------------\n')
                        print(' 1 - Create user')
                        print(' 2 - View user')
                        print(' 3 - Update user')
                        print(' 4 - Delete user')
                        print(' 0 - Back')
                        menu_choice_user = int(input(' Choice : '))
                        if int(menu_choice_user) == 1:
                            user_view.create_user(database_name, secret_key)
                        elif int(menu_choice_user) == 2:
                            user_view.view_users(database_name, secret_key)
                        elif int(menu_choice_user) == 3:
                            user_view.update_user(database_name, secret_key)
                        elif int(menu_choice_user) == 4:
                            user_view.delete_user(database_name, secret_key)
                # Menu to manage customers
                elif int(menu_choice) == 2:
                    customer_view = CustomerView(database_name, secret_key)
                    menu_choice_customer = 1
                    while int(menu_choice_customer) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Manager Menu ----------------\n')
                        print('--------------------- Customers Menu ---------------------\n')
                        print(' 1 - Create customer')
                        print(' 2 - View customer')
                        print(' 3 - Update customer')
                        print(' 4 - Delete customer')
                        print(' 0 - Back')
                        menu_choice_customer = int(input(' Choice : '))
                        if int(menu_choice_customer) == 1:
                            customer_view.create_customer(database_name, secret_key)
                        elif int(menu_choice_customer) == 2:
                            customer_view.view_customers(database_name, secret_key)
                        elif int(menu_choice_customer) == 3:
                            customer_view.update_customer(database_name, secret_key)
                        elif int(menu_choice_customer) == 4:
                            customer_view.delete_customer(database_name, secret_key)
                # Menu to manage contracts
                elif int(menu_choice) == 3:
                    contract_view = ContractView(database_name, secret_key)
                    menu_choice_contract = 1
                    while int(menu_choice_contract) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Manager Menu ----------------\n')
                        print('--------------------- Contracts Menu ---------------------\n')
                        print(' 1 - Create contract')
                        print(' 2 - View contract')
                        print(' 3 - Update contract')
                        print(' 4 - Delete contract')
                        print(' 0 - Back')
                        menu_choice_contract = int(input(' Choice : '))
                        if int(menu_choice_contract) == 1:
                            contract_view.create_contract(database_name, secret_key)
                        elif int(menu_choice_contract) == 2:
                            contract_view.view_contracts(database_name, secret_key)
                        elif int(menu_choice_contract) == 3:
                            contract_view.update_contract(database_name, secret_key)
                        elif int(menu_choice_contract) == 4:
                            contract_view.delete_contract(database_name, secret_key)
                # Menu to manage events
                elif int(menu_choice) == 4:
                    event_view = EventView(database_name, secret_key)
                    menu_choice_event = 1
                    while int(menu_choice_event) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Manager Menu ----------------\n')
                        print('---------------------- Events Menu -----------------------\n')
                        print(' 1 - Create event')
                        print(' 2 - View event')
                        print(' 3 - Update event')
                        print(' 4 - Delete event')
                        print(' 0 - Back')
                        menu_choice_event = int(input(' Choice : '))
                        if int(menu_choice_event) == 1:
                            event_view.create_event(database_name, secret_key)
                        elif int(menu_choice_event) == 2:
                            event_view.view_events(database_name, secret_key)
                        elif int(menu_choice_event) == 3:
                            event_view.update_event(database_name, secret_key)
                        elif int(menu_choice_event) == 4:
                            event_view.delete_event(database_name, secret_key)
            except Exception:
                print('WRONG CHOICE')

    def menu_administration(database_name, secret_key) -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
            # Menu selection
            print('\n\n---------------- EPIC Events Admin Menu ----------------\n')
            print(' 1 - Users menu')
            print(' 2 - Customer Menu')
            print(' 3 - Contract menu')
            print(' 4 - Event menu')
            print(' 0 - Exit')
            menu_choice = int(input(' Choice : '))
            # Menu to manage users
            if int(menu_choice) == 1:
                user_view = UserView(database_name, secret_key)
                menu_choice_user = 1
                while int(menu_choice_user) != 0:
                    # Menu selection
                    print('\n\n---------------- EPIC Events Admin Menu ----------------\n')
                    print('------------------------- Users Menu -----------------------\n')
                    print(' 1 - Create user')
                    print(' 2 - View user')
                    print(' 3 - Update user')
                    print(' 4 - Delete user')
                    print(' 0 - Back')
                    menu_choice_user = int(input(' Choice : '))
                    if int(menu_choice_user) == 1:
                        user_view.create_user(database_name, secret_key)
                    elif int(menu_choice_user) == 2:
                        user_view.view_users(database_name, secret_key)
                    elif int(menu_choice_user) == 3:
                        user_view.update_user(database_name, secret_key)
                    elif int(menu_choice_user) == 4:
                        user_view.delete_user(database_name, secret_key)
            # Menu to manage customers
            elif int(menu_choice) == 2:
                menu_choice_customer = 1
                while int(menu_choice_customer) != 0:
                    # Menu selection
                    print('\n\n---------------- Customers Menu ----------------\n')
                    print(' 1 - View customer')
                    print(' 0 - Back')
                    menu_choice_customer = int(input(' Choice : '))
            # Menu to manage contracts
            elif int(menu_choice) == 3:
                menu_choice_contract = 1
                while int(menu_choice_contract) != 0:
                    # Menu selection
                    print('\n\n---------------- Contracts Menu ----------------\n')
                    print(' 1 - Create contract')
                    print(' 2 - View contract')
                    print(' 3 - Update contract')
                    print(' 0 - Back')
                    menu_choice_contract = int(input(' Choice : '))
            # Menu to manage events
            elif int(menu_choice) == 4:
                menu_choice_event = 1
                while int(menu_choice_event) != 0:
                    # Menu selection
                    print('\n\n---------------- Events Menu ----------------\n')
                    print(' 1 - View event')
                    print(' 2 - Update event')
                    print(' 0 - Back')
                    menu_choice_event = int(input(' Choice : '))

    def menu_commercial() -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
            # Menu selection
            print('\n\n---------------- EPIC Events ----------------\n')
            print(' 1 - Customer menu')
            print(' 2 - Contract menu')
            print(' 3 - Event menu')
            print(' 0 - Exit')
            menu_choice = int(input(' Choice : '))
            # Menu to manage customers
            if int(menu_choice) == 1:
                menu_choice_customer = 1
                while int(menu_choice_customer) != 0:
                    # Menu selection
                    print('\n\n---------------- Customers Menu ----------------\n')
                    print(' 1 - Create customer')
                    print(' 2 - View customer')
                    print(' 3 - Update customer')
                    print(' 0 - Back')
                    menu_choice_customer = int(input(' Choice : '))
            # Menu to manage contracts
            elif int(menu_choice) == 2:
                menu_choice_contract = 1
                while int(menu_choice_contract) != 0:
                    # Menu selection
                    print('\n\n---------------- Contracts Menu ----------------\n')
                    print(' 1 - View contract')
                    print(' 2 - Update contract')
                    print(' 0 - Back')
                    menu_choice_contract = int(input(' Choice : '))
            # Menu to manage events
            elif int(menu_choice) == 3:
                menu_choice_event = 1
                while int(menu_choice_event) != 0:
                    # Menu selection
                    print('\n\n---------------- Events Menu ----------------\n')
                    print(' 1 - Create event')
                    print(' 2 - View event')
                    print(' 3 - Update event')
                    print(' 0 - Back')
                    menu_choice_event = int(input(' Choice : '))

    def menu_support() -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
            # Menu selection
            print('\n\n---------------- EPIC Events ----------------\n')
            print(' 1 - Customer menu')
            print(' 2 - Contract menu')
            print(' 3 - Event menu')
            print(' 0 - Exit')
            menu_choice = int(input(' Choice : '))
            # Menu to manage customers
            if int(menu_choice) == 1:
                menu_choice_customer = 1
                while int(menu_choice_customer) != 0:
                    # Menu selection
                    print('\n\n---------------- Customers Menu ----------------\n')
                    print(' 1 - View customer')
                    print(' 0 - Back')
                    menu_choice_customer = int(input(' Choice : '))
            # Menu to manage contracts
            elif int(menu_choice) == 2:
                menu_choice_contract = 1
                while int(menu_choice_contract) != 0:
                    # Menu selection
                    print('\n\n---------------- Contracts Menu ----------------\n')
                    print(' 1 - View contract')
                    print(' 0 - Back')
                    menu_choice_contract = int(input(' Choice : '))
            # Menu to manage events
            elif int(menu_choice) == 3:
                menu_choice_event = 1
                while int(menu_choice_event) != 0:
                    # Menu selection
                    print('\n\n---------------- Events Menu ----------------\n')
                    print(' 1 - View event')
                    print(' 2 - Update event')
                    print(' 0 - Back')
                    menu_choice_event = int(input(' Choice : '))

