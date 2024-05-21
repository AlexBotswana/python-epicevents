from models.Contract_Model import ContractModel

class ContractController:
    def __init__(self, database_name, secret_key):
        self.contract_model = ContractModel(database_name)
        self.secret_key = secret_key

    def create_contract(self, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id):
        try:
            success = self.contract_model.create_contract(title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id)
            return success
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def update_contract(self, contract_id, title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id):
        try:
            success = self.contract_model.update_contract(contract_id, title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id)
            return success
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def delete_contract(self, contract_id):
        try:
            success = self.contract_model.delete_contract(contract_id)
            return success
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def view_contracts(self):
        try:
            contracts_list = self.contract_model.view_contracts()
            return contracts_list
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
