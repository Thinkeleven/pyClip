from __future__ import print_function
try:from tkinter import *
except ImportError:from Tkinter import *

try: from tkinter import ttk
except ImportError: import Tkinter as ttk
#import tkinter.font as tkfont
#import loadfonts
#from PIL import Image, ImageTk
import pyHook#, pythoncom, win32clipboard
import pyautogui
import pyperclip
import pickle


DEBUG = False


def dprint(*argv):
    if DEBUG:
        print(argv)

#loadfonts.loadfont('')

class ASWindow:

    def save(self):
        'Save everything via pickle'

        pickle.dump((self.dict,(self.activ,self.drawn,self.selecting,self.first,self._seld,self.auto_sel,self.count)),open('clip.clip','wb')) #Dump everything via pickle

    def update_listbox(self):
        'Updates the listbox in the window'

        #First delete everything in the listbox
        self.listbox.delete(0,END)

        #For everything in self.dict add it to the listbox
        for i in self.dict:
            t = str(i)+'. '+self.dict[i]
            self.listbox.insert(END,t)

        #Save everything!
        self.save()

    def __init__(self,root):
        'Initalise everything, and also create the widgets'
        #Determine basic things
        self.root = root
        #Withdraw window so it doesn't take up taskbar space OR be useless
        self.root.withdraw()
        #Remove title bar and frame of (withdrawn) window
        self.root.overrideredirect(True)
        #The following code is old and for testing/dev purposes:
            #self.root.wm_attributes("-disabled", True)
            #self.root.wm_attributes("-transparentcolor", "white")
            #self.root.bind('<Button-1>',self.click)
            ##If any comment has a purposeless indent, it is depreciated.
        self.recent_value = ''
        #Set a lot of variables
        self.activ, self.drawn, self.selecting, self.first, self._seld, self.auto_sel = False, False, False, True, False, True

        #Bind key to selection process (used to select things to paste)
        self.root.bind('<Key>',self.key)

        #Load self.dict from a pickle
        self.dict, temp = pickle.load( open( "clip.clip", "rb" ) )
            #self.activ, self.drawn, self.selecting, self.first, self._seld, self.auto_sel, self.count = temp
        self.count = temp[5]
        self.auto_sel = temp[4]

        #Draw all the widgets
        self._del = ttk.Button(self.root,
                               command=self.delf,
                               text='Delete')
        self._del.pack()
            #self._button = ttk.Button(self.root,text='Auto',command=self.button); self._button.pack()
        self._svar = IntVar()
        self._switch = Checkbutton(self.root,
                                   text='Manual Selection',
                                   command=self.button,
                                   variable=self._svar)
        self._switch.pack()
        self._clear = ttk.Button(self.root,
                                 text='Clear',
                                 command=self.clear)
        self._clear.pack()
        self.listbox = Listbox(self.root,
                               width=33,
                               height=10,
                               bg='white')
        self.listbox.pack()
            #self._frame.place(x=w/2-100,y=h/2-150)
            #self._frame.place(x=400,y=400)
            #if not self.auto_sel: self._button['text'] = 'Manual'
        #Update a few things
        self._clupdate()
        self.update_listbox()

    def button(self):
        'Event handler for changing of button/textbox'
        dprint(1)
        self.auto_sel = not self.auto_sel #Swap auto-selection variable around
        dprint(2)
            #if self.auto_sel: self._button['text'] = 'Auto'
            #else: self._button['text'] = 'Manual'
        dprint(3)
        self.save() #So self.auto_sel can be recorded


    def click(self,evt):
        'Close window if there is a click outside of the window'
            #return
        if not self.drawn:
            return
        #To jog my memory: x1 < x < x2 and y1 < y < y2
        try:
            #Try to see if click is out of window
            w = self.root.winfo_screenwidth()
            h = self.root.winfo_screenheight()
            x,y = evt.Position[0], evt.Position[1]
                #x,y = evt.x,evt.y
            dprint(x,y)
            #See if point is out of window
            if w/2-100 < x < w/2+100 and h/2-150 < y <h/2+150:
                return
            dprint('withdraw')
            #Withdraw window
            self.drawn, self.selecting = False, False

            self.root.withdraw()
        except:
            #Testing, don't even think about this
            dprint('problem')
            return

    def delf(self):
        'Delete certain elements'

        #Get current selection
        now = self.listbox.curselection()
        dprint(now)
        if not now:
            return
        lnum = now[0]
        self.dict[lnum] = ''
        self.update_listbox()
        self.listbox.selection_set(lnum+1)

    def clear(self):
        'Clear listbox'

        #Clear dict that stores everything
        self.dict = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',0:''}
        self.update_listbox()
        self.listbox.selection_set(lnum+1)

    def event(self,event):
        'Check for key events'
        if self.drawn and False:
            return
        if self.drawn:
            dprint('df')
        if event.Key == 'Space':
            dprint('space')
        if event.Key == 'Space' and self.activ:
            self.activ = False
            #self.root.after
            self.activate()
            return True

        elif event.Key == 'Lcontrol':
            self.activ = True
            dprint('lcontrol')
            #self.root.after(500,self.end)
            return True
            
        elif event.Key == 'Rmenu':
            self.activ = True
        else:
            self.activ = False
        return True

    def end(self):
        "I don't know what this does."

        #Finish stuff?
        self.activ = False


    

    def destr(self,evt):
        'Destroy main thing'

        #Set vars
        self.drawn, self.selecting = False, False
        #Withdraw window
        self.root.withdraw()

    def activate(self):
        'Open the window; called from EVENT when RALT and SPACE are pressed'
        dprint('asfa')
        self.drawn = True
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        return True

    def key(self,evt):
        'See if key press is used to select an element or to close window'
        if not self.drawn:
            return
        char = evt.char
        if char in '1 2 3 4 5 6 7 8 9 0'.split(' '):
            if self.selecting:
                dprint('selecting because copied')
                dprint(self.recent_value)
                self.dict[int(char)] = self.recent_value
                
                self.drawn, self.selecting = False, False
                self.root.withdraw()
                self.update_listbox()
        
                return
            self.drawn, self.selecting = False, False
            #Close window
            self.root.withdraw()
            dprint(char)
            text = self.dict[int(char)]
            #Type selected text
            pyautogui.typewrite(text)
        elif evt.keysym == 'space':
            return
        else:
            return
            dprint(char)
            dprint(evt.keysym)
            dprint('bye')
            self.root.withdraw()
            self.drawn, self.selecting = False,False
            return

    def _clupdate(self):
        'Every half minute, check for new clipboard things.'
        #self.tmp_value = pyperclip.paste()
        #self.tmp_value = self.root.clipboard_get()
        try:
            win32clipboard.OpenClipboard()
            self.tmp_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
        except:
            self.tmp_value = pyperclip.paste()
        if self.tmp_value != self.recent_value:

            self.recent_value = self.tmp_value
            dprint('copied')
            if self.first:
                dprint('returning')
                self.root.after(500,self._clupdate)
                self.first = False; return
            if not self.auto_sel:
                self.selecting = True
                self.activate()
            else:
                    #for i in self.dict:
                        #if self.dict[i] == '':
                            #dprint('chkpt')
                            #self.dict[int(i)] = self.recent_value
                            #self.update_listbox()
                            #self.root.after(500,self._clupdate)
                            #dprint('chkpt2')
                            #return
                self.count += 1
                if self.count >= 10:
                    self.count = 0
                    #self.dict[0] = self.recent_value
                self.dict[self.count - 1] = self.recent_value
                self.update_listbox()
            
        self.root.after(500,self._clupdate)

       
        


def start():      
    root = Tk()
    root.attributes("-topmost", True)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
        
    root.geometry("%dx%d+%d+%d" % (200,300,w/2-100,h/2-150))
    #root.geometry("%dx%d+0+0" % (w, h))
    window = ASWindow(root)
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyUp = window.event
    # set the hook

    hm.HookKeyboard()
    try:
        hm.SubscribeMouseAllButtonsDown(window.click)
        hm.HookMouse()
    except:
        hm.SubscribeMouseAllButtonsDown(window.click)
        hm.HookMouse()

    mainloop()

if __name__ == '__main__':
    start()