# Imports
import re

# Functions
# Check if the given string is allowed
def match(str):
    # Regex pattern: Aceppts only 0's, 1's
    regex = re.compile('^(?!.*\n)[01]*$')
    if not re.search(regex,str):
        print(str)
        
def sum_digits(str):
    return sum(int(x) for x in str)


str = input('str: ')
match(str)
