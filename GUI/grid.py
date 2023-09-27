import tkinter as tk

root = tk.Tk()

root.geometry("420x420")


#Var
StandardSize = 420
Canvas_Size = 400 # canvas size
Division = 10 #spacing between lines
Scale = StandardSize // Canvas_Size
Division_size = Canvas_Size // Division #making the spacing between lines
DataList = []

with open("Files\data.txt", "r") as f:
  Data = f.readlines()

  for line in Data:
    DataList.append(int(line.rstrip()))


#Make a canvas
Canvas = tk.Canvas(root, width=Canvas_Size, height=Canvas_Size, background = "Black")
Canvas.place(x = 10, y = 10)

#draw grid

for y in range(0, Canvas_Size, Division_size): # (start: 0, end = whatever Canvas_Size is, step (how much it increments): Whatever Division_Size is.)
  Canvas.create_line(0, y, Canvas_Size, y, fill = "white")
  GridLabel_Y = tk.Label(root, text = Canvas_Size - y)
  GridLabel_Y.place(x = 0, y = y + Division_size - 40)

for x in range(0, Canvas_Size, Division_size):
  Canvas.create_line(x, 0, x, Canvas_Size, fill = "white")
  GridLabel_X = tk.Label(root, text = x)
  GridLabel_X.place(y = 0, x = x + Division_size - 40)

x = 0
#plotting on grid
for i in range(0, 10):
  Canvas.create_line(x, (Canvas_Size - (DataList[i] // Scale)),x + Division_size, (Canvas_Size - (DataList[i + 1] // Scale)), fill = "Red", width = 6)
  x = x + Division_size

root.mainloop()