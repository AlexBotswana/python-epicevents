from views.User_View import UserView
from views.Customer_View import CustomerView
from views.Contract_View import ContractView
from views.Event_View import EventView

class MenuView:
    def __init__(self) -> None:
        pass

    def menu_manager() -> None:
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
                    user_view = UserView()
                    menu_choice_user = 1
                    while int(menu_choice_user) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Manager Menu ----------------\n')
                        print('---------------------------- Users  -------------------------\n')
                        print(' 1 - Create user')
                        print(' 2 - View user')
                        print(' 3 - Update user')
                        print(' 4 - Delete user')
                        print(' 0 - Back')
                        menu_choice_user = int(input(' Choice : '))
                        if int(menu_choice_user) == 1:
                            user_view.create_user()
                        elif int(menu_choice_user) == 2:
                            user_view.view_users()
                        elif int(menu_choice_user) == 3:
                            user_view.update_user()
                        elif int(menu_choice_user) == 4:
                            user_view.delete_user()
                # Menu to manage customers
                elif int(menu_choice) == 2:
                    customer_view = CustomerView()
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
                            customer_view.create_customer()
                        elif int(menu_choice_customer) == 2:
                            customer_view.view_customers()
                        elif int(menu_choice_customer) == 3:
                            customer_view.update_customer()
                        elif int(menu_choice_customer) == 4:
                            customer_view.delete_customer()
                # Menu to manage contracts
                elif int(menu_choice) == 3:
                    contract_view = ContractView()
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
                            contract_view.create_contract()
                        elif int(menu_choice_contract) == 2:
                            contract_view.view_contracts()
                        elif int(menu_choice_contract) == 3:
                            contract_view.update_contract()
                        elif int(menu_choice_contract) == 4:
                            contract_view.delete_contract()
                # Menu to manage events
                elif int(menu_choice) == 4:
                    event_view = EventView()
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
                            event_view.create_event()
                        elif int(menu_choice_event) == 2:
                            menu_choice_event_view = 1
                            while int(menu_choice_event_view) != 0:
                            # Menu selection
                                print('\n\n---------------- EPIC Events Manager Menu ----------------\n')
                                print('---------------------- View Events Menu -----------------------\n')
                                print(' 1 - View events without support')
                                print(' 2 - View all events')
                                print(' 0 - Back')
                                menu_choice_event_view = int(input(' Choice : '))
                                if int(menu_choice_event_view) == 1:
                                    event_view.view_events_wo_support()
                                elif int(menu_choice_event_view) == 2:
                                    event_view.view_events()
                        elif int(menu_choice_event) == 3:
                            event_view.update_event()
                        elif int(menu_choice_event) == 4:
                            event_view.delete_event()
            except Exception as e:
                print('WRONG CHOICE')

    def menu_administration() -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
            try:
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
                    user_view = UserView()
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
                            user_view.create_user()
                        elif int(menu_choice_user) == 2:
                            user_view.view_users()
                        elif int(menu_choice_user) == 3:
                            user_view.update_user()
                        elif int(menu_choice_user) == 4:
                            user_view.delete_user()
                # Menu to manage customers
                elif int(menu_choice) == 2:
                    customer_view = CustomerView
                    menu_choice_customer = 1
                    while int(menu_choice_customer) != 0:
                        print('\n\n---------------- EPIC Events Admin Menu ----------------\n')
                        print('\n\n---------------- Customers Menu ----------------\n')
                        print(' 1 - View customer')
                        print(' 0 - Back')
                        menu_choice_customer = int(input(' Choice : '))
                        if int(menu_choice_customer) == 1:
                            customer_view.view_customers()
                # Menu to manage contracts
                elif int(menu_choice) == 3:
                    contract_view = ContractView()
                    menu_choice_contract = 1
                    while int(menu_choice_contract) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Admin Menu ----------------\n')
                        print('--------------------- Contracts Menu ---------------------\n')
                        print(' 1 - Create contract')
                        print(' 2 - View contract')
                        print(' 3 - Update contract')
                        print(' 0 - Back')
                        menu_choice_contract = int(input(' Choice : '))
                        if int(menu_choice_contract) == 1:
                            contract_view.create_contract()
                        elif int(menu_choice_contract) == 2:
                            contract_view.view_contracts()
                        elif int(menu_choice_contract) == 3:
                            contract_view.update_contract()
                # Menu to manage events
                elif int(menu_choice) == 4:
                    event_view = EventView()
                    menu_choice_event = 1
                    while int(menu_choice_event) != 0:
                        print('\n\n---------------- EPIC Events Admin Menu ----------------\n')
                        print('\n\n---------------- Events Menu ----------------\n')
                        print(' 1 - View event')
                        print(' 2 - Update event')
                        print(' 0 - Back')
                        menu_choice_event = int(input(' Choice : '))
                        if int(menu_choice_event) == 1:
                            menu_choice_event_view = 1
                            while int(menu_choice_event_view) != 0:
                            # Menu selection
                                print('\n\n---------------- EPIC Events Admin Menu ----------------\n')
                                print('---------------------- View Events Menu -----------------------\n')
                                print(' 1 - View events without support')
                                print(' 2 - View all events')
                                print(' 0 - Back')
                                menu_choice_event_view = int(input(' Choice : '))
                                if int(menu_choice_event_view) == 1:
                                    event_view.view_events_wo_support()
                                elif int(menu_choice_event_view) == 2:
                                    event_view.view_events()
                        elif int(menu_choice_event) == 2:
                            menu_choice_event_update = 1
                            while int(menu_choice_event_update) != 0:
                            # Menu selection
                                print('\n\n---------------- EPIC Events Admin Menu ----------------\n')
                                print('---------------------- Update Events Menu -----------------------\n')
                                print(' 1 - Add a support to an event')
                                print(' 0 - Back')
                                menu_choice_event_update = int(input(' Choice : '))
                                if int(menu_choice_event_update) == 1:
                                    event_view.update_event_support()
            except Exception as e:
                print('WRONG CHOICE')

    def menu_commercial() -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
            try:
                # Menu selection
                print('\n\n---------------- EPIC Events Commercial Menu----------------\n')
                print(' 1 - Customer menu')
                print(' 2 - Contract menu')
                print(' 3 - Event menu')
                print(' 0 - Exit')
                menu_choice = int(input(' Choice : '))
                # Menu to manage customers
                if int(menu_choice) == 1:
                    customer_view = CustomerView()
                    menu_choice_customer = 1
                    while int(menu_choice_customer) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Commercial Menu ----------------\n')
                        print('--------------------- Customers Menu ---------------------\n')
                        print(' 1 - Create customer')
                        print(' 2 - View customer')
                        print(' 3 - Update customer')
                        print(' 0 - Back')
                        menu_choice_customer = int(input(' Choice : '))
                        if int(menu_choice_customer) == 1:
                            customer_view.create_customer()
                        elif int(menu_choice_customer) == 2:
                            customer_view.view_customers()
                        elif int(menu_choice_customer) == 3:
                            customer_view.update_customer()
                # Menu to manage contracts
                elif int(menu_choice) == 2:
                    contract_view = ContractView()
                    menu_choice_contract = 1
                    while int(menu_choice_contract) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Commercial Menu ----------------\n')
                        print('--------------------- Contracts Menu ---------------------\n')
                        print(' 1 - View contract')
                        print(' 2 - Update contract')
                        print(' 0 - Back')
                        menu_choice_contract = int(input(' Choice : '))
                        if int(menu_choice_contract) == 1:
                            menu_choice_contract_view = 1
                            while int(menu_choice_contract_view) != 0:
                            # Menu selection
                                print('\n\n---------------- EPIC Events Commercial Menu ----------------\n')
                                print('---------------------- View Contract Menu -----------------------\n')
                                print(' 1 - View not signed contracts')
                                print(' 2 - View not totally paid contracts')
                                print(' 3 - View all contracts')
                                print(' 0 - Back')
                                menu_choice_contract_view = int(input(' Choice : '))
                                if int(menu_choice_contract_view) == 1:
                                    contract_view.view_not_signed_contracts()
                                elif int(menu_choice_contract_view) == 2:
                                    contract_view.view_not_paid_contracts()
                                elif int(menu_choice_contract_view) == 3:
                                    contract_view.view_contracts()
                        elif int(menu_choice_contract) == 2:
                            contract_view.update_contract()
                # Menu to manage events
                elif int(menu_choice) == 3:
                    event_view = EventView()
                    menu_choice_event = 1
                    while int(menu_choice_event) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Commercial Menu ----------------\n')
                        print('---------------- Events Menu ----------------\n')
                        print(' 1 - Create event')
                        print(' 2 - View event')
                        print(' 0 - Back')
                        menu_choice_event = int(input(' Choice : '))
                        if int(menu_choice_event) == 1:
                            event_view.create_event()
                        elif int(menu_choice_event) == 2:
                            event_view.view_events()
            except Exception as e:
                print('WRONG CHOICE')

    def menu_support() -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
            try:
                # Menu selection
                print('\n\n---------------- EPIC Events Support Menu----------------\n')
                print(' 1 - Customer menu')
                print(' 2 - Contract menu')
                print(' 3 - Event menu')
                print(' 0 - Exit')
                menu_choice = int(input(' Choice : '))
                # Menu to manage customers
                if int(menu_choice) == 1:
                    customer_view = CustomerView()
                    menu_choice_customer = 1
                    while int(menu_choice_customer) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Support Menu----------------\n')
                        print('---------------- Customers Menu ----------------\n')
                        print(' 1 - View customer')
                        print(' 0 - Back')
                        menu_choice_customer = int(input(' Choice : '))
                        if int(menu_choice_customer) == 1:
                            customer_view.view_customers()
                # Menu to manage contracts
                elif int(menu_choice) == 2:
                    contract_view = ContractView
                    menu_choice_contract = 1
                    while int(menu_choice_contract) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Support Menu----------------\n')
                        print('---------------- Contracts Menu ----------------\n')
                        print(' 1 - View contract')
                        print(' 0 - Back')
                        menu_choice_contract = int(input(' Choice : '))
                        if int(menu_choice_contract) == 1:
                            contract_view.view_contracts()
                # Menu to manage events
                elif int(menu_choice) == 3:
                    event_view = EventView()
                    menu_choice_event = 1
                    while int(menu_choice_event) != 0:
                        # Menu selection
                        print('\n\n---------------- EPIC Events Support Menu----------------\n')
                        print('---------------- Events Menu ----------------\n')
                        print(' 1 - View event')
                        print(' 2 - Update event')
                        print(' 0 - Back')
                        menu_choice_event = int(input(' Choice : '))
                        if int(menu_choice_event) == 1:
                            menu_choice_event_view = 1
                            while int(menu_choice_event_view) != 0:
                                # Menu selection
                                print('\n\n---------------- EPIC Events Support Menu----------------\n')
                                print('---------------- Events Menu ----------------\n')
                                print(' 1 - View your events')
                                print(' 2 - View all events')
                                print(' 0 - Back')
                                menu_choice_event_view = int(input(' Choice : '))
                                if int(menu_choice_event_view) == 1:
                                    event_view.view_events_for_support()
                                elif int(menu_choice_event_view) == 2:
                                    event_view.view_events()
                        elif int(menu_choice_event) == 2:
                            event_view.update_event()
            except Exception as e:
                print('WRONG CHOICE')
