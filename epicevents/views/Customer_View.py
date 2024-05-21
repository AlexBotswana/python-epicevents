from controllers.Customer_Controller import CustomerController
from views.Display_View import DisplayView
from datetime import date

class CustomerView:
    def __init__(self, database_name, secret_key) -> None:
        self.customer_connection = CustomerController(database_name, secret_key)
    
    @staticmethod
    def create_customer(database_name, secret_key):
        customer_connection = CustomerController(database_name, secret_key)
        try:
            firstname = input("Enter firstname: ")
            lastname = input("Enter lastname: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            company_name = input("Enter company name: ")
            located = input("Enter located: ")
            creation_date = date.today()
            last_contact_date = input("Enter last contact date: ")
            commercial_user_id = input("Enter commercial user ID: ")
            success = customer_connection.create_customer(firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id)
            DisplayView.display_creation_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))

    @staticmethod
    def update_customer(database_name, secret_key):
        customer_connection = CustomerController(database_name, secret_key)
        try:
            customer_id = input("Enter customer ID to be updated: ")
            firstname = input("Enter new firstname: ")
            lastname = input("Enter new lastname: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            company_name = input("Enter new company name: ")
            located = input("Enter new located: ")
            creation_date = input("Enter new creation date: ")
            last_contact_date = date.today()
            commercial_user_id = input("Enter new commercial user ID: ")
            success = customer_connection.update_customer(customer_id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id)
            DisplayView.display_update_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))

    @staticmethod
    def delete_customer(database_name, secret_key):
        customer_connection = CustomerController(database_name, secret_key)
        try:
            customer_id = input("Enter customer ID to be deleted: ")
            success = customer_connection.delete_customer(customer_id)
            DisplayView.display_delete_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))

    @staticmethod
    def view_customers(database_name, secret_key):
        customer_connection = CustomerController(database_name, secret_key)
        list_customers = customer_connection.view_customers()
        print(list_customers)
