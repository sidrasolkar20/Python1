# Exp04(Poatlab02)
# Aim:Write a program in Python to Perform following operations on file handling
# Name: Sidra Solkar
# UIN:231P087
# Roll No.:43
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")

def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
        print(f"Content written to '{file_name}' successfully.")

def append_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
        print(f"Content appended to '{file_name}' successfully.")

if __name__ == "__main__":
 
    write_to_file('example.txt', 'This is the initial content.\n')

    append_to_file('example.txt', 'This is some appended content.\n')

    read_file('example.txt')

    print("\nName: Sidra Solkar \nUIN:231P087 \nRoll no:43")
