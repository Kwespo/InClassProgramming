#Functions are a subroutine

def Add_X_Y(x:float, y:float) -> float| str:
  """
  Adding function taking TWO integer values.
  """
  try:
    x == int(x)
    y == int(y)
    return x + y
  except:
    return("The data you've given does not match the parameters of the function")

print(Add_X_Y(5,10))


def Subtract_X_Y(x:float, y:float) -> float| str:
  """
  Subtract function taking TWO integer values.
  """
  try:
    x == int(x)
    y == int(y)
    return x - y
  except:
    return("The data you've given does not match the parameters of the function")

print(Subtract_X_Y(5,10))



def Area_Circle(Radius:float) -> float:
  """
  pir^2 == area
  """

  pi = 3.14
  return pi * (Radius * Radius)

def Vol_Cuboid(Length:float, Width:float, Height:float) -> float | str:
  """
  Takes three numbers and returns the volume of the cuboid made by the inputted data
  """

  try:
    Length = float(Length)
    Width = float(Width)
    Height = float(Height)
    return Length * Width * Height
  except:
    return("You've done bad!")
  

print(Vol_Cuboid(10, 5, 10))


def Surf_Area_Cuboid(Length:float, Width:float, Height:float) -> float | str:
  """
  2(lb + bh + hl)
  """
  try:
    Length = float(Length)
    Width = float(Width)
    Height = float(Height)
    return(2* ((Length*Width) + (Width*Height) + (Height*Length)))
  except:
    return("You've done bad!")
  
print(round(Surf_Area_Cuboid(38, 6.5, 17.2), 2))