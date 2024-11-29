# First program 

# Collect the informations
def collect_info():
    while True:

        # Ask for the informations
        full_name = input("Full name: ")
        user_age = input("Age: ")
        loc_address = input("Address: ")
        personal_email = input("Email: ")
        phone_number = input("Phone Number: ")

        another = input("Do you want to input another person's information? (Yes/No): ")

        if another != "Yes":
            break 

if __name__ == "__main__":
    collect_info()


         

