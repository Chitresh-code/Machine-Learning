# Concept of Strings

# Defining strings
str1 = 'Single quoted string'  # Single-quoted string
str2 = "Double quoted string"  # Double-quoted string
str3 = '''Triple quoted String'''  # Triple-quoted string

# Printing strings
print(str1)  # Output: Single quoted string
print(str2)  # Output: Double quoted string
print(str3)  # Output: Triple quoted String

# String slicing
name = "Chitresh"
length = len(name)  # Length of the string
print("Length of the string:", length)  # Output: 8

# String has 2 types of indexing
# Forward Indexing -> 0 to len-1
# Reverse Indexing -> -len to -1

# String slicing -> string[first_index : last_index]
# Here, first_index is included and last_index is not included
print(name[0:4])  # Prints characters from index 0 to index 3 from string 'name'
# Output: Chit

# Reverse indexing example
# Note: Reverse slicing with a negative step value is required for expected output
print(name[-1:-4:-1])  # Prints characters in reverse from index -1 to index -4
# Output: hse

# Slicing string with skip value
# string[first_index : last_index : skip_count]
print(name[0 : length : 2])  # Prints every second character from the string 'name'
# Output: Cies

# String functions
str = "hello World"

# len(string_name) -> returns the length of the string
l = len(str)  # Output: 11
print("Length of the string:", l)  # Output: Length of the string: 11

# string_name.endswith("substring") -> returns a boolean indicating if the string ends with the specified substring
print(str.endswith("ld"))  # Output: True

# string_name.count("substring") -> counts the total occurrence of the substring in the string
print(str.count('l'))  # Output: 3

# string_name.capitalize() -> returns a copy of the string with the first character capitalized and the rest lowercased
print(str.capitalize())  # Output: Hello world

# string_name.find('substring') -> returns the index of the first occurrence of the substring; returns -1 if not found
print(str.find(' Wo'))  # Output: 5

# string_name.replace('old_substring', 'new_substring') -> returns a copy of the string with all occurrences of old_substring replaced by new_substring
new_str = str.replace('l', 'c')
print(new_str)  # Output: hecco Worcd

# Additional string functions

# string_name.upper() -> converts all characters in the string to uppercase
print(str.upper())  # Output: HELLO WORLD

# string_name.lower() -> converts all characters in the string to lowercase
print(str.lower())  # Output: hello world

# string_name.title() -> converts the first character of each word to uppercase
print(str.title())  # Output: Hello World

# string_name.strip() -> removes leading and trailing whitespace
str_with_spaces = "   hello World   "
print(str_with_spaces.strip())  # Output: hello World

# string_name.lstrip() -> removes leading whitespace
print(str_with_spaces.lstrip())  # Output: hello World   

# string_name.rstrip() -> removes trailing whitespace
print(str_with_spaces.rstrip())  # Output:    hello World

# string_name.split(separator) -> splits the string into a list using the specified separator
print(str.split(' '))  # Output: ['hello', 'World']

# string_name.join(iterable) -> joins elements of an iterable with the string as a separator
words = ['hello', 'World']
print(' '.join(words))  # Output: hello World

# string_name.isalpha() -> returns True if all characters in the string are alphabetic
print(name.isalpha())  # Output: True

# string_name.isdigit() -> returns True if all characters in the string are digits
num_str = "12345"
print(num_str.isdigit())  # Output: True

# string_name.isalnum() -> returns True if all characters in the string are alphanumeric
alnum_str = "Chitresh123"
print(alnum_str.isalnum())  # Output: True

# string_name.isspace() -> returns True if all characters in the string are whitespace
space_str = "   "
print(space_str.isspace())  # Output: True

# string_name.startswith('substring') -> returns True if the string starts with the specified substring
print(str.startswith('he'))  # Output: True

# string_name.format() -> formats the string using placeholders
formatted_str = "Hello, {}. Welcome to {}.".format("Chitresh", "Python")
print(formatted_str)  # Output: Hello, Chitresh. Welcome to Python.

# string_name.format_map(mapping) -> formats the string using a mapping
mapping = {'name': 'Chitresh', 'language': 'Python'}
formatted_str_map = "Hello, {name}. Welcome to {language}.".format_map(mapping)
print(formatted_str_map)  # Output: Hello, Chitresh. Welcome to Python.

# string_name.islower() -> returns True if all characters in the string are lowercase
print(str.islower())  # Output: False

# string_name.isupper() -> returns True if all characters in the string are uppercase
print(str.isupper())  # Output: False

# string_name.swapcase() -> swaps case of all characters in the string
print(str.swapcase())  # Output: HELLO wORLD

# string_name.zfill(width) -> pads the string on the left with zeros to fill the specified width
num_str = "42"
print(num_str.zfill(5))  # Output: 00042

# string_name.center(width, fillchar) -> centers the string and fills the rest with the specified character
print(str.center(20, '-'))  # Output: ----hello World-----

# string_name.ljust(width, fillchar) -> left justifies the string and fills the rest with the specified character
print(str.ljust(20, '-'))  # Output: hello World---------

# string_name.rjust(width, fillchar) -> right justifies the string and fills the rest with the specified character
print(str.rjust(20, '-'))  # Output: ---------hello World

# string_name.partition('substring') -> splits the string at the first occurrence of the substring into a tuple
print(str.partition(' '))  # Output: ('hello', ' ', 'World')

# string_name.rpartition('substring') -> splits the string at the last occurrence of the substring into a tuple
print(str.rpartition(' '))  # Output: ('hello', ' ', 'World')