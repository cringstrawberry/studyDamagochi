#초안



from tkinter import *
from PIL import Image, ImageTk


win = Tk()
win.geometry("1000x1500")
win.title("오늘은 공부를 했나요?")
# win.option_add("*font", "")
bstart=Button(win)
bend=Button(win)
bstop=Button(win)
breplay=Button(win)

img = Image.open("/Users/ttalgi/Documents/study/교과목/수행평가/파이썬/GUItk/image/egg.png")

img = img.resize((200, 200))
photo = ImageTk.PhotoImage(img)

label = Label(win, image=photo, bd=0)
label.grid(row=0, column=0)
timer = Text(win, width=30, height=5)
timer.grid()

bstart.config(width = 20 , height = 3)
bend.config(width = 20 , height = 3)
bstop.config(width = 20 , height = 3)
breplay.config(width = 20 , height = 3)

bstart.config(text="공부시작")
bend.config(text="공부종료")
bstop.config(text="일시정지")
breplay.config(text="계속")

bstart.grid(row=1, column=0, padx=10, pady=10)
bend.grid(row=1, column=1, padx=10, pady=10)
bstop.grid(row=2, column=0, padx=10, pady=10)
breplay.grid(row=2, column=1, padx=10, pady=10)




win.mainloop()