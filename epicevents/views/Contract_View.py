from controllers.Contract_Controller import ContractController
from datetime import date

class ContractView:
    def __init__(self, database_name, secret_key) -> None:
        self.user_connection = ContractController(database_name, secret_key)

    @staticmethod
    def create_contract(database_name, secret_key):
        contract_controller = ContractController(database_name, secret_key)
        try:
            title = input("Enter contract title: ")
            total_amount = float(input("Enter total amount: "))
            remaining_amount = float(input("Enter remaining amount: "))
            customer_id = int(input("Enter customer ID: "))
            commercial_user_id = int(input("Enter commercial user ID: "))
            statement_id = int(input("Enter statement ID: "))
            creation_date = date.today()
            success = contract_controller.create_contract(title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id)
            if success:
                print("Contract created successfully!")
            else:
                print("Failed to create contract.")
            return success
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def update_contract(database_name, secret_key):
        contract_controller = ContractController(database_name, secret_key)
        try:
            contract_id = int(input("Enter contract ID to be updated: "))
            title = input("Enter new contract title: ")
            total_amount = float(input("Enter new total amount: "))
            remaining_amount = float(input("Enter new remaining amount: "))
            customer_id = int(input("Enter new customer ID: "))
            commercial_user_id = int(input("Enter new commercial user ID: "))
            statement_id = int(input("Enter new statement ID: "))
            success = contract_controller.update_contract(contract_id, title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id)
            if success:
                print("Contract updated successfully!")
            else:
                print("Failed to update contract.")
            return success
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def delete_contract(database_name, secret_key):
        contract_controller = ContractController(database_name, secret_key)
        try:
            contract_id = int(input("Enter contract ID to be deleted: "))
            success = contract_controller.delete_contract(contract_id)
            if success:
                print("Contract deleted successfully!")
            else:
                print("Failed to delete contract.")
            return success
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def view_contracts(database_name, secret_key):
        contract_controller = ContractController(database_name, secret_key)
        try:
            contracts_list = contract_controller.view_contracts()
            if contracts_list:
                for contract in contracts_list:
                    print(contract)
            else:
                print("No contracts found.")
        except Exception as e:
            print(f"An error occurred: {e}")
