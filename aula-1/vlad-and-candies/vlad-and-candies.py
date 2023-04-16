n = int(input())
for _ in range(n):
  totalCandies = int(input())
  candieTypes = list(map(int, input().split()))
  mostFrequentCandie = max(candieTypes)
  index = candieTypes.index(mostFrequentCandie)
  if mostFrequentCandie == 1:
    print("YES")
    continue
  for i in range(totalCandies):
    canEat = candieTypes[i] == mostFrequentCandie and i != index or candieTypes[i] == mostFrequentCandie - 1
    if canEat:
      break
  print("YES" if canEat else "NO")