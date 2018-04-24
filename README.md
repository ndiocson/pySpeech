# pySpeech

#### Developed By:
- Nick Diocson
- Cole Milburn

## About
pySpeech is a text-to-speech program developed with Python. The program converts given text inserted by the user to audio outputted through 
the user's device. The user may choose to enter their own personalized message through the keyboard, or import pre-existing .txt files.

Running this program is very simple. Start by making sure that the current VM being used has the tkinter package installed.
If this file is missing, refer to the Downloading Packages portion of this README. Next you can start the program by typing
'python3 main.py' into the command line. This will result in a user interface widget to appear. From the generated widget you
should see multiple text boxes as well as various buttons. The first text box is used for a display. The user cannot modify this
text as it is only used to display what words have already been converted to speech. The following text box is used for entering data.
Here the user can type any text that they wish to have converted to speech. After entering the desired text, the user must press submit
to save the data to the program. An alternative option to this text box is the import box. Here the user can type the file path to a
specific document that they wish to convert to speech. Pressing import will save all data in the given file to our program. Now that the
data has been saved, the user has various options of how to convert the text to speech. Refer to the following guide on each button:

|Play|  -  plays all of the text entered
|Line|  -  plays the next line of text
|Word|  -  plays the next word
|Prev|  -  plays the last word/line/all said
|Clear| -  clears the display text box
|Exit|  -  closes the program

## Resources
To obtain the phoneme pronunciations for various words, we used a pre-existing dictionary provided by the Carnegie Mellon University (CMU) found here http://www.speech.cs.cmu.edu/cgi-bin/cmudict. This file has been imported into the project as a simple readable file labelled 'Words.txt', and contains the phoneme pronunciations for over 300,000 words.

## Downloading Packages

If you are missing the tkinter package, you must type the following code into the terminal;

sudo apt-get install python3-tk

This will install tkinter and allow you to use it for our text to speech program.
