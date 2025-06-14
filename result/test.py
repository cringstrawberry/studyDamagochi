from tkinter import *

def 저장():
    with open("animal_name.txt", "w", encoding="utf-8") as f:
        f.write(animalname.get())

win = Tk()
win.title("동물 이름 저장")
win.geometry("300x150")

animalname = Entry(win)
animalname.pack(pady=10)
animalname.insert(0, "동물이름")

save_button = Button(win, text="저장하기", command=저장)
save_button.pack()

win.mainloop()
