from tkinter import *
from frame import StudyDamagochiFrame
from filesave import SaveFile  # 파일 저장 클래스

class MakeAnimal(StudyDamagochiFrame):
    def __init__(self, win):
        # super().__init__(win)
        self.aniname = None
        self.password = None
        self.win = None
        self.saver = SaveFile(self)
        # self.aniset=False

    def aniset(self, create_win):
        self.aniset=True
        self.win = Toplevel(create_win)  # 새 창 생성
        self.win.title('나만의 펫 만들기')
        self.win.geometry('600x600')
        self.win.configure(bg="white")
        self.win.resizable(False, False)

        # 가운데 정렬 위한 열 비율 조정
        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_columnconfigure(1, weight=2)
        self.win.grid_columnconfigure(2, weight=1)

        # 동물 이름
        lab1 = Label(self.win, text='동물 이름을 설정하세요.', bg="white", fg="black")
        lab1.grid(row=0, column=1, pady=10)
        self.aniname = Entry(self.win, bg="gray", width=30)
        self.aniname.grid(row=1, column=1, pady=10)

        # 비밀번호
        lab2 = Label(self.win, text='비밀번호를 설정하세요.', bg="white", fg="black")
        lab2.grid(row=2, column=1, pady=10)
        self.password = Entry(self.win, show="*", bg="gray", width=30)
        self.password.grid(row=3, column=1, pady=10)

        # 저장 버튼
        self.save_button = Button(
            self.win,
            text="만들기",
            command=self.create_character,
            width=20, height=2,
            font=("BM Jua", 20),
            fg="black"
        )
        self.save_button.grid(row=4, column=1, pady=20)

        # 로그인 버튼
        로그인할래용 = Button(
            self.win,
            text="동물이 있으신가요?",
            font=("BM Jua", 15),
            command=lambda: self.로그인(self.win)
        )
        로그인할래용.grid(row=5, column=1, pady=10)

    def update_character(self,aniname,levelup,경험치값):
        self.character.config(text=f"{aniname} lv. {levelup} ({경험치값}%)")

    def first_character(self):
        self.saver.생성(self.win)
        name = self.aniname.get()
        self.character.config(text=f"{name} lv. 1 (0%)")

    def create_character(self):
        self.win.destroy()
        name = self.aniname_entry.get()
        pw = self.password_entry.get()
        self.saver.생성(self.win,name,pw,1,0)
        self.character.config(text=f"{name} lv. 1 (0%)")
        self.first_character()
        

    def 로그인(self, login_win):
        login_win.destroy()  # 여기서 받은 창을 닫음
        self.win = Toplevel()
        self.win.title("로그인하기")
        self.win.geometry("600x600")
        self.win.resizable(False, False)
        self.win.config(bg="white")

        # 동물 이름
        lab1 = Label(self.win, text='동물 이름을 입력하세요.', bg="white", fg="black")
        lab1.grid(row=0, column=1, pady=10)
        self.aniname = Entry(self.win, bg="gray", width=30)
        self.aniname.grid(row=1, column=1, pady=10)

        # 비밀번호
        lab2 = Label(self.win, text='비밀번호를 입력하세요.', bg="white", fg="black")
        lab2.grid(row=2, column=1, pady=10)
        self.password = Entry(self.win, show="*", bg="gray", width=30)
        self.password.grid(row=3, column=1, pady=10)

        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_columnconfigure(1, weight=2)
        self.win.grid_columnconfigure(2, weight=1)

        self.로그인정보불러오기(self.aniname,self.password)
        self.update_character(self.aniname, )

        login = Button(
            self.win,
            text="로그인할래용",
            font=("BM Jua", 15),
            command=self.update_character()
        )
        login.grid(row=3, column=1, pady=10)








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