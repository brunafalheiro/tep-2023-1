#----------------------------#
#           IMPORTS          #
#----------------------------#
import re

#----------------------------#
#         FUNCTIONS          #
#----------------------------#
# Sum all the digits from the string        
def sum_digits(str):
  return sum(int(x) for x in str)

# Check minority of characters of a given substring
def check_minority(sum, length):
  #----------------------------#
  #        NO MINORITY         #
  #----------------------------#
  # Same amount of 1's and 0's
  if sum == length / 2:
    return 'No minority'

  # Only 0's
  if sum == 0:
    return 'No minority'
  
  # Only 1's
  if sum == length:
    return 'No minority'

  #----------------------------#
  #       0's MINORITY         #
  #----------------------------#
  if sum > length / 2:
    return '0 minority'

  #----------------------------#
  #       1's` MINORITY        #
  #----------------------------#
  if sum < length / 2:
    return '1 minority'

# Main
def main():
  str = input()

  # Check if the given string is allowed
  regex = re.compile('^(?!.*\n)[01]*$') # Regex pattern: Aceppts only 0's, 1's
  if not re.search(regex,str):
    print(0)
    return

  length = len(str)
  sum = sum_digits(str)

  minority = check_minority(sum, length)
  
  if minority == 'No minority':
    print(0)
  if minority == '0 minority':
    print(length - sum)
  if minority == '1 minority':
    print(sum)
  
# Call main function
main()