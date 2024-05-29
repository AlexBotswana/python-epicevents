from models.Customer_Model import CustomerModel
from models.User_Model import UserModel
from views.Flash_View import FlashView
#from config import USER_ID_CONNECTED
from dotenv import load_dotenv, find_dotenv, dotenv_values

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
            # find .env file
            env_path = find_dotenv('.env')
            # reload var environnement
            load_dotenv(env_path)
            env_vars = dotenv_values(env_path)
            USER_ID_CONNECTED = env_vars['USER_ID']
            commercial_id = self.customer_model.view_single_customer(customer_id)
            job_id_user_connected = self.user_model.get_user_permissions(USER_ID_CONNECTED)
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
            if customers_list:
                # replace user id by username for user in charge of the customer
                for i in range(len(customers_list)):
                    customer_list = list(customers_list[i])
                    commercial_username = self.user_model.get_username(int(customer_list[9]))
                    customer_list[9] = commercial_username
                    customers_list[i] = tuple(customer_list)
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
