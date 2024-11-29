# Second Program

# 
def open_info():
    try:
        with open("personal_info.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("Error: 'personal_info.txt' not found. Please run Program 1 first to create a file.")
        return
    
if __name__ == "__main__":
    open_info()