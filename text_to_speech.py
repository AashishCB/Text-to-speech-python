import os
from tkinter import *
from gtts import gTTS #google text to speech
from playsound import playsound #module to play audio files

#Window Initialization
root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Text-To-Speech')

#Heading
Label(root, text = 'TEXT TO SPEECH', font = 'arial 20 bold', bg = 'white smoke').pack()

#other widgets
Label(root, text = 'Enter Your Text', font = 'arial 15 bold', bg = 'white smoke').place(x = 20, y = 60)
Msg = StringVar()
entry_field = Entry(root, textvariable = Msg, width = '50')
entry_field.place(x = 20, y = 100)

def Text_to_speech():
	Message = entry_field.get()
	speech = gTTS(text = Message)
	speech.save('audio_file.mp3')
	playsound('audio_file.mp3')
	os.remove('audio_file.mp3')

def Exit():
	root.destroy()

def Reset():
	Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)

root.mainloop()
