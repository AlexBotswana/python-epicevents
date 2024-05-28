from controllers.Contract_Controller import ContractController
from datetime import date
from views.Flash_View import FlashView

class ContractView:
    def __init__(self) -> None:
        self.user_connection = ContractController()

    @staticmethod
    def create_contract():
        contract_controller = ContractController()
        try:
            title = input("Enter contract title: ")
            total_amount = float(input("Enter total amount: "))
            remaining_amount = float(input("Enter remaining amount: "))
            customer_id = int(input("Enter customer ID: "))
            commercial_user_id = int(input("Enter commercial user ID: "))
            statement_id = int(input("Enter statement ID (1-Initial; 2-Signed; 3-Paid; 4-Cancelled): "))
            creation_date = date.today()
            success = contract_controller.create_contract(title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id)
            FlashView.display_update_result(success)
            return success
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def update_contract():
        contract_controller = ContractController()
        try:
            contract_id = int(input("Enter contract ID to be updated: "))
            author_update = contract_controller.contract_in_charge(contract_id)
            if author_update:
                title = input("Enter new contract title: ")
                total_amount = float(input("Enter new total amount: "))
                remaining_amount = float(input("Enter new remaining amount: "))
                customer_id = int(input("Enter new customer ID: "))
                commercial_user_id = int(input("Enter new commercial user ID: "))
                statement_id = int(input("Enter new statement ID (1-Initial; 2-Signed; 3-Paid; 4-Cancelled): "))
                success = contract_controller.update_contract(contract_id, title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id)
                FlashView.display_update_result(success)
                return success
            else:
                print("You are not in charge of this contract")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def delete_contract():
        contract_controller = ContractController()
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
    def view_contracts():
        contract_controller = ContractController()
        try:
            contracts_list = contract_controller.view_contracts()
            if contracts_list:
                for contract in contracts_list:
                    print(contract)
            else:
                print("No contracts found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def view_not_signed_contracts():
        contract_controller = ContractController()
        try:
            contracts_list = contract_controller.view_not_signed_contracts()
            if contracts_list:
                for contract in contracts_list:
                    print(contract)
            else:
                print("No contracts found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def view_not_paid_contracts():
        contract_controller = ContractController()
        try:
            contracts_list = contract_controller.view_not_paid_contracts()
            if contracts_list:
                for contract in contracts_list:
                    print(contract)
            else:
                print("No contracts found.")
        except Exception as e:
            print(f"An error occurred: {e}")
