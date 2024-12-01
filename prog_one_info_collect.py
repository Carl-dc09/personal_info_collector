# First program 

# Collect the informations
def collect_info():
    while True:

        # Ask for the informations
        full_name = input("Full name (Last Name, First Name, M.I.): ").strip()

        # Set a condition that only numbers can be inputted
        while True:
            try:
                user_age = int(input("Age: "))
                break

            except ValueError:
                print("Invalid input. Please try again.")
                
        while True:
            gender_info = input("Gender (Male/Female/Prefer Not To Say): ").strip().lower()

            # Set a condition when asking for gender.
            if gender_info == "male":
                break
            elif gender_info == "female":
                break    
            elif gender_info == "prefer not to say":
                break
            else:
                print("Invalid input. Please enter 'Male', 'Female', or 'Prefer Not To Say' only.")        
        
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
                
        birth_date = input("Date of Birth: ").strip()
        birth_place = input("Place of Birth: ").strip()
        mother_name = input("Mother's Name: ").strip()
        father_name = input("Father's Name: ").strip()
        marital_status = input("Marital Status: ").strip()        
        user_nationality = input("Nationality: ").strip()
        user_occupation = input("Occupation: ").strip()
        user_ethnicity = input("Ethnicity: ").strip()
        user_religion = input("Religion: ").strip()
        user_education = input("Education (Primary/Secondary/College): ").strip()
        user_hobby = input("Hobby: ").strip()      

        # The informations will be saved and open in a file
        with open("personal_info.txt", "a") as file:
            file.write(f"Full Name: {full_name}\n")
            file.write(f"Age: {user_age}\n")
            file.write(f"Gender: {gender_info}\n")
            file.write(f"Address: {loc_address}\n")
            file.write(f"Email: {personal_email}\n")
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Date of Birth: {birth_date}\n")
            file.write(f"Place of Birth: {birth_place}\n")
            file.write(f"Mother's Name: {mother_name}\n")
            file.write(f"Father's Name: {father_name}\n")
            file.write(f"Marital Status: {marital_status}\n")
            file.write(f"Nationality: {user_nationality}\n")
            file.write(f"Occupation: {user_occupation}\n")
            file.write(f"Ethnicity: {user_ethnicity}\n")
            file.write(f"Religion: {user_religion}\n")
            file.write(f"Education: {user_education}\n")
            file.write(f"Hobby: {user_hobby}\n")
            file.write("-" * 40 + "\n") # Separator for different user information

        print("\n--- Information saved successfully. ---")

        # Ask for another user input
        while True:
            another_info = input("\nDo you want to input another person's information? (Yes/No): ").strip().lower()

            # Set a condition for Yes/No answer
            if another_info == "yes":
                break
            elif another_info == "no":
                print("The program is closing.")
                return
            else:
                print("Invalid input. Please enter 'Yes' or 'No' only.")

# Run the program
if __name__ == "__main__":
    collect_info()