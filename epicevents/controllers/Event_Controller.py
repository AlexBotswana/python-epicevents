from models.Event_Model import EventModel
from models.User_Model import UserModel
from models.Contract_Model import ContractModel
from views.Flash_View import FlashView
from dotenv import load_dotenv, find_dotenv, dotenv_values

class EventController:
    def __init__(self):
        self.event_model = EventModel()
        self.user_model = UserModel()
        self.contract_model = ContractModel()

    # Function to know if the user connected is in charge of the event or is the user manager (superuser, job = 1)
    def support_in_charge(self, event_id):
        try:
            # find .env file
            env_path = find_dotenv('.env')
            # reload var environnement
            load_dotenv(env_path)
            env_vars = dotenv_values(env_path)
            USER_ID_CONNECTED = env_vars['USER_ID']
            # support in charge of the event
            support_id = self.event_model.view_single_event(event_id)
            job_id_user_connected = self.user_model.get_user_permissions(USER_ID_CONNECTED)
            print(USER_ID_CONNECTED)
            if support_id[0] != '':
                if (int(support_id[0]) == int(USER_ID_CONNECTED)) or (int(job_id_user_connected) == 1):
                    return True
                else:
                    return False
            elif int(job_id_user_connected) == 1:
                return True
            else:
                return False
        except Exception as e:
            FlashView.display_error(str(e))

    def create_event(self, title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id):
        try:
            success = self.event_model.create_event(title, begin_date, end_date, located, attendees, notes, contract_id, support_user_id)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def update_event(self, event_id, title, begin_date, end_date, located, attendees, notes, support_user_id):
        try:
            success = self.event_model.update_event(event_id, title, begin_date, end_date, located, attendees, notes, support_user_id)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def update_event_support(self, event_id, support_user_id):
        # add a support to an event
        try:
            success = self.event_model.update_event_support(event_id, support_user_id)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def delete_event(self, event_id):
        try:
            success = self.event_model.delete_event(event_id)
            return success
        except Exception as e:
            FlashView.display_error(str(e))

    def view_events(self):
        try:
            events_list = self.event_model.view_events()
            if events_list:
                # replace customer id by customer lastname for user in charge of the customer
                for i in range(len(events_list)):
                    event_list = list(events_list[i])
                    contract = self.contract_model.view_single_contract(int(event_list[7])) # info contract with contract id
                    event_list[7] = contract[1] # Contract title
                    if event_list[8]:
                        event_list[8] = self.user_model.get_username(int(event_list[8])) # support username
                    events_list[i] = tuple(event_list)
            return events_list
        except Exception as e:
            FlashView.display_error(str(e))

    def view_events_wo_support(self):
        try:
            events_list = self.event_model.view_events_wo_support()
            if events_list:
                # replace customer id by customer lastname for user in charge of the customer
                for i in range(len(events_list)):
                    event_list = list(events_list[i])
                    contract = self.contract_model.view_single_contract(int(event_list[7])) # info contract with contract id
                    event_list[7] = contract[1] # Contract title
                    events_list[i] = tuple(event_list)
            return events_list
        except Exception as e:
            FlashView.display_error(str(e))

    def view_events_for_support(self):
        try:
            events_list = self.event_model.view_events_for_support()
            if events_list:
                # replace customer id by customer lastname for user in charge of the customer
                for i in range(len(events_list)):
                    event_list = list(events_list[i])
                    contract = self.contract_model.view_single_contract(int(event_list[7])) # info contract with contract id
                    event_list[7] = contract[1] # Contract title
                    events_list[i] = tuple(event_list)
            return events_list
        except Exception as e:
            FlashView.display_error(str(e))
