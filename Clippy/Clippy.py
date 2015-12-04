from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
import loadfonts
from PIL import Image, ImageTk
import pyHook, pythoncom
import pyautogui
import pyperclip



loadfonts.loadfont('')

class ASWindow:

    def __init__(self,root):
        self.root = root
        self.root.withdraw()
        self.root.overrideredirect(True)
        self.recent_value = ''
        self.auto_sel = True
        self.activ, self.drawn, self.selecting, self.first, self._seld = False, False, False, True, False
        self.root.bind('<Key>',self.key)
        self.dict = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',0:''}
        self._frame = Frame(self.root)
        self._del = ttk.Button(self._frame,command=self.delf,text='Delete'); self._del.grid()
        self.button = ttk.Button(self._frame,text='Auto',command=self._button); self.button.grid(column=1,row=0)
        self._frame.pack()

        self.lbf = Frame(self.root,height=100)
        self.listbox = Listbox(self.lbf,width=400,height=100)
        #self.listbox.bind('<Button-1>',self.destr)
        self.listbox.pack()
        self.lbf.pack()


        self._clupdate()
        for i in self.dict:
            t = str(i)+'. '+self.dict[i]
            self.listbox.insert(END,t)

    def click(self,evt):
        #return
        if not self.drawn:
            return
        #x1 < x < x2 and y1 < y < y2
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        x,y = evt.Position[0], evt.Position[1]

        if w/2-100 < x < w/2+100 and h/2-150 < y <h/2+150:
            return
        self.drawn, self.selecting = False, False

        self.root.withdraw()

    def delf(self):
        now = self.listbox.curselection()

    def event(self,event):
        if self.drawn and False:
            return
        if self.drawn:
            print('df')

        if event.Key == 'Space' and self.activ:
            self.activ = False
            self.activate()

        elif event.Key == 'Lcontrol':
            self.activ = True
            
            return True
            
        elif event.Key == 'Rmenu':
            self.activ = True
            
            

        else:
            
            self.activ = False

    def _button(self):
        self.auto_sel = not self.auto_sel
        if self.auto_sel: self.button['text'] = 'Auto'
        else: self.button['text'] = 'Manual'

    def destr(self,evt):
        self.drawn, self.selecting = False, False
        self.root.withdraw()

    def activate(self):
        print('asfa')
        self.drawn = True
        self.root.withdraw()
        self.root.deiconify()
        self.root.focus_force()
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        
        self.root.geometry("%dx%d+%d+%d" % (200,300,w/2-100,h/2-150))

    def key(self,evt):
        if not self.drawn:
            return
        char = evt.char
        if char in '1 2 3 4 5 6 7 8 9 0'.split(' '):
            if self.selecting:
                print('selecting because copied')
                print(self.recent_value)
                self.dict[int(char)] = self.recent_value
                
                self.drawn, self.selecting = False, False
                self.root.withdraw()
                self.listbox.delete(0,END)
                for i in self.dict:
                    t = str(i)+'. '+self.dict[i]
                    self.listbox.insert(END,t)
        
                return
            self.drawn, self.selecting = False, False
            self.root.withdraw()
            print(char)
            text = self.dict[int(char)]
            pyautogui.typewrite(text)
        elif evt.keysym == 'space':
            return
        else:
            print(char)
            print(evt.keysym)
            print('bye')
            self.root.withdraw()
            self.drawn, self.selecting = False,False
            return

    def _clupdate(self):
        self.tmp_value = pyperclip.paste()
        if self.tmp_value != self.recent_value:
            self.recent_value = self.tmp_value
            print('copied')
            if self.first:
                print('returning')
                self.root.after(500,self._clupdate)
                self.first = False; return
            if not self.auto_sel:
                self.selecting = True
                self.activate()
            else:
                for i in self.dict:
                    if self.dict[i] == '':
                        print('selfdict',i)
                        self.dict[int(i)] = self.recent_value
                        self.listbox.delete(0,END)
                        for i in self.dict:
                            t = str(i)+'. '+self.dict[i]
                            self.listbox.insert(END,t)
                        self.root.after(500,self._clupdate)
                        return
                self.dict[0] = self.recent_value
                self.listbox.delete(0,END)
                for i in self.dict:
                    t = str(i)+'. '+self.dict[i]
                    self.listbox.insert(END,t)
            
        self.root.after(500,self._clupdate)

       
        



root = Tk()
window = ASWindow(root)
# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = window.event
# set the hook
hm.HookKeyboard()
hm.SubscribeMouseAllButtonsDown(window.click)
hm.HookMouse()

mainloop()