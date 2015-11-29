from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
import loadfonts
from PIL import Image, ImageTk

loadfonts.loadfont('')

class ASWindow:

    def __init__(self,root):
        self.root = root
        self.root.bind('<Key>',self.event)
        

    def event(self,evt):
        keypresses = evt.keysym
        print(keypresses)
        print('***')





root = Tk()
launcherIcon = ImageTk.PhotoImage(Image.open('dat_1.jpg'))
button = ttk.Button(root,image=launcherIcon)
button.pack()
window = ASWindow(root)

mainloop()