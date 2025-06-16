# makeanimal.py 파일 내용 (이 코드로 완전히 바꿔주세요!)

from tkinter import *
from filesave import SaveFile 
# StudyDamagochiFrame을 직접 상속받지 않습니다.
# from frame import StudyDamagochiFrame # 이 줄은 필요 없지만, 필요시 참조만 함

class MakeAnimal: # 더 이상 StudyDamagochiFrame을 상속받지 않습니다.
    # __init__ 메서드는 self 외에 두 개의 인자(main_win, study_damagochi_frame_instance)를 받아야 합니다.
    def __init__(self, main_win, study_damagochi_frame_instance): 
        self.main_win = main_win # 메인 Tk 윈도우 인스턴스
        # StudyDamagochiFrame 인스턴스를 저장하여 메인 프레임의 메서드를 호출할 수 있게 합니다.
        self.study_damagochi_frame = study_damagochi_frame_instance 

        self.aniname_entry = None # Entry 위젯을 참조할 변수 초기화 (나중에 할당됨)
        self.password_entry = None # Entry 위젯을 참조할 변수 초기화 (나중에 할당됨)
        
        self.saver = SaveFile()
        self.aniset_open = False
        self.로그인_open = False

    def aniset(self, create_win):
        if not self.aniset_open and not self.로그인_open:
            self.win = Toplevel(create_win)
            self.win.title("나만의 펫 만들기")
            self.win.geometry("600x600")
            self.win.configure(bg="white")

            Label(self.win, text="동물 이름").pack()
            # Entry 위젯을 self.aniname_entry에 할당하여 나중에 값을 가져올 수 있게 합니다.
            self.aniname_entry = Entry(self.win) 
            self.aniname_entry.pack()

            Label(self.win, text="비밀번호").pack()
            # Entry 위젯을 self.password_entry에 할당하여 나중에 값을 가져올 수 있게 합니다.
            self.password_entry = Entry(self.win, show="*") 
            self.password_entry.pack()

            Button(
                self.win, text="만들기",
                command=self.create_character
            ).pack(pady=10)

            Button(
                self.win, text="동물이 있으신가요?",
                command=self.로그인
            ).pack()

            self.aniset_open = True

    def create_character(self):
        # Entry 위젯에서 값을 가져올 때는 .get() 메서드를 사용합니다.
        name = self.aniname_entry.get() 
        pw = self.password_entry.get()   
        if name and pw: # 이름과 비밀번호가 모두 입력되었는지 확인
            self.saver.tray(name, pw, 1, 0)  # 파일 저장 (이름, 비밀번호, 레벨 1, 경험치 0)
            self.win.destroy() # 현재 Toplevel 창 닫기
            self.aniset_open = False
            # StudyDamagochiFrame의 메서드를 호출하여 메인 화면의 라벨을 업데이트
            self.study_damagochi_frame.update_character_display(name, 1, 0)
        else:
            # 사용자에게 입력 누락 메시지 표시 (필요시 라벨 사용)
            messagebox.showerror("입력 오류", "이름과 비밀번호를 모두 입력해주세요.")


    def 로그인(self):  # 로그인 창 띄우기
        # 이전에 열린 Toplevel 창이 있다면 닫기
        if hasattr(self, 'win') and self.win.winfo_exists():
            self.win.destroy()
        self.로그인_open = True

        self.win = Toplevel() # 새로운 Toplevel 창 생성
        self.win.title("로그인")
        self.win.geometry("600x600")
        self.win.configure(bg="white")

        Label(self.win, text="동물 이름").pack()
        self.aniname_entry = Entry(self.win) # Entry 위젯 재할당
        self.aniname_entry.pack()

        Label(self.win, text="비밀번호").pack()
        self.password_entry = Entry(self.win, show="*") # Entry 위젯 재할당
        self.password_entry.pack()

        Button(
            self.win, text="로그인",
            command=self.로그인확인
        ).pack()

    def 로그인확인(self): # 파일에서 불러온 정보와 비교
        name = self.aniname_entry.get() # Entry 위젯에서 값 가져오기
        pw = self.password_entry.get() # Entry 위젯에서 값 가져오기
        user = self.saver.불러오기()  # 저장된 정보 불러오기

        if user and user["name"] == name and user["pw"] == pw:
            self.win.destroy() # 현재 Toplevel 창 닫기
            self.로그인_open = False
            
            # 여기서 불러온 레벨과 경험치 값을 추출합니다.
            loaded_level = user.get("level", 1) # 'level' 키가 없으면 기본값 1
            loaded_exp = user.get("경험치", 0) # '경험치' 키가 없으면 기본값 0

            # 로그인 성공 시 StudyDamagochiFrame의 메서드를 호출하여 메인 화면의 라벨 업데이트
            # 이름, 레벨, 경험치를 모두 전달합니다.
            self.study_damagochi_frame.update_character_display(user["name"], loaded_level, loaded_exp) 
        else:
            # 로그인 실패 메시지 표시 (messagebox 사용 시 사용자에게 더 명확)
            messagebox.showerror("로그인 실패", "로그인 실패. 이름 또는 비밀번호를 확인해주세요.")

# messagebox를 사용하려면 tkinter 임포트 시 추가해야 합니다.
# from tkinter import * # <-- 이 부분에 messagebox 추가
try:
    from tkinter import messagebox
except ImportError:
    # Python 2.x 호환성을 위해 (거의 사용되지 않지만)
    import tkMessageBox as messagebox




























# from tkinter import *
# from frame import StudyDamagochiFrame
# from filesave import SaveFile  # 파일 저장 클래스

# class MakeAnimal(StudyDamagochiFrame):
#     def __init__(self, win):
#         # super().__init__(win)
#         self.aniname = None
#         self.password = None
#         self.character=Label(win,text="")
#         self.character.pack()
#         self.win = None
#         self.saver = SaveFile()
#         self.aniset_open=False
#         self.로그인_open=False
#         # self.aniset=False

#     def aniset(self, create_win):
#         #한번 누르면 창켜짐, 창 켜진데에서 한번 더 창누르면 창 삭제
#         if self.로그인_open == False and self.aniset_open == False: #창이 안켜져있을 때
            
#             self.win = Toplevel(create_win)  # 새 창 생성
#             self.win.title('나만의 펫 만들기')
#             self.win.geometry('600x600')
#             self.win.configure(bg="white")
#             self.win.resizable(False, False)
#             self.aniset_open=True

#             # 가운데 정렬 위한 열 비율 조정
#             self.win.grid_columnconfigure(0, weight=1)
#             self.win.grid_columnconfigure(1, weight=2)
#             self.win.grid_columnconfigure(2, weight=1)

#             # 동물 이름
#             lab1 = Label(self.win, text='동물 이름을 설정하세요.', bg="white", fg="black")
#             lab1.grid(row=0, column=1, pady=10)
#             self.aniname = Entry(self.win, bg="gray", width=30)
#             self.aniname.grid(row=1, column=1, pady=10)

#             # 비밀번호
#             lab2 = Label(self.win, text='비밀번호를 설정하세요.', bg="white", fg="black")
#             lab2.grid(row=2, column=1, pady=10)
#             self.password = Entry(self.win, show="*", bg="gray", width=30)
#             self.password.grid(row=3, column=1, pady=10)

#             # 저장 버튼
#             self.save_button = Button(
#                 self.win,
#                 text="만들기",
#                 command=lambda:self.create_character(self.aniname, self.password),
#                 width=20, height=2,
#                 font=("BM Jua", 20),
#                 fg="black"
#             )
#             self.save_button.grid(row=4, column=1, pady=20)

#             # 로그인 버튼
#             로그인할래용 = Button(
#                 self.win,
#                 text="동물이 있으신가요?",
#                 font=("BM Jua", 15),
#                 command=lambda: self.로그인(self.win)
#             )
#             로그인할래용.grid(row=5, column=1, pady=10)
#         else:
#             print('다른 창을 닫아주세요')
#             self.on_aniset_close() #True일 때, 창닫기

#         # 서브창(동물만들기) 닫기
#     def on_aniset_close(self):
#         self.aniset_open = False
#         self.win.destroy()

#         # 성장했을 경우 레벨업하기
#     def update_character(self,aniname,levelup,경험치값):
#         self.character.config(text=f"{aniname} lv. {levelup} ({경험치값}%)")


#         # 첫 생성할 때 파일 저장
#     # def first_character(self):
#     #     self.saver.생성(self.win)
#     #     name = self.aniname.get()
#     #     self.character.config(text=f"{name} lv. 1 (0%)")
#     def create_character(self, aniname, password):
#         self.win.destroy()
#         name = aniname.get()
#         pw = password.get()
#         self.saver.생성(self.win,name,pw,1,0)
#         self.character.config(text=f"{name} lv. 1 (0%)")
#         self.first_character()
        

#         # 로그인 서브창 열기
#     def 로그인(self, login_win):
#         login_win.destroy()  # 여기서 받은 창을 닫음
#         self.win = Toplevel()
#         self.win.title("로그인하기")
#         self.win.geometry("600x600")
#         self.win.resizable(False, False)
#         self.win.config(bg="white")

#         self.win.grid_columnconfigure(0, weight=1)
#         self.win.grid_columnconfigure(1, weight=2)
#         self.win.grid_columnconfigure(2, weight=1)

#         # 동물 이름
#         lab1 = Label(self.win, text='동물 이름을 입력하세요.', bg="white", fg="black")
#         lab1.grid(row=0, column=1, pady=10)
#         self.aniname = Entry(self.win, bg="gray", width=30)
#         self.aniname.grid(row=1, column=1, pady=10)

#         # 비밀번호
#         lab2 = Label(self.win, text='비밀번호를 입력하세요.', bg="white", fg="black")
#         lab2.grid(row=2, column=1, pady=10)
#         self.password = Entry(self.win, show="*", bg="gray", width=30)
#         self.password.grid(row=3, column=1, pady=10)


#         login = Button(
#             self.win,
#             text="로그인할래용",
#             font=("BM Jua", 15),

#             # command=self.update_character(self.aniname, )
#         )
#         login.grid(row=4, column=1, pady=10)


        # self.로그인정보불러오기(self.aniname,self.password)
        # self.update_character(self.aniname,)










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