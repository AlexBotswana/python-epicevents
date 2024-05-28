import sqlite3
from views.Flash_View import FlashView
from config import DATABASE_NAME, USER_ID_CONNECTED

class CustomerModel:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    def test_database_connection():
        try:
            conn = sqlite3.connect(DATABASE_NAME)
            print("Connexion à la base de données réussie !")
            conn.close()
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def create_customer(self, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date):
        try:
            query = "INSERT INTO Customers (firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, (firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, USER_ID_CONNECTED))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def update_customer(self, customer_id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id):
        try:
            query = "UPDATE Customers SET firstname = ?, lastname = ?, email = ?, phone = ?, company_name = ?, located = ?, creation_date = ?, last_contact_date = ?, commercial_user_id = ? WHERE id = ?"
            self.cursor.execute(query, (firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id, customer_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_customers(self):
        try:
            query = "SELECT id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id FROM Customers"
            self.cursor.execute(query)
            list_customers = self.cursor.fetchall()
            return list_customers if list_customers else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_single_customer(self, customer_id):
        try:
            query = "SELECT commercial_user_id, firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, id FROM Customers WHERE id = ?"
            self.cursor.execute(query, (customer_id,))
            customer = self.cursor.fetchone()
            return customer if customer else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def delete_customer(self, customer_id):
        try:
            query = "DELETE FROM Customers WHERE id = ?"
            self.cursor.execute(query, (customer_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            FlashView.display_error(str(e))
