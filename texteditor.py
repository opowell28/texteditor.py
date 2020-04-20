import sys
from Tkinter import *
import tkFileDialog

root=Tk("Text Editor")

text=Text(root)
text.grid()

def saveas():
    global text

    t = text.get("1.0", "end-1c")
    saveLocation=tkFileDialog.asksaveasfilename()
    file1=open(saveLocation, "w+")
    file1.write(t)
    file1.close()

button=Button(root, text="Save", command=saveas)
button.grid()

root.mainloop()