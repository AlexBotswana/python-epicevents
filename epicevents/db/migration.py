import sqlite3
from controllers.User_Controller import UserController

def create_database(database_name):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS Jobs (
                id INTEGER PRIMARY KEY,
                title VARCHAR(255)
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        pwd VARCHAR(255) NOT NULL,
        firstname VARCHAR(255),
        lastname VARCHAR(255),
        salt VARCHAR(255),
        job_id INTEGER NOT NULL,
        FOREIGN KEY (job_id) REFERENCES Jobs(id)
        )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(255),
        lastname VARCHAR(255),
        email VARCHAR(255) UNIQUE NOT NULL,
        phone VARCHAR(255),
        company_name VARCHAR(255),
        located VARCHAR(255),
        creation_date DATE NOT NULL,
        last_contact_date DATE,
        commercial_user_id INTEGER,
        FOREIGN KEY (commercial_user_id) REFERENCES Users(id)
        )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Statements (
        id INTEGER PRIMARY KEY,
        statement_name VARCHAR(255) 
        )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Contracts (
        id INTEGER PRIMARY KEY,
        title VARCHAR(255),
        total_amount DECIMAL(10, 2),
        remaining_amount DECIMAL(10, 2),
        creation_date DATETIME,
        customer_id INTEGER,
        commercial_user_id INTEGER,
        statement_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES Customers(id),
        FOREIGN KEY (commercial_user_id) REFERENCES Users(id),
        FOREIGN KEY (statement_id) REFERENCES Statements(id)
        )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Events (
        id INTEGER PRIMARY KEY,
        title VARCHAR(255),
        begin_date DATETIME,
        end_date DATETIME,
        located VARCHAR(255),
        attendees INTEGER,
        notes TEXT,
        contract_id INTEGER,
        support_user_id INTEGER,
        FOREIGN KEY (contract_id) REFERENCES Contracts(id),
        FOREIGN KEY (support_user_id) REFERENCES Users(id)
        )''')

def load_data_from_sql_file(sql_file, database_name, secret_key):
    # Connect to the database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # test if manager already exists
    if sql_file == './db/manager_dataset.sql':
        query = "SELECT * FROM Users WHERE username = 'manager'"
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            pass
        else:
            user_connection = UserController(database_name, secret_key)
            username = "manager"
            password = "manager123"
            job_id = 1
            user_connection.create_user(username, password, job_id)
            # Read SQL file
            with open(sql_file, 'r') as f:
                sql_script = f.read()
                # Execute SQL script
                cursor.executescript(sql_script)
    else:
        # Read SQL file
        with open(sql_file, 'r') as f:
            sql_script = f.read()
            # Execute SQL script
            cursor.executescript(sql_script)

    # Commit changes and close connection
    conn.commit()
    conn.close()
