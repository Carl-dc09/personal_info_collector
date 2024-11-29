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
        search_name = input("Enter the full name: ").strip()

        if search_name in data_info:
            print("Information Found!")

            records = data_info.split("-" * 40)

            for record in records:
                if f"Full Name: {search_name}" in record: 
                    print(record.strip())
                    break
        else:
            print("No records found.")
    
if __name__ == "__main__":
    open_info()