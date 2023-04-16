t = int(input())

def calcAddedVotes(x):
  if x < maxVotes:
    addedVotes.append(maxVotes - x + 1)
  else:
    addedVotes.append(0)


for i in range(t):
  a, b, c = map(int, input().split())
  totalVotesArray = [a, b, c]
  totalVotes = a + b + c
  maxVotes = max(a, b, c)

  addedVotes = []

  if totalVotes == 0 or (a == b == c):
    print(1, 1, 1)
    continue

  for x in [a, b, c]:
    if len(set(totalVotesArray)) != len(totalVotesArray):
      # Get the duplicated item
      duplicated = set([x for x in totalVotesArray if totalVotesArray.count(x) > 1])
      duplicated = list(set(duplicated))[0]
    
    # If the current amount of votes is the duplicated one and the max value, add 1
    if duplicated == maxVotes and x == duplicated:
      addedVotes.append(1)
    else:
      calcAddedVotes(x)

  print(*addedVotes)