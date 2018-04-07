from tkinter import *

root = Tk()


def printNote():
    notify = Label(right, text="the button has been pressed")
    notify.pack()


left = Frame(root)
left.pack(side=LEFT)

right = Frame(root)
right.pack(side=RIGHT)

prompt = Label(left, text="Enter a sentence")
play_button = Button(left, text="Play", command=printNote)
text = Entry(left)

prompt.grid(columnspan=2)
text.grid(row=1)
play_button.grid(row=1, column=1)

root.mainloop()
