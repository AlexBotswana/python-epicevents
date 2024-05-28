from controllers.Event_Controller import EventController
from views.Flash_View import FlashView

class EventView:
    def __init__(self) -> None:
        self.user_connection = EventController()

    @staticmethod
    def create_event():
        event_controller = EventController()
        try:
            title = input("Enter event title: ")
            begin_date = input("Enter begin date (YYYY-MM-DD HH:MM): ")
            end_date = input("Enter end date (YYYY-MM-DD HH:MM): ")
            located = input("Enter event location: ")
            attendees = int(input("Enter number of attendees: "))
            notes = input("Enter event notes: ")
            contract_id = int(input("Enter contract ID: "))
            support_user_id = int(input("Enter support user ID: "))
            success = event_controller.create_event(title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id)
            FlashView.display_creation_result(success)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def update_event():
        event_controller = EventController()
        try:
            event_id = int(input("Enter event ID to be updated: "))
            author_update = event_controller.support_in_charge(event_id)
            if author_update:
                title = input("Enter new event title: ")
                begin_date = input("Enter new begin date (YYYY-MM-DD HH:MM): ")
                end_date = input("Enter new end date (YYYY-MM-DD HH:MM): ")
                located = input("Enter new event location: ")
                attendees = int(input("Enter new number of attendees: "))
                notes = input("Enter new event notes: ")
                support_user_id = input("Enter new support user ID: ")
                success = event_controller.update_event(event_id, title, begin_date, end_date, located, attendees, notes, support_user_id)
                FlashView.display_update_result(success)
                return success
            else:
                print("You are not in charge of this event")
                return False
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def update_event_support():
        # add a support to an event
        event_controller = EventController()
        try:
            event_id = int(input("Enter event ID to be updated: "))
            support_user_id = input("Enter new support user ID: ")
            success = event_controller.update_event_support(event_id, support_user_id)
            if success:
                print("Support added successfully!")
            else:
                print("Failed to update event.")
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def delete_event():
        event_controller = EventController()
        try:
            event_id = int(input("Enter event ID to be deleted: "))
            success = event_controller.delete_event(event_id)
            FlashView.display_delete_result(success)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def view_events():
        event_controller = EventController()
        try:
            events_list = event_controller.view_events()
            if events_list:
                for event in events_list:
                    print(event)
            else:
                print("No events found.")
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def view_events_wo_support():
        event_controller = EventController()
        try:
            events_list = event_controller.view_events_wo_support()
            if events_list:
                for event in events_list:
                    print(event)
            else:
                print("No events found.")
        except Exception as e:
            FlashView.display_error(str(e))

    @staticmethod
    def view_events_for_support():
        event_controller = EventController()
        try:
            events_list = event_controller.view_events_for_support()
            if events_list:
                for event in events_list:
                    print(event)
            else:
                print("No events found.")
        except Exception as e:
            FlashView.display_error(str(e))
