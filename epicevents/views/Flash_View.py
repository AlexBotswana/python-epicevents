class FlashView:
    @staticmethod
    def display_authent_result(success):
        if success:
            print("Authentification successful !")
        else:
            print("Authentification failed. Invalid username or password")

    @staticmethod
    def display_authorization_result(success):
        if success:
            print("Authorization successful")
        else:
            print("Authorization failed. You do not have the required permissions.")

    @staticmethod
    def display_creation_result(success):
        if success:
            print("Creation successful !")
        else:
            print("Creation failed.")

    @staticmethod
    def display_update_result(success):
        if success:
            print("Update successful !")
        else:
            print("Update failed.")

    @staticmethod
    def display_delete_result(success):
        if success:
            print("Delete successful !")
        else:
            print("Delete failed.")

    @staticmethod
    def display_error(message):
        print("Error:", message)
