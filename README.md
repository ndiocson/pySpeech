# pySpeech

### Developed By:

- Nick Diocson
- Cole Milburn

## About

pySpeech is a text-to-speech program developed with Python. The program converts given text inserted by the user to audio outputted through the user's device. The user may choose to enter their own personalized message through the keyboard, or import pre-existing '.txt' files.

## How to Run

If you are missing the tkinter package, download it through:

'''
sudo apt-get install python3-tk
'''

To run the program, type:

'''
python3 main.py
'''

Running the program will result in a user interface widget to appear. From the generated widget you should see multiple text boxes as well as various buttons. Refer to the following guide for each button:

|Play|  -  plays all of the text entered
|Line|  -  plays the next line of text
|Word|  -  plays the next word
|Prev|  -  plays the last word/line/all said
|Clear| -  clears the display text box
|Exit|  -  closes the program

### Resources

To obtain the phoneme pronunciations for various words, we used a pre-existing dictionary provided by the Carnegie Mellon University (CMU) found here http://www.speech.cs.cmu.edu/cgi-bin/cmudict. 

This file has been imported into the project as a readable file labelled 'Words.txt', and contains the phoneme pronunciations for over 130,000 words.
