from models.Customer_Model import CustomerModel
from models.User_Model import UserModel
from views.Flash_View import FlashView
from config import USER_ID_CONNECTED

class CustomerController:
    def __init__(self):
        self.customer_model = CustomerModel()
        self.user_model = UserModel()
        self.current_user = None

    def close_connection(self):
        self.customer_model.close_connection()

    # Function to know if the user connected is in charge of the customer or is the user manager (all rights = job = 1)
    def customer_in_charge(self, customer_id):
        try:
            commercial_id = self.customer_model.view_single_customer(customer_id)
            job_id_user_connected = self.user_model.get_user_permissions(USER_ID_CONNECTED)
            print(USER_ID_CONNECTED)
            if commercial_id[0] != '':
                if (int(commercial_id[0]) == int(USER_ID_CONNECTED)) or (int(job_id_user_connected) == 1):
                    return True
                else:
                    return False
            elif int(job_id_user_connected) == 1:
                return True
            else:
                return False
        except Exception as e:
            FlashView.display_error(str(e))

    def create_customer(self, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date):
        try:
            success = self.customer_model.create_customer(firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date)
            FlashView.display_creation_result(success)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def view_customers(self):
        try:
            customers_list = self.customer_model.view_customers()
            return customers_list
        except Exception as e:
            FlashView.display_error(str(e))

    def update_customer(self, customer_id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id):
        try:
            success = self.customer_model.update_customer(customer_id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id)
            FlashView.display_update_result(success)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def delete_customer(self, customer_id):
        try:
            success = self.customer_model.delete_customer(customer_id)
            FlashView.display_delete_result(success)
            return success
        except Exception as e:
            FlashView.display_error(str(e))
