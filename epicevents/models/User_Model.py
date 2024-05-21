import sqlite3
from views.Display_View import DisplayView

class UserModel:
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

    def authenticate_user(self, username, password):
        try:
            query_pwd = "SELECT pwd FROM Users WHERE username = ?"
            self.cursor.execute(query_pwd, (username,))
            hashed_pwd_db = self.cursor.fetchone()[0]
            query = "SELECT id FROM Users WHERE username = ?"
            self.cursor.execute(query, (username,))
            user_id = self.cursor.fetchone()[0]
            if user_id is not None:
                if password == hashed_pwd_db:
                    return True, user_id
                else:
                    return False, user_id
            else:
                return False, None
        except sqlite3.Error as e:
            DisplayView.display_error(str(e))
            #return False, None, str(e)

    def get_pwd_salt(self, username):
        try:
            query = "SELECT salt FROM Users WHERE username = ?"
            self.cursor.execute(query, (username,))
            salt = self.cursor.fetchone()[0]
            return salt if salt else None
        except sqlite3.Error as e:
            return None, str(e)
    
    def get_user_permissions(self, user_id):
        try:
            query = "SELECT job_id FROM Users WHERE id = ?"
            self.cursor.execute(query, (user_id,))
            job = self.cursor.fetchone()[0]
            return job if job else None
        except sqlite3.Error as e:
            return None, str(e)

    def create_user(self, username, password, job_id, salt):
        try:
            query = "INSERT INTO Users (username, pwd, job_id, salt) VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, (username, password, job_id, salt))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("An error occurred:", e)
            return False, str(e)

    def update_user(self, username, password, job_id, firstname, lastname, salt):
        try:
            query = "UPDATE Users SET pwd = ?, job_id = ?, firstname = ?, lastname = ?, salt = ? WHERE username = ?"
            self.cursor.execute(query, (password, job_id,firstname, lastname, salt, username))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("An error occurred:", e)
            return False

    def view_users(self):
        try:
            query = "SELECT username, job_id, firstname, lastname, id FROM Users"
            self.cursor.execute(query)
            list_users = self.cursor.fetchall()
            return list_users if list_users else None
        except sqlite3.Error as e:
            return False, str(e)

    def delete_user(self, username):
        try:
            query = "DELETE FROM Users WHERE username = ?"
            self.cursor.execute(query, (username,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            return False, str(e)