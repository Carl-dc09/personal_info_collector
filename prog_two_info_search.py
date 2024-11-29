# Second Program

# Open the txt file and serach the information that is being asked
def open_info():
    try:
        with open("personal_info.txt", "r") as file:
            data_info = file.read()
    except FileNotFoundError:
        print("Error: 'personal_info.txt' not found. Please run Program 1 first to create a file.")
        return
    
    # Search for the information using the name
    while True:
        search_name = input("Enter the full name: ").strip().lower()

        recorded_infos = data_info.split("-" * 40)

        found_info = False 

        for record_info in recorded_infos:
            if f"Full Name:".lower() in record_info.lower() and search_name in record_info.lower(): 
                start_index = record_info.lower().find("full name:") + len("full name:")
                end_index = record_info.lower().find("\n", start_index)
                full_name = record_info[start_index:end_index].strip().lower()

                if search_name in full_name:
                    print("\n ---Information Found! ---")
                    print(record_info.strip())
                    found_info = True

        if not found_info:
            print("\nNo records found.")

        # Ask if they want to search for another person's information
        while True:
            another_info = input("\nDo you want to search for another person's information? (Yes/No): ").strip().lower()

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
    open_info()
