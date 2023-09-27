import tkinter as tk

root = tk.Tk()

root.geometry("440x440")
root.config()

Canvas = tk.Canvas(root, width=400, height=400, background= "gray")
Canvas.place(x = 20, y = 20)

x = 250
y = 250
size = 60

BlackBox = Canvas.create_line(48,48,343,49,344,352,48,352,48,48, fill = "black", width= 5)


root.mainloop()