"""Creates the box for our executable"""

import os
import os.path
import easygui


p = './synthesizer.py'

path = os.path.relpath(p, start=os.curdir)

MSG = "Load application..."
TITLE="Text-to-Speech Audio ReImagination" # TSAR I
CHOICES = ["Create Audio File",".","Exit"]

easygui.ynbox(MSG, TITLE, ('Yes', 'No'))
easygui.msgbox('This is a basic message box.', TITLE)


# TODO: need titles for the execution in the GUI
# TODO: need command line for inputting text in GUI
# TODO: need __init__ file for the python directory to compile everything before the py too exe is run

def main():
    """runs the main application"""
    reply = easygui.buttonbox(MSG, TITLE, CHOICES)
    if reply == CHOICES[0]:
        return path
    if reply == "CHOICES[1]":
        num1 = os.startfile(f"{path}")
        return num1
    else:
        os.system("Exit")
        return

if __name__=='__main__':
    main()
