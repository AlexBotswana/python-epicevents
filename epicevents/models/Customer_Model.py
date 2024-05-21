import sqlite3
from views.Display_View import DisplayView

class CustomerModel:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    def test_database_connection(database_name):
        try:
            conn = sqlite3.connect(database_name)
            print("Connexion à la base de données réussie !")
            conn.close()
        except sqlite3.Error as e:
            print("Erreur lors de la connexion à la base de données :", e)

    def create_customer(self, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id):
        try:
            query = "INSERT INTO Customers (firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, (firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("An error occurred:", e)
            return False

    def update_customer(self, customer_id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id):
        try:
            query = "UPDATE Customers SET firstname = ?, lastname = ?, email = ?, phone = ?, company_name = ?, located = ?, creation_date = ?, last_contact_date = ?, commercial_user_id = ? WHERE id = ?"
            self.cursor.execute(query, (firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id, customer_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("An error occurred:", e)
            return False

    def view_customers(self):
        try:
            query = "SELECT id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id FROM Customers"
            self.cursor.execute(query)
            list_customers = self.cursor.fetchall()
            return list_customers if list_customers else None
        except sqlite3.Error as e:
            return False, str(e)

    def delete_customer(self, customer_id):
        try:
            query = "DELETE FROM Customers WHERE id = ?"
            self.cursor.execute(query, (customer_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            return False, str(e)
