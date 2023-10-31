"""Bubble sorting"""

"""
Bubble sorting is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are larger then the following letter. For example:

6 5 7 9 8 

would be the list length -1 (that being 4, but it keeps going down till you reach 1)

you test if the number is smaller than the following number. If it is not then you swap the numbers. you do not compare the final number ad you'd be comparing against the void

it would look like this:

6 5 7 9 8 (4)

5 6 7 9 8 (3)

5 6 7 8 9 (2)

5 6 7 8 9 (1) (end)
"""

def sort(data):

  numberListCopy = data.copy()

  listLen = len(numberListCopy) 


  for i in range(0, listLen - 1):
    for j in range (0, listLen-i-1): #loop through the list, but not sorting numbers already set in place

      if numberListCopy [j] > numberListCopy [j+1]: #check the number then the following number

        numberListCopy [j], numberListCopy[j+1] = numberListCopy [j+1], numberListCopy[j] # swaps the numbers

        print(f"Sorting List : {numberListCopy}")

  return numberListCopy


unsortedList = [7,7,3,7,9,5,6,5,5,8,8,5]

sortedList = sort(unsortedList)

print(sortedList)