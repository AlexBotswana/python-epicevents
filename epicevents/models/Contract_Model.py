import sqlite3
import sentry_sdk
from config import DATABASE_NAME
from views.Flash_View import FlashView


class ContractModel:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.conn.cursor()

    def create_contract(self, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id):
        try:
            query = "INSERT INTO Contracts (title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, (title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def update_contract(self, contract_id, title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id):
        try:
            query = "UPDATE Contracts SET title = ?, total_amount = ?, remaining_amount = ?, customer_id = ?, commercial_user_id = ?, statement_id = ? WHERE id = ?"
            self.cursor.execute(query, (title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id, contract_id))
            self.conn.commit()
            # Register into Sentry if a contract is signed (statement_id = 2)
            if int(statement_id) == 2:
                sentry_sdk.capture_message(f"Contract Signed : {title}", level="info")
            return True
        except sqlite3.Error as e:
            sentry_sdk.capture_exception(e)
            FlashView.display_error(str(e))

    def delete_contract(self, contract_id):
        try:
            query = "DELETE FROM Contracts WHERE id = ?"
            self.cursor.execute(query, (contract_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_contracts(self):
        try:
            query = "SELECT id, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id FROM Contracts"
            self.cursor.execute(query)
            contracts_list = self.cursor.fetchall()
            return contracts_list if contracts_list else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_single_contract(self, contract_id):
        try:
            query = "SELECT id, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id FROM Contracts WHERE id = ?"
            self.cursor.execute(query, (contract_id,))
            contract = self.cursor.fetchone()
            return contract if contract else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_not_signed_contracts(self):
        try:
            query = "SELECT id, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id FROM Contracts WHERE statement_id != 2"
            self.cursor.execute(query)
            contracts_list = self.cursor.fetchall()
            return contracts_list if contracts_list else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_not_paid_contracts(self):
        try:
            query = "SELECT id, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id FROM Contracts WHERE statement_id != 3"
            self.cursor.execute(query)
            contracts_list = self.cursor.fetchall()
            return contracts_list if contracts_list else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def get_statement_name(self, id):
        try:
            query = "SELECT statement_name FROM Statements WHERE id = ?"
            self.cursor.execute(query, (id,))
            statement_name = self.cursor.fetchone()[0]
            return statement_name if statement_name else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))