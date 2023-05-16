from tkinter import *


def my_click():
    my_label = Label(root, text=e.get())
    my_label.pack()


root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")


# my_button = Button(root, text="Click it", state=DISABLED)
my_button = Button(root, text="Enter your name", padx=50, pady=10, command=my_click, fg="pink", bg="cyan", font="bold")
my_button.pack()

root.mainloop()
