# First program 

# Collect the informations
def collect_info():
    while True:

        # Ask for the informations
        full_name = input("Full name: ").strip()

        # Set a condition that only numbers can be inputted
        while True:
            try:
                user_age = int(input("Age: "))
                break
            
            except ValueError:
                print("Invalid input. Please try again.")

        loc_address = input("Address: ").strip()
        personal_email = input("Email: ").strip()

        # Set a condition that 11-digit numbers can only be inputted
        while True:
            try:
                phone_number = input("Phone Number: ")
                if len(phone_number) != 11:
                    raise ValueError("Phone number must only consist a 11-digit number.")
                phone_number = int(phone_number)
                break
            
            except ValueError as error:
                print(error, "Input invalid. Please input 11-digit numbers only.")

        # The informations will be saved and open in a file
        with open("personal_info.txt", "a") as file:
            file.write(f"Full Name: {full_name}\n")
            file.write(f"Age: {user_age}\n")
            file.write(f"Address: {loc_address}\n")
            file.write(f"Email: {personal_email}\n")
            file.write(f"Phone Number: {phone_number}\n")
            
        print("\nInformation saved successfully.")

        # Ask for another user input
        while True:
            another_info = input("\nDo you want to input another person's information? (Yes/No): ").strip().lower()

            # Set a condition for Yes/No answer
            if another_info == "yes":
                continue
            elif another_info == "no":
                print("The program is closing.")
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No' only.")
        if another_info == "no":
            break


if __name__ == "__main__":
    collect_info()


         

