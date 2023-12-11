dayValueList = []
smallestValue = 0

for d in range(0, 7): # D = Days
  value = input(f"Day {d+1}: ")
  dayValueList.append(value)

  if d == 1: # List starts at 0 so 2 is 1
    if dayValueList[0] > dayValueList[1]:
      smallestValue = dayValueList[1]
    else:
      smallestValue = dayValueList[0]

for i in dayValueList:
  if i < smallestValue:
    smallestValue = i
  else:
    pass


print("smallest value is", smallestValue)


raise Exception