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
    real = MakeAnimal(win)

    open_button = Button(win, text="새로운 친구 만나기", command=lambda: real.aniset(win), width=10,height=2)
    open_button.grid(row=7 , column=0, columnspan=2)


    saver = SaveFile(app)
    win.mainloop()





