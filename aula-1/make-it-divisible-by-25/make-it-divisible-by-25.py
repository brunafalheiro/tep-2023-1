def min_digits(n):
  list_n = list(str(n))
  length = len(list_n)

  # Initialize result as infinity
  result = float('inf')
  
  for i in range(length):
    for j in range(i + 1, length):
      # Combine the list_n at positions i and j to form a number
      num = int(list_n[i] + list_n[j])
      if num % 25 == 0:
        # Calculate the number of list_n to be removed before the formed number
        removed_before = j - i - 1

        # Calculate the number of list_n to be removed after the formed number
        removed_after = length - (j + 1)

        # Set the minor number of list_n to be removed
        result = min(result, removed_before + removed_after)
  return result if result != float('inf') else -1

t = int(input())
for _ in range(t):
  n = int(input())
  print(min_digits(n))
