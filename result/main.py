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
    app = MakeAnimal()

    open_button = Button(win, text="새로운 친구 만나기", command=lambda: app.aniset(win), width=13,height=3)
    open_button.grid()


    saver = SaveFile(app)
    win.mainloop()





