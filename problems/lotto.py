import random

i = 0
while True:
  i +=1
  slots = random.randint(0, 100100100100100100)
  roll = random.randint(0, 100100100100100100)
  if roll == slots:
    print(roll, "---", slots)
    break
  
  print(f"Try number {i}")

