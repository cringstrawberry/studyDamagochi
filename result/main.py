from tkinter import *
# from PIL import Image, ImageTk
from frame import StudyDamagochiFrame
from runbutton import RunButton
from makeanimal import MakeAnimal
from filesave import SaveFile

if __name__== "__main__":
    win=Tk()
    app = StudyDamagochiFrame(win)
    logic = RunButton(app)
    animal = MakeAnimal()
    win.mainloop()





