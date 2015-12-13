# pyClip
An extended clipboard for Windows, pyClip puts you in control of 10 'extended' slots, that you can use!

Along with that, pyClip lets you use your clipboard like normal. For power users, pyClip's 'Manual' function lets you custom select your slot, but 'Auto' mode lets you use your clipboard like normal (but with the extended features).

To start pyClip, install Python 3, and then run:

- `pip install pillow`
- `pip install pyperclip`

Along with that, head to [Christoph Gohlke's Python Extension Modules page](http://www.lfd.uci.edu/~gohlke/pythonlibs/) and find pyHook. Download the version that has your Python version on it AND Python version (x86, x64). Then navigate to the folder you downloaded the file via `cmd` using the `cd` command, and then type:

`pip install pyHook-1.5.1-cp35-none` and press TAB to auto-complete the file (should end with `.whl`)

And finally, run Start_pyClip.py with pythonw.

Once it's running, copy like you normally do and paste like you normally do. But note that when you tap R_ALT first and then SPACE afterwards, a box appears. This box has your recent copies. You can use the number keys to select one, and it will paste into the text box. Try it out! Copy this text into Notepad, and then copy some extra text, and then tap R_ALT + SPACE!

The Manual checkbox can toggle between Manual mode and Auto mode. In Manual, when you copy something, the box pops up and you have to select a slot with the number keys.

The Clear button and Delete button can help you clear things. Clear clears all the slots, but Delete only gets rid of the selected slot.
