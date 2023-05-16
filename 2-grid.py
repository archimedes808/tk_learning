from tkinter import *

root = Tk()

my_label1 = Label(root, text="Hellurrrr, world!")
my_label2 = Label(root, text="The real slim shady!")
Label(root, text=" ").grid(row=1, column=1)
Label(root, text=" ").grid(row=2, column=2)
Label(root, text=" ").grid(row=3, column=3)
Label(root, text=" ").grid(row=4, column=4)
my_label1.grid(row=0, column=0)
my_label2.grid(row=10, column=5)


root.mainloop()
