"""Bianary search. 

Target is 10

List is : 
2, 6, 7, 4, 10, 66, 3, 69, 100

I will need to sort the list, find the half by finding the Lowest point, upper point and middle point


"""

target = 15

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
  
  else:
    print("The data you're searching for is not in the list. Please check you're input is correct and try again.")