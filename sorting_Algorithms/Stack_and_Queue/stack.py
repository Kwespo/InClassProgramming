class Stack():
  def __init__(self):
    self.stack = [] #Stack's variables

  def push(self, item : str):
    self.stack.append(item) # Adds a new thing to the stack

  def pop(self):
    if len(self.stack) == 0:
      raise Exception("Stack Is Empty. Cannot pop.")
    self.stack.pop() # removes the last item in the stack

  def peek(self) -> str | float:
    return self.stack[-1] # returns the last item in the stack
  
  def debugging(self):
    print(self.stack)
  

stackOfItems = Stack()

stackOfItems.push(5)
stackOfItems.push(6)
stackOfItems.push(7)
stackOfItems.push(8)

# 5,6,7,8

stackOfItems.pop()

# 5,6,7

stackOfItems.debugging()