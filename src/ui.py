from tkinter import *
from sound import Sound
from time import sleep
import word as w
import tkinter.messagebox

# initalize a widget class
class GUI:
    def __init__(self, master):
        # assign a title and size to the created widget
        self.master = master
        master.geometry("700x500")
        master.title("pySpeech")

        # generate and place a label for entering text
        self.label_1 = Label(master, text="Enter Text Below: ")
        self.label_1.grid(row=1, column=0)

        # create and place a scollbar for each box created
        self.scroll_1 = Scrollbar(master)
        self.scroll_2 = Scrollbar(master)
        self.scroll_1.grid(row=2, column=1, sticky=NS)
        self.scroll_2.grid(row=0, column=1, sticky=NS)

        # create and place a textbox for entering desired text to the program
        self.text_entry = Text(master, width=95, height=10, bd=5, bg="white")
        self.text_entry.grid(row=2, column=0)

        # link the first scroll bar to the entry textbox
        self.scroll_1.config(command=self.text_entry.yview)
        self.text_entry.config(yscrollcommand=self.scroll_1.set)

        # create and place an entry box to enter filenames to the program
        self.file_entry = Entry(master, width=15, bd=5)
        self.file_entry.place(x=80, y=465)

        # create and place another textbox for displaying spoken text
        self.display = Text(master, width=95, height=19, bd=5, bg="white")
        self.display.grid(row=0, column=0)
        # prevent the display from being edited
        self.display.configure(state=DISABLED)

        # link the second scroll bar to the display textbox
        self.scroll_2.config(command=self.display.yview)
        self.display.config(yscrollcommand=self.scroll_2.set)

        # create and place a button for submitting entered text, calls client_enter function
        self.enter = Button(master, text="Submit", command=self.client_enter, bg="DodgerBlue2", activebackground="grey70")
        self.enter.place(x=5, y=465)

        # create and place a button for impoprting an entered filename, calls client_submit function
        self.submit = Button(master, text="Import", command=self.client_submit, bg="limegreen", activebackground="grey70")
        self.submit.place(x=215, y=465)

        # create and place a button for converting all entered text to speech, calls client_all function
        self.entire = Button(master, text="Play", command=self.client_all, bg="DarkOrange2", activebackground="grey70")
        self.entire.place(x=285, y=465)

        # create and place a button for converting the next line of text to speech, calls client_line function
        self.line = Button(master, text="Line", command=self.client_line, bg="OrangeRed2", activebackground="grey70")
        self.line.place(x=338, y=465)

        # create and place a button for converting the next word of text to speech, calls client_word function
        self.word = Button(master, text="Word", command=self.client_word, bg="red", activebackground="grey70")
        self.word.place(x=392, y=465)

        # create and place a button for replaying the previously spoken text, calls client_prev function
        self.prev = Button(master, text="Prev", command=self.client_prev, bg="medium purple", activebackground="grey70")
        self.prev.place(x=453, y=465)

        # create and place a button for clearing the displayed text, calls clear function
        self.clear = Button(master, text="Clear", command=self.clear, bg="gold3", activebackground="grey70")
        self.clear.place(x=508, y=465)

        # create and place a button for exiting the widget by quitting the widget
        self.exit = Button(master, text="Exit", command=master.quit, bg="grey40", activebackground="grey70")
        self.exit.place(x=640, y=465)

        # initalize variables used amongst the following functions
        self.data = ""
        self.prev = ""
        self.ind = 0

        # create a graph from the given text file
        phoneme_graph = w.create_phoneme_graph("text/Symbols.txt")
        self.graph = w.create_word_graph("text/Words.txt", phoneme_graph)

    # this functions takes given data and displays it to the display textbox
    def editor(self, data):
        if self.ind == 0:
            self.display.configure(state=NORMAL)
            self.display.insert(INSERT, data)
            self.display.configure(state=DISABLED)

    # create a messagebox to indicate a warning while running the program
    def popup(self, bad, sim):
        # will display what word was not found and what word was used to replace it
        tkinter.messagebox.showwarning("NOTICE", "The word '{}' was not found in the database. '{}' will be spoken in its place.".format(bad, sim))

    # generates audio for the provided data by linking sounds with corresponding phonemes
    def play_sentence(self, pronounce):
        for phoneme in pronounce:
            for sound in phoneme:
                sound_instance = Sound(sound)
                sound_instance.play()
            sleep(0.08)

    # maps the provided data with its phonemes
    def map_audio(self, data):
        words = data.split()
        pronounce = []

        # for each word, find its phonemes using the get_pronounce() method
        # and append them as a list to the pronounce list
        for word in words:
            phonemes = w.get_pronounce(word, self.graph)

            # if the word was not found in the database, find a similar word
            if phonemes is None:
                sim = w.get_similar(word, self.graph)
                phonemes = w.get_pronounce(sim, self.graph)

                # notify the user that a given word could not be found
                self.popup(word, sim)
            pronounce.append(phonemes)

        self.play_sentence(pronounce)

    # delete all text that has been inserted into the display textbox
    def clear(self):
        self.display.configure(state=NORMAL)
        self.display.delete(1.0, END)
        self.display.configure(state=DISABLED)

    # this function is used to play the next word in the data file
    def client_word(self):
        try:
            # split the data into lines and words
            self.lines = self.data.split("\n")
            self.words = self.lines[0].split(" ")
            self.length = len(self.words[0]) + 1
            # if there is only one word left in the given line...
            if len(self.words) == 1 and self.words[0] != "":
                # display the word followed by a line feed
                self.ind = 0
                self.editor(self.words[0] + "\n")
                # convert the displayed text to speech
                self.map_audio(self.words[0])
                # save this word as the last word spoken
                self.prev = self.words[0]
                # cut the spoken text out of the data file
                self.data = self.data[self.length:]
            # if there is stll data left to be converted...
            elif self.data != "":
                # display the word followed by a space
                self.ind = 0
                self.editor(self.words[0] + " ")
                # convert the displayed text to speech
                self.map_audio(self.words[0])
                # save this word as the last word spoken
                self.prev = self.words[0]
                # cut the spoken text out of the data file
                self.data = self.data[self.length:]
            # notify the user that no more text is left to be converted
            else:
                self.editor("\n**End of Text**\n")
                self.ind = 1
        # return an error message if no data was received from the user
        except NameError:
            self.ind = 0
            self.editor("\n**Error: No Data Received**\n")

    # this function is used to play the next line in the data file
    def client_line(self):
        try:
            # split the data file into lines
            self.lines = self.data.split("\n")
            self.length = len(self.lines[0]) + 1
            # if there is stll data left to be converted...
            if self.data != "":
                # display the line followed by a line feed
                self.ind = 0
                self.editor(self.lines[0] + "\n")
                # convert the displayed text to speech
                self.map_audio(self.lines[0])
                # save this line as the last line spoken
                self.prev = self.lines[0]
                # cut the spoken text out of the data file
                self.data = self.data[self.length:]
            # notify the user that no more text is left to be converted
            else:
                self.editor("\n**End of Text**\n")
                self.ind = 1
        # return an error message if no data was received from the user
        except NameError:
            self.ind = 0
            self.editor("\n**Error: No Data Received**\n")

    # this function is used to play all of the text in the data file
    def client_all(self):
        try:
            # if there is stll data left to be converted..
            if self.data != "":
                # display all of the text
                self.ind = 0
                self.editor(self.data)
                # convert the displayed text to speech
                self.map_audio(self.data)
                # save this text as the last text spoken
                self.prev = self.data
                # cut the spoken text out of the data file
                self.data = ""
            # notify the user that no more text is left to be converted
            else:
                self.editor("\n**End of Text**\n")
                self.ind = 1
        # return an error message if no data was received from the user
        except NameError:
            self.ind = 0
            self.editor("\n**Error: No Data Received**\n")

    # replay the previously spoken text
    def client_prev(self):
        self.map_audio(self.prev)

    # get the text entered by the user and save it to data
    def client_enter(self):
        # notify the user if no text was entered
        if self.text_entry.get(1.0, END)[:-1] + "\n" == "\n":
            self.ind = 0
            self.editor("\n**Error: No Data Received**\n")
        # otherwise save all entered text
        else:
            self.data = self.text_entry.get(1.0, END)[:-1] + "\n"

    # get the text entered by the user to retrieve the text file
    def client_submit(self):
        try:
            # get the file name, open it and save all text to data
            self.text = self.file_entry.get()
            self.file_object = open(self.text, 'r')
            self.data = self.file_object.read()
        # notify the user if the filename entered does not exist
        except FileNotFoundError:
            self.ind = 0
            self.editor("\n**Error: File Not Found**\n")
