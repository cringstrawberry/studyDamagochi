from tkinter import *
from datetime import datetime

def what_time():
    dnow = datetime.now()
    btn.config(text=dnow)


win = Tk()
win.geometry("500x500")
win.title("what time?")
win.option_add("*font", "궁서 20")

btn = Button(win) # 버튼 생성
btn.config(width = 20, height= 10)
btn.config(text = "현재 시각")
btn.config(command = what_time) #


btn.pack()

win.mainloop()

datetime