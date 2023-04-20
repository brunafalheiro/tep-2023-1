t = int(input())

for _ in range(t):
  # Get hole point and the the number of mices
  n, k = list(map(int, input().split()))

  # Get the list of positions of the mices and sort it in ascending order
  arr = list(map(int, input().split())).sort()

  cat_position = 0
  rescued = 0

  for i in range(k-1, -1, -1):
    if arr[i] == n:
      rescued = rescued + 1
    elif arr[i] <= n:
      # If the position of the mice is less than or equal to the hole and the position of the mice 
      # is greater than the current position of the cat, rescue the mice and update the position of
      # the cat
      if cat_position < arr[i]:
        rescued = rescued + 1
        cat_position = cat_position + n - arr[i]
  print(rescued)
  