import subprocess
import traceback
import sys
import pickle

if sys.platform.startswith("win"):
    # Don't display the Windows GPF dialog if the invoked program dies.
    # See comp.os.ms-windows.programmer.win32
    #  How to suppress crash notification dialog?, Jan 14,2004 -
    #     Raymond Chen's response [1]

    import ctypes
    SEM_NOGPFAULTERRORBOX = 0x0002 # From MSDN
    ctypes.windll.kernel32.SetErrorMode(SEM_NOGPFAULTERRORBOX);
    CREATE_NO_WINDOW = 0x08000000    # From Windows API
    subprocess_flags = CREATE_NO_WINDOW
else:
    subprocess_flags = 0

dict = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',0:''}
pickle.dump((dict,(False, False, False, True, True, True, 0)), open( "clip.clip", "wb" ) )

while True:
    subprocess.call('"c:\python(86)34\python.exe" pyClip.py')
    print('something happened, redoing stuff')


print('done')