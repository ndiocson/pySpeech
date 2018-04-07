from tkinter import *
from graph import Graph
from word import Word
from audio import *
from word_methods import *

master = Tk()

master.geometry("700x500")
master.title("pySpeech")

L1 = Label(master, text="Enter Text Below: ")
L1.grid(row=1, column=0)

S = Scrollbar(master)
S2 = Scrollbar(master)
S.grid(row=2, column=1, sticky=NS)
S2.grid(row=0, column=1, sticky=NS)

entrytext = Text(master, width=95, height=10, bd=5)
entrytext.grid(row=2, column=0)

S.config(command=entrytext.yview)
entrytext.config(yscrollcommand=S.set)

entryfile = Entry(master, width=25, bd=5)
entryfile.place(x=70, y=465)

display = Text(master, width=95, height=19, bd=5)
display.grid(row=0, column=0)
display.configure(state=DISABLED)

S2.config(command=display.yview)
display.config(yscrollcommand=S2.set)

def play(text):
    '''
    Takes a list of words and plays audio
    '''
    files = convert(text)
    error = []
    for f in files:
        play_audio(str(f))

def client_enter():
    text = entrytext.get(1.0, END)[:-1]
    display.configure(state=NORMAL)
    display.delete(1.0, END)
    display.insert('1.0', text)
    display.configure(state=DISABLED)
    play(text.split())

def client_submit():
    text = entryfile.get()
    try:
        file_object = open(text, 'r')
        words = file_object.read()
    except FileNotFoundError:
        words = "File not found."

    display.configure(state=NORMAL)
    display.delete(1.0, END)
    display.insert('1.0', words)
    display.configure(state=DISABLED)
    # L2 = Label(master, text=words, wraplength=50)
    # for data in file_object:
    #     words = data.split()
    #     print(words)


enter = Button(master, text="Play", command=client_enter, bg="limegreen", activebackground="grey60")
enter.place(x=5, y=465)

submit = Button(master, text="Import", command=client_submit, bg="DodgerBlue2", activebackground="grey60")
submit.place(x=285, y=465)

mainloop()
