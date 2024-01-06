scores=input("Enter the list scores:").split()
for n in range (0,len(scores)):
    scores[n]=int(scores[n])
print(scores)
highest = 0
for big in scores:
  if highest > big:
      None
  else:
      highest = big
print(f"The Highest Score is :{highest}")
