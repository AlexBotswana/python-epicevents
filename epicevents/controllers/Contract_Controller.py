from models.Contract_Model import ContractModel
from controllers.Customer_Controller import CustomerController
from views.Flash_View import FlashView

class ContractController:
    def __init__(self):
        self.contract_model = ContractModel()

    def create_contract(self, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id):
        try:
            success = self.contract_model.create_contract(title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def update_contract(self, contract_id, title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id):
        try:
            success = self.contract_model.update_contract(contract_id, title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def delete_contract(self, contract_id):
        try:
            success = self.contract_model.delete_contract(contract_id)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def view_contracts(self):
        try:
            contracts_list = self.contract_model.view_contracts()
            return contracts_list
        except Exception as e:
            FlashView.display_error(str(e))

    def view_not_signed_contracts(self):
        try:
            contracts_list = self.contract_model.view_not_signed_contracts()
            return contracts_list
        except Exception as e:
            FlashView.display_error(str(e))

    def view_not_paid_contracts(self):
        try:
            contracts_list = self.contract_model.view_not_paid_contracts()
            return contracts_list
        except Exception as e:
            FlashView.display_error(str(e))        

    def contract_in_charge(self, contract_id):
        # Commercial of the customer contract
        try:
            # select the customer of the contract
            contract_info = self.contract_model.view_single_contract(contract_id)
            customer_id = contract_info[0]
            customer_connection = CustomerController()
            # test if the user connected is in charge of the customer 
            author_update = customer_connection.customer_in_charge(customer_id)
            return author_update
        except Exception as e:
            FlashView.display_error(str(e))
