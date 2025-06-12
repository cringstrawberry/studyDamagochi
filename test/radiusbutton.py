from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.geometry("300x300")

# 둥근 버튼 배경 이미지 (png로 배경이 투명한 이미지여야 함)
img = Image.open("rounded_button.png")
img = img.resize((150, 50))
photo = ImageTk.PhotoImage(img)

def on_click():
    print("눌림!")

button = Button(win, image=photo, command=on_click, borderwidth=0)
button.pack(pady=20)

win.mainloop()
