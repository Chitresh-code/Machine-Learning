# fill in a letter template given below with name and date
"""
letter = '''
Dear <|Name|>,
    You are selected!
    <|Date|>
'''
"""
from datetime import datetime

letter = '''
Dear <|Name|>,
    You are selected!
    <|Date|>
'''
name = input("Enter your name: ")
date = datetime.now().strftime("%d-%m-%Y")

filled_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)
print(filled_letter)