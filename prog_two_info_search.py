# Second Program

# Open the txt file and serach the information that is being asked
def open_info():
    try:
        with open("personal_info.txt", "r") as file:
            data_info = file.read()
    except FileNotFoundError:
        print("Error: 'personal_info.txt' not found. Please run Program 1 first to create a file.")
        return
    
    while True:
        search_name = input("Enter the full name: ")
    
if __name__ == "__main__":
    open_info()