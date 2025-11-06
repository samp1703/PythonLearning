user_text1 = input("Enter text to write to the file: ")

with open("sample1.txt", "w") as file:
    file.write(f"{user_text1}\n")

user_text2 = input("Enter additional text to append: ")
with open("sample1.txt", "a") as file:
    file.write(f"{user_text2}\n")

file = open("sample1.txt", 'r')
contents = file.read()
print("Final content of Sample.txt:")
print(contents)
file.close()