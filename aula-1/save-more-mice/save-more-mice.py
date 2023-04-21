t = int(input())
for _ in range(t):
  # Get hole point and the the number of mices
  n, k = list(map(int, input().split()))

  # Get the list of positions of the mices and sort it in ascending order
  mices = list(map(int, input().split()))
  mices.sort()
  cat_position = 0
  rescued = 0

  for index in range(k-1,-1,-1):
    if mices[index] == n:
      rescued += 1
    elif mices[index] <= n:
      # If the position of the mice is less than or equal to the hole and the position of the mice 
      # is greater than the current position of the cat, rescue the mice and update the position of
      # the cat
      if cat_position < mices[index]:
        rescued += 1
        cat_position = cat_position + n - mices[index]
  print(rescued)
  