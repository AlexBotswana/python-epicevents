from controllers.Event_Controller import EventController

class EventView:
    def __init__(self, database_name, secret_key) -> None:
        self.user_connection = EventController(database_name, secret_key)

    @staticmethod
    def create_event(database_name, secret_key):
        event_controller = EventController(database_name, secret_key)
        try:
            title = input("Enter event title: ")
            begin_date = input("Enter begin date (YYYY-MM-DD HH:MM:SS): ")
            end_date = input("Enter end date (YYYY-MM-DD HH:MM:SS): ")
            located = input("Enter event location: ")
            attendees = int(input("Enter number of attendees: "))
            notes = input("Enter event notes: ")
            contract_id = int(input("Enter contract ID: "))
            support_user_id = int(input("Enter support user ID: "))
            success = event_controller.create_event(title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id)
            if success:
                print("Event created successfully!")
            else:
                print("Failed to create event.")
            return success
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def update_event(database_name, secret_key):
        event_controller = EventController(database_name, secret_key)
        try:
            event_id = int(input("Enter event ID to be updated: "))
            title = input("Enter new event title: ")
            begin_date = input("Enter new begin date (YYYY-MM-DD HH:MM:SS): ")
            end_date = input("Enter new end date (YYYY-MM-DD HH:MM:SS): ")
            located = input("Enter new event location: ")
            attendees = int(input("Enter new number of attendees: "))
            notes = input("Enter new event notes: ")
            contract_id = int(input("Enter new contract ID: "))
            support_user_id = int(input("Enter new support user ID: "))
            success = event_controller.update_event(event_id, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id)
            if success:
                print("Event updated successfully!")
            else:
                print("Failed to update event.")
            return success
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def delete_event(database_name, secret_key):
        event_controller = EventController(database_name, secret_key)
        try:
            event_id = int(input("Enter event ID to be deleted: "))
            success = event_controller.delete_event(event_id)
            if success:
                print("Event deleted successfully!")
            else:
                print("Failed to delete event.")
            return success
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def view_events(database_name, secret_key):
        event_controller = EventController(database_name, secret_key)
        try:
            events_list = event_controller.view_events()
            if events_list:
                for event in events_list:
                    print(event)
            else:
                print("No events found.")
        except Exception as e:
            print(f"An error occurred: {e}")
