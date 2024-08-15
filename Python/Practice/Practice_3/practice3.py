#  detect double space in a string
str = input("Enter a string: ")
index = str.find("  ")

if index == -1:
    print("No double spaces found")
else:
    print(f"Double spaces found at index {index}")