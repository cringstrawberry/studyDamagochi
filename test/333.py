from tkinter import *
from PIL import Image, ImageTk
import time

root = Tk()
root.title("tkinter_practice") #상단의 타이틀 지정
root.geometry("1000x1000") # 크기 설정 (1000x1000)
root.configure(bg="white")

img = Image.open("/Users/ttalgi/Documents/study/교과목/수행평가/파이썬/프로젝트 기획/GUItk/image/egg.png")
img = img.resize((200, 200))
photo = ImageTk.PhotoImage(img)

label = Label(root, image=photo, bd=0)
label.place(relx=0.5, rely=0.5, anchor='center')
timer = Text(root, width=30, height=5)
timer.pack()
# start_btn = Button(root, com)
root.mainloop()