"""Bianary search. 

Target is 10

List is : 
2, 6, 7, 4, 10, 66, 3, 69, 100

I will need to sort the list, find the half by finding the Lowest point, upper point and middle point


"""

target = 10

listOfNumbers = [2, 6, 7, 4, 10, 66, 3, 69, 100]

listOfNumbers = sorted(listOfNumbers)

middle = None
lowest = 0
upper = len(listOfNumbers) - 1


while True:
  middle = (lowest + upper) // 2

  if listOfNumbers[middle] > target:
    upper = middle - 1

  elif listOfNumbers[middle] < target:
    lowest = middle + 1

  elif listOfNumbers[middle] == target:
    print(f"Found it! it is {middle}")
    break
