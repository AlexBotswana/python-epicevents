from controllers.Customer_Controller import CustomerController
from views.Flash_View import FlashView
from datetime import date

class CustomerView:
    def __init__(self) -> None:
        self.customer_connection = CustomerController()
    
    @staticmethod
    def create_customer():
        customer_connection = CustomerController()
        try:
            firstname = input("Enter firstname: ")
            lastname = input("Enter lastname: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            company_name = input("Enter company name: ")
            located = input("Enter located: ")
            creation_date = date.today()
            last_contact_date = input("Enter last contact date: ")
            success = customer_connection.create_customer(firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date)
            FlashView.display_creation_result(success)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def update_customer():
        customer_connection = CustomerController()
        try:
            customer_id = input("Enter customer ID to be updated: ")
            author_update = customer_connection.customer_in_charge(customer_id)
            if author_update:
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
                FlashView.display_update_result(success)
                return success
            else:
                print("You are not in charge of this customer")
                return False
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def delete_customer():
        customer_connection = CustomerController()
        try:
            customer_id = input("Enter customer ID to be deleted: ")
            author_update = customer_connection.customer_in_charge(customer_id)
            if author_update:
                success = customer_connection.delete_customer(customer_id)
                FlashView.display_delete_result(success)
                return success
            else:
                print("You are not in charge of this customer")
                return False
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def view_customers():
        customer_connection = CustomerController()
        try:
            list_customers = customer_connection.view_customers()
            if list_customers:
                for customer in list_customers:
                    print(customer)
            else:
                print("No customer found.")
        except Exception as e:
            FlashView.display_error(str(e))
