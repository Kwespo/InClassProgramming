# Learning about procedural programming and functions

# Pure . Deterministic. (Its pure and deterministic as it does not use global variables and all data is given to it )

#           Paramiters
def area(x : float, y : float) -> str | float:
  # Function Body
  areaAns = x * y
  return areaAns

  # INSIDE of tab: Function scope

#         Arguments
print(area(20, 60))# Calling the function


# Non Pure and determinisitc function

multiplyer = 2

def double(num):
  global multiplyer
  return num * multiplyer

print(double(10))