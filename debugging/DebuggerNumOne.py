Z = 0.2

while True:
  if round(Z, 2) == 0.6:
    print("All done!")
    break
  Z =  + 0.2


A = 1

B = 2

C = 3

print(f": {A} | B: {B} | C : {C} | are the INITIAL data")

for _ in range(1,6): #it starts at 0 so you gotta do +1
  A= (C + B)
  C = (A - B)
  B = (A + B + C)
  
  print(f": {A} | B: {B} | C: {C} | are the results")