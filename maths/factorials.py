"""
Find the factotorial of any inputted number
"""

inpNum = input("")

def factorial(n):
  total = n
  for i in range(1,inpNum):

    total = total * (n - i)

  return total

try:
  inpNum = int(inpNum)

  answer = factorial(inpNum)
except:
  print("The inputted data is not valid. Please only provide a NUMBER")


print(answer)