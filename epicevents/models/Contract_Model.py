import sqlite3

class ContractModel:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_contract(self, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id):
        try:
            query = "INSERT INTO Contracts (title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, (title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False, str(e)

    def update_contract(self, contract_id, title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id):
        try:
            query = "UPDATE Contracts SET title = ?, total_amount = ?, remaining_amount = ?, customer_id = ?, commercial_user_id = ?, statement_id = ? WHERE id = ?"
            self.cursor.execute(query, (title, total_amount, remaining_amount, customer_id, commercial_user_id, statement_id, contract_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False, str(e)

    def delete_contract(self, contract_id):
        try:
            query = "DELETE FROM Contracts WHERE id = ?"
            self.cursor.execute(query, (contract_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False, str(e)

    def view_contracts(self):
        try:
            query = "SELECT id, title, total_amount, remaining_amount, creation_date, customer_id, commercial_user_id, statement_id FROM Contracts"
            self.cursor.execute(query)
            contracts_list = self.cursor.fetchall()
            return contracts_list if contracts_list else None
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
