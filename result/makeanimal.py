from tkinter import *
from frame import StudyDamagochiFrame
from filesave import SaveFile  # 파일 저장 클래스

class MakeAnimal(StudyDamagochiFrame):
    def __init__(self):
        self.aniname = None
        self.password = None
        self.saver = SaveFile(self)

    def aniset(self, parent_win):
        self.win = Toplevel(parent_win)  # 새 창 생성
        self.win.title('나만의 펫 만들기')
        self.win.geometry('600x600')
        self.win.configure(bg="white")
        self.win.resizable(False, False)

        # 동물 이름
        lab1 = Label(self.win, text='동물 이름을 설정하세요.', bg="white")
        lab1.pack(pady=10)
        self.aniname = Entry(self.win)
        self.aniname.pack()

        # 비밀번호
        lab2 = Label(self.win, text='비밀번호를 설정하세요.', bg="white")
        lab2.pack(pady=10)
        self.password = Entry(self.win, show="*")
        self.password.pack()

        # 저장 버튼
        save_button = Button(self.win, text="만들기", command=lambda: self.saver.생성(self.win))
        save_button.pack(pady=20)

        # 로그인 버튼
        login = Button(self.win, text="동물이 있으신가요?", font=("BM Jua", 15), width=25, height=2)
        login.pack(pady=10)

    def update_character(self):
        name = self.aniname.get()
        self.character.config(text=f"{name} lv. {self.levelup} ({self.경험치값}%)")




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