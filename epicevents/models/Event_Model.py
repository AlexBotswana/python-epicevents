import sqlite3

class EventModel:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_event(self, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id):
        try:
            query = "INSERT INTO Events (title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, (title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False, str(e)

    def update_event(self, event_id, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id):
        try:
            query = "UPDATE Events SET title = ?, begin_date = ?, end_date = ?, located = ?, attendees = ?, notes = ?, contract_id = ?, support_user_id = ? WHERE id = ? "
            self.cursor.execute(query, (title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id, event_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False, str(e)

    def delete_event(self, event_id):
        try:
            query = "DELETE FROM Events WHERE id = ?"
            self.cursor.execute(query, (event_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False, str(e)

    def view_events(self):
        try:
            query = "SELECT id, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id FROM Events"
            self.cursor.execute(query)
            events_list = self.cursor.fetchall()
            return events_list if events_list else None
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
