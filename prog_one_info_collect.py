# First program 

# Collect the informations
def collect_info():
    while True:

        # Ask for the informations
        full_name = input("Full name: ").strip()

        while True:
            try:
                user_age = int(input("Age: "))
                break
        
            except ValueError:
                print("Invalid input. Please try again.")

        loc_address = input("Address: ").strip()
        personal_email = input("Email: ").strip()

        while True:
            try:
                phone_number = input("Phone Number: ")
                if len(phone_number) != 11:
                    raise ValueError("Phone number must only consist a 11-digit number.")
                phone_number = int(phone_number)
                break
            
            except ValueError as error:
                print(error, "Input invalid. Please input 11-digit numbers only.")
                
        # Ask for another user input
        another = input("Do you want to input another person's information? (Yes/No): ")

        if another != "Yes":
            print("\nInformation Saved Successfully!")
            break

if __name__ == "__main__":
    collect_info()


         

