def Area(Length: float, Width: float,) -> float | str:
  try:
    Length = float(Length)
    Width = float(Width)
    return abs(round(Length * Width, 3))
  except:
    return "Cannot convert given values into a 'float'"


