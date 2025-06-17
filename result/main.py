from tkinter import *
from frame import StudyDamagochiFrame
from runbutton import RunButton
from setanimal import MakeAnimal
from filesave import SaveFile
from tkinter import messagebox

if __name__== "__main__":
    win = Tk() # 창 생성

    saver = SaveFile() 

    all_animals = saver.목록불러오기()

    app = StudyDamagochiFrame(win, initial_animal_data=None) 

    logic = RunButton(app)

    make = MakeAnimal(win, app)



    if not all_animals:
        messagebox.showinfo("시작", "환영합니다! 처음이시군요.\n새로운 동물 친구를 만들어주세요.")
        all_animals.aniset(win)

    # 새로운 친구 만나기
    new_friend = Button(win, text="새로운 친구 만나기", command=lambda: make.aniset(win), width=15, height=2, font=('BM Jua', 15))
    new_friend.grid(row=7, column=0, columnspan=2, pady=10) # 버튼 위치와 스타일 조정

    # 떠나보내기
    delate_friend = Button(win, text="친구랑 헤어지기", command=lambda: make.계정삭제창(win), width=15, height=2, font=('BM Jua', 15))
    delate_friend.grid(row=8, column=0, columnspan=2)


    # new_friend = Button(win, text="새로운 친구 만나기", command=lambda: make.aniset(win), width=15, height=2, font=('BM Jua', 15))
    # new_friend.grid(row=7, column=0, columnspan=2, pady=10) # 버튼 위치와 스타일 조정

    win.mainloop()



# from tkinter import *
# # from PIL import Image, ImageTk
# from frame import StudyDamagochiFrame
# from runbutton import RunButton
# from makeanimal import MakeAnimal
# from filesave import SaveFile

# if __name__== "__main__":
#     win=Tk()
#     app = StudyDamagochiFrame(win)
#     logic = RunButton(app)
#     real = MakeAnimal(win)

#     open_button = Button(win, text="새로운 친구 만나기", command=lambda: real.aniset(win), width=10,height=2)
#     open_button.grid(row=7 , column=0, columnspan=2)


#     saver = SaveFile()
#     win.mainloop()