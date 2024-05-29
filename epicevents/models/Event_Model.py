import sqlite3
from config import DATABASE_NAME
from views.Flash_View import FlashView
from dotenv import find_dotenv, load_dotenv, dotenv_values

class EventModel:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.conn.cursor()

    def create_event(self, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id):
        try:
            query = "INSERT INTO Events (title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, (title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def update_event(self, event_id, title, begin_date, end_date, located, attendees, notes, support_user_id):
        try:
            query = "UPDATE Events SET title = ?, begin_date = ?, end_date = ?, located = ?, attendees = ?, notes = ?, support_user_id = ? WHERE id = ? "
            self.cursor.execute(query, (title, begin_date, end_date, located, attendees, notes, support_user_id, event_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
           FlashView.display_error(str(e))

    def update_event_support(self, event_id, support_user_id):
        # add a support to an event
        try:
            query = "UPDATE Events SET support_user_id = ? WHERE id = ? "
            self.cursor.execute(query, (support_user_id, event_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
           FlashView.display_error(str(e))

    def delete_event(self, event_id):
        try:
            query = "DELETE FROM Events WHERE id = ?"
            self.cursor.execute(query, (event_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_events(self):
        try:
            query = "SELECT id, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id FROM Events"
            self.cursor.execute(query)
            events_list = self.cursor.fetchall()
            return events_list if events_list else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_single_event(self, event_id):
        try:
            query = "SELECT support_user_id, title, begin_date, end_date, located, attendees, notes, contract_id FROM Events WHERE id = ?"
            self.cursor.execute(query, (event_id,))
            event = self.cursor.fetchone()
            return event if event else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_events_wo_support(self):
        try:
            query = "SELECT id, title, begin_date, end_date, located, attendees, notes, contract_id FROM Events WHERE support_user_id = ''"
            self.cursor.execute(query)
            events_list = self.cursor.fetchall()
            return events_list if events_list else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))

    def view_events_for_support(self):
        try:
            # find .env file
            env_path = find_dotenv('.env')
            # reload var environnement
            load_dotenv(env_path)
            env_vars = dotenv_values(env_path)
            USER_ID_CONNECTED = env_vars['USER_ID']
            query = "SELECT id, title, begin_date, end_date, located, attendees, notes, contract_id FROM Events WHERE support_user_id = ?"
            self.cursor.execute(query, (USER_ID_CONNECTED,))
            events_list = self.cursor.fetchall()
            return events_list if events_list else None
        except sqlite3.Error as e:
            FlashView.display_error(str(e))
