from tkinter import *
from frame import StudyDamagochiFrame
from filesave import SaveFile


class MakeAnimal(StudyDamagochiFrame, SaveFile):
    def aniset(self, win):
        self.win = win
        win.title('나만의 펫 만들기')
        win.geometry ('600x600')
        win.resizable (False, False)
        # 문제 라벨 설정
        lab1 = Label(win)
        lab1 ['text']='동물 이름을 설정하세요.'
        lab1.pack()
        # 입력창 설정
        self.aniname=Entry(win)
        self.aniname.pack()
        
        lab2 = Label(win)
        lab2 ['text']='비밀번호를 설정하세요.'
        lab2.pack()
        # 입력창 설정
        self.password=Entry(win)
        self.password.pack()

        save_button = Button(win, text="만들기", command=self.생성)
        save_button.pack()

        login = Button(Text="동물이 있으신가요?", font=("BM Jua", 20), width=8, height=2)


        win.mainloop()





    def update_character(self):
        if self.로그인()==True:
            self.character.config(text=f"{self.aniname} lv. {self.levelup}({self.경험치값}%)")


# def aniset(self):
#         aniset = Toplevel(self.win)
#         aniset.title("나만의 펫 만들기")
#         aniset.geometry("600x600")
#         aniset.configure(background="white")


#     def 동물생성(self):
#         create_win=Tk()


#     def 동물이름짓기(self):
#         self.aniname=Entry(self.win)
#         self.aniname.pack()