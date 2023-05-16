from tkinter import *


def my_click():
    my_label = Label(root, text="HEY YA!!")
    my_label.pack()

root = Tk()



# my_button = Button(root, text="Click it", state=DISABLED)
my_button = Button(root, text="Click it", padx=50, pady=10, command=my_click, fg="pink", bg="cyan", font="bold")
my_button.pack()

root.mainloop()
