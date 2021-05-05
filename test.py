#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
import random

app = Tk() #application window

app['bg'] = '#B7B9B0'
app.geometry("150x200")
pin = "1111"
possiblePass = "" 
numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def updateLabel():
	label['text'] = possiblePass
	reshuffle()

def response(buttonPressed):
	global possiblePass
	#print(buttonPressed)
	possiblePass += buttonPressed
	updateLabel()
	if len(label['text']) > 3: #check if passcode is right when length is right
		#when length is equal to 4, doesn't update label. only leaves with 3 digits
		checkPin(possiblePass)
		possiblePass = ""

def checkPin(password):
	if pin == password:
		messagebox.showinfo("Passed", "Congratulations!")
	else:
		messagebox.showwarning("Didn't pass", "You fucked up")

def backspace():
	global possiblePass
	if len(possiblePass) > 0:
		possiblePass = possiblePass[:-1]
	updateLabel()

def reshuffle():
	random.shuffle(numList)
	upperLeft['text'] = numList[0]
	upperLeft['command'] = lambda m = numList[0]: response(m)
	upperMid['text'] = numList[1]
	upperMid['command'] = lambda m = numList[1]: response(m)
	upperRight['text'] = numList[2]
	upperRight['command'] = lambda m = numList[2]: response(m)
	midLeft['text'] = numList[3]
	midLeft['command'] = lambda m = numList[3]: response(m)
	midMid['text'] = numList[4]
	midMid['command'] = lambda m = numList[4]: response(m)
	midRight['text'] = numList[5]
	midRight['command'] = lambda m = numList[5]: response(m)
	lowerLeft['text'] = numList[6]
	lowerLeft['command'] = lambda m = numList[6]: response(m)
	lowerMid['text'] = numList[7]
	lowerMid['command'] = lambda m = numList[7]: response(m)
	lowerRight['text'] = numList[8]
	lowerRight['command'] = lambda m = numList[8]: response(m)
	bottomMid['text'] = numList[9]
	bottomMid['command'] = lambda m = numList[9]: response(m)	

label = Label(app, text = possiblePass, width = 13) #not sure how width is decided

exit_button = Button(app, text = "Quit", command = app.destroy)

random.shuffle(numList)
upperLeft = Button(app, text = numList[0], command = lambda m = numList[0]: response(m))
upperMid = Button(app, text = numList[1], command = lambda m = numList[1] : response(m))
upperRight = Button(app, text = numList[3], command = lambda m = numList[3] : response(m))
midLeft = Button(app, text = numList[4], command = lambda m = numList[4] : response(m))
midMid = Button(app, text = numList[5], command = lambda m = numList[5] : response(m))
midRight = Button(app, text = numList[6], command = lambda m = numList[6] : response(m))
lowerLeft = Button(app, text = numList[7], command = lambda m = numList[7] : response(m))
lowerMid = Button(app, text = numList[8], command = lambda m = numList[8] : response(m))
lowerRight = Button(app, text = numList[9], command = lambda m = numList[9]: response(m))
bottomMid = Button(app, text = numList[2], command = lambda m = numList[2] : response(m)) #i messed up


bottomLeft = Button(app, text = '<', command = backspace)

upperLeft.place(x = 10, y = 50)
upperMid.place(x = 60, y = 50)
upperRight.place(x = 110, y = 50)
midLeft.place(x = 10, y = 80)
midMid.place(x = 60, y = 80)
midRight.place(x = 110, y = 80)
lowerLeft.place(x = 10, y = 110)
lowerMid.place(x = 60, y = 110)
lowerRight.place(x = 110, y = 110)
bottomMid.place(x = 60, y = 140)
bottomLeft.place(x = 10, y = 140)

label.place(x = 10, y = 10)
exit_button.place(x = 100, y = 140)

app.mainloop()


def main():
	print("yay")

main()