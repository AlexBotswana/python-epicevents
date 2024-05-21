from models.Customer_Model import CustomerModel
from views.Display_View import DisplayView

class CustomerController:
    def __init__(self, database_name, secret_key):
        self.customer_model = CustomerModel(database_name)
        self.secret_key = secret_key
        self.current_user = None

    def close_connection(self):
        self.customer_model.close_connection()

    def create_customer(self, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id):
        try:
            success = self.customer_model.create_customer(firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id)
            DisplayView.display_creation_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))
            return False

    def view_customers(self):
        try:
            customers_list = self.customer_model.view_customers()
            return customers_list
        except Exception as e:
            DisplayView.display_error(str(e))
            return None

    def update_customer(self, customer_id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id):
        try:
            success = self.customer_model.update_customer(customer_id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id)
            DisplayView.display_update_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))
            return False

    def delete_customer(self, customer_id):
        try:
            success = self.customer_model.delete_customer(customer_id)
            DisplayView.display_delete_result(success)
            return success
        except Exception as e:
            DisplayView.display_error(str(e))
            return False
