#Read a File and Handle Errors

def open_file(filename):
    try:
        # Try to open the file in read ('r') mode
        i=0
        with open(filename, 'r') as file:
            for line in file:
                i=i+1
                print(f"Line {i} : {line}", end='')

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
file_name = input("Input a file name: ")
open_file(file_name)

