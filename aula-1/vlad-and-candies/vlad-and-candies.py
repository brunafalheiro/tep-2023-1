def canEatCandies(candies):
  if max(candies) % sum(candies) == 0:
    print("YES")
    return
  if max(candies) <= (sum(candies) - max(candies)) % 2:
    print("YES")
  else:
    print("NO")

# The number of test cases
t = int(input())

for i in range(t):
  # The number of types of candies
  n = int(input())
  # The number of candies for each type. Turns an input like '1 1 1' into [1,1,1]
  candies = list(map(int, input().split()))
  print(canEatCandies(candies))