from models.Event_Model import EventModel

class EventController:
    def __init__(self, database_name, secret_key):
        self.event_model = EventModel(database_name)
        self.secret_key = secret_key

    def create_event(self, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id):
        try:
            success = self.event_model.create_event(title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id)
            return success
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def update_event(self, event_id, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id):
        try:
            success = self.event_model.update_event(event_id, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id)
            return success
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def delete_event(self, event_id):
        try:
            success = self.event_model.delete_event(event_id)
            return success
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def view_events(self):
        try:
            events_list = self.event_model.view_events()
            return events_list
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
