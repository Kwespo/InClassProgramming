order = []
name = ""
price = 0

def show_Options():
  print("\n")
  print("***************************************")
  print(" Burgor shop ")
  print("Options: \n 1 : Make an Order \n 2 : Print your recipt \n 3 : Exit")
  print("***************************************")

  option = input("Your choice: ")

  try:
    option = int(option)
    if option == 1:
      option = 0
      make_Order()

    elif option == 2:
      option = 0
      print_Receipt()
    
    elif option == 3:
      option = 0
      exit_Order()

  except:
    print("What is your action?")

def make_Order():
  global name, order, price
  """Making an order, takes name, what you're getting and if it has toppings or not"""
  if name == "":
    nameInp = input("Name? ")
    name = nameInp

  while True:
    orderInp = input("Please give *ONE* Order at a time, and if it has toppings or not.\n Your options are: Small, Medium, Large \n And for topics : Yes or No. \n To finish your order please finish with 'Finish : ")

    orderInp = orderInp.lower()
    orderInp = orderInp.split()

    if len(orderInp) > 2:
      print("Only input ONE order at a time using the valid options.")

    if orderInp[0] == "small":
      price += 4
      if orderInp[1] == "yes":
        price += 1.50
      elif orderInp[1] == "no": 
        pass
      else:
        "Please provide if you're having topings or not. Yes OR No"
      order.append([orderInp[0], orderInp[1]])
    
    elif orderInp[0] == "medium":
      price += 5
      if orderInp[1] == "yes":
        price += 1.50
      elif orderInp[1] == "no": 
        pass
      else:
        "Please provide if you're having topings or not. Yes OR No"
      order.append([orderInp[0], orderInp[1]])

    elif orderInp[0] == "large":
      price += 7
      if orderInp[1] == "yes":
        price += 1.50
      elif orderInp[1] == "no": 
        pass 
      else:
        "Please provide if you're having topings or not. Yes OR No"
      order.append([orderInp[0], orderInp[1]])
    
    elif orderInp[0] == "finish":
      break

    else: 
      print("Check your order again. Something went wrong")

    print(f"\n \n Added your order of: 1x {orderInp[0]} with topings: {orderInp[1]} \n You can keep ordering or finish by typing 'finish' \n \n")
  
  print("Order Finished...")


def print_Receipt():
  global name, order, price
  if len(order) < 1:
    print("Please provide an order before printing your receipt")

  print("Your order is:")
  print(f"Your name is {name}")
  print(f"Your order is {order}")
  print(f"Your price is: £{float(price)}")

def exit_Order():
  print("Goodbye...")


show_Options()
print_Receipt()