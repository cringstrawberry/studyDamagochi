
from tkinter import *
from filesave import SaveFile 
from PIL import Image, ImageTk
import os

try:
    from tkinter import messagebox
except ImportError:
    import tkMessageBox as messagebox



class MakeAnimal: 
    def __init__(self, main_win, study_damagochi_frame_instance): 
        self.main_win = main_win # 메인 Tk 윈도우 인스턴스

        self.study_damagochi_frame = study_damagochi_frame_instance 

        self.aniname_entry = None
        self.password_entry = None
        
        self.saver = SaveFile()
        self.aniset_open = False
        self.로그인_open = False
        self.계정삭제창_open = False

    def aniset(self, create_win):
        print(self.aniset_open, self.로그인_open, self.계정삭제창_open)
        if not self.aniset_open and not self.로그인_open and not self.계정삭제창_open:
            self.on_login_close()
            self.on_delate_close()
            self.anisetwin = Toplevel(create_win)
            self.anisetwin.title("나만의 펫 만들기")
            self.anisetwin.geometry("600x600")
            self.anisetwin.configure(bg="white")
            
            self.anisetwin.protocol("WM_DELETE_WINDOW", self.on_aniset_close)

            Label(self.anisetwin, text="동물 이름", bg='white',fg='black',font=('BM Jua', 20)).pack()
            self.aniname_entry = Entry(self.anisetwin) 
            self.aniname_entry.pack()

            Label(self.anisetwin, text="비밀번호", bg='white',fg='black',font=('BM Jua', 20)).pack()
            self.password_entry = Entry(self.anisetwin, show="*") 
            self.password_entry.pack()

            Button(
                self.anisetwin, text="만들기",
                command=self.create_character,
                bg='white', fg='black', font=('BM Jua', 20), width=11
            ).pack(pady=20)

            Button(
                self.anisetwin, text="동물이 있으신가요?",
                command=self.로그인,
                bg='white', fg='black', font=('BM Jua', 20)
            ).pack()

            self.aniset_open = True
        else:
            messagebox.showinfo("알림", "이미 다른 창이 열려 있어요!")
            self.on_aniset_close() #True일 때, 창닫기

    def on_aniset_close(self):
        self.aniset_open = False
        if hasattr(self, 'anisetwin') and self.anisetwin.winfo_exists(): # anisetwin이 존재하는지 확인
            self.anisetwin.destroy()


    def create_character(self):
        # Entry 위젯에서 값을 가져올 때는 .get() 메서드를 사용합니다.
        name = self.aniname_entry.get() 
        pw = self.password_entry.get()
        user = self.saver.특정불러오기(name)
        if name and pw: # 이름과 비밀번호가 모두 입력되었는지 확인
            if user is None:
                self.saver.tray(name, pw, level=1, exp=0)  # 파일 저장 (이름, 비밀번호, 레벨 1, 경험치 0)
                self.anisetwin.destroy() # 현재 Toplevel 창 닫기
                self.aniset_open = False
                # StudyDamagochiFrame의 메서드를 호출하여 메인 화면의 라벨을 업데이트
                self.study_damagochi_frame.update_character_display(name, 1, 0)
            else:
                messagebox.showerror("중복오류","이미 같은 이름의 동물 친구가 있어요.")
        else:
            # 사용자에게 입력 누락 메시지 표시 (필요시 라벨 사용)
            messagebox.showerror("입력오류","동물 친구의 이름과 비밀번호는 꼭 필요해요")


    def 로그인(self):  # 로그인 창 띄우기
        # 이전에 열린 Toplevel 창이 있다면 닫기
        if self.aniset_open and not self.로그인_open and not self.계정삭제창_open:
            self.on_aniset_close()
            self.on_delate_close()
            self.loginwin = Toplevel() # 새로운 Toplevel 창 생성
            self.loginwin.title("로그인")
            self.loginwin.geometry("600x600")
            self.loginwin.configure(bg="white")
            
            self.loginwin.protocol("WM_DELETE_WINDOW", self.on_login_close)

            Label(self.loginwin, text="동물 이름", bg='white',fg='black',font=('BM Jua', 20)).pack()
            self.aniname_entry = Entry(self.loginwin) # Entry 위젯 재할당
            self.aniname_entry.pack()

            Label(self.loginwin, text="비밀번호", bg='white',fg='black',font=('BM Jua', 20)).pack()
            self.password_entry = Entry(self.loginwin, show="*") # Entry 위젯 재할당
            self.password_entry.pack()

            Button(
                self.loginwin, text="로그인",
                command=self.로그인확인,
                bg='black', fg='white', font=('BM Jua', 20), width=11
            ).pack()

            self.로그인_open=True
        else:
            messagebox.showinfo("알림", "이미 다른 창이 열려 있어요!")
            self.로그인_open=False
            self.on_login_close()

    def on_login_close(self):
        self.로그인_open = False
        if hasattr(self, 'loginwin') and self.loginwin.winfo_exists():
            self.loginwin.destroy()


    def 로그인확인(self): # 파일에서 불러온 정보와 비교
        name = self.aniname_entry.get() # Entry 위젯에서 값 가져오기
        pw = self.password_entry.get() # Entry 위젯에서 값 가져오기
        user = self.saver.특정불러오기(name)  # 저장된 정보 불러오기

        if user and user["name"] == name and user["pw"] == pw:
            self.loginwin.destroy() # 현재 Toplevel 창 닫기
            self.로그인_open = False
            
            # 여기서 불러온 레벨과 경험치 값을 추출합니다.
            loaded_level = user.get("level", 1) # 'level' 키가 없으면 기본값 1
            loaded_exp = user.get("경험치", 0) # '경험치' 키가 없으면 기본값 0

            # 로그인 성공 시 StudyDamagochiFrame의 메서드를 호출하여 메인 화면의 라벨 업데이트
            # 이름, 레벨, 경험치를 모두 전달합니다.
            self.study_damagochi_frame.update_character_display(user["name"], loaded_level, loaded_exp) 
        else:
            # 로그인 실패 메시지 표시 (messagebox 사용 시 사용자에게 더 명확)
            messagebox.showerror("로그인오류","동물 친구의 이름과 비밀번호가 일치하지 않아요.")


    def 계정삭제창(self, delate_win):
        if not self.계정삭제창_open and not self.aniset_open and not self.로그인_open:
            self.on_aniset_close()
            self.on_login_close()
            self.계정삭제창_open = True
            self.delatewin = Toplevel(delate_win)
            self.delatewin.title('친구랑 헤어지기')
            self.delatewin.geometry('600x600')
            self.delatewin.configure(bg='white')

            img_path = "studyDamagochi/result/egg.jpg"

            if os.path.exists(img_path):
                img = Image.open(img_path)
                img = img.resize((200, 200))
                self.photo = ImageTk.PhotoImage(img)
            else:
                # 이미지가 없을 경우를 대비한 처리 (예: 빈 이미지 또는 에러 메시지)
                print(f"에러: 해당 파일 못찾겠음 {img_path}")
                self.photo = None # 또는 기본 제공되는 투명 이미지 등

            # 사용자 잡기
            dontgoaway=Label(self.delatewin, text="정말.. 떠나실 건가요?", bg='white',fg='black', font=('BM Jua',20))
            dontgoaway.grid(row=0,column=0,columnspan=2,padx=20)

            # 동물 그림 나타내기
            delateanimal = Label(self.delatewin, image=self.photo, bd=0, background="white")
            delateanimal.grid(row=1,column=0,columnspan=2,padx=20)

            Label(self.delatewin, text="동물 이름", bg="white", fg='black',font=('BM Jua',20)).grid(row=2,column=0,columnspan=2)
            self.delate_aniname_entry = Entry(self.delatewin)
            self.delate_aniname_entry.grid(row=3,column=0,columnspan=2)

            Label(self.delatewin, text="비밀번호", bg="white", fg='black',font=('BM Jua',20)).grid(row=4,column=0,columnspan=2)
            self.delate_password_entry = Entry(self.delatewin, show="*")
            self.delate_password_entry.grid(row=5,column=0,columnspan=2)

            Button(

                self.delatewin, 
                text="삭제하기",
                command=self.계정삭제,
                bg='red', fg='white', font=('BM Jua', 15)
            ).grid(row=6, column=0, columnspan=2, pady=20) 
        else:
            messagebox.showinfo("알림", "이미 다른 창이 열려 있어요!")
            self.on_delate_close()
            
    def on_delate_close(self):
        self.계정삭제창_open = False
        if hasattr(self, 'delatewin') and self.delatewin.winfo_exists():
            self.delatewin.destroy()

    def 계정삭제(self):
        name = self.delate_aniname_entry.get()
        pw = self.delate_password_entry.get()
        user = self.saver.특정불러오기(name)

        if user and user["name"] == name and user["pw"] == pw:
            level = user.get("level", 1)
            exp = user.get("경험치", 0)
            self.saver.삭제하기(name,level,exp)  # 저장된 파일 삭제 메서드가 있어야 함
            self.delatewin.destroy()
            self.계정삭제창_open = False
            messagebox.showinfo("동물 친구와 헤어지게 되었습니다. 그동안 고마웠어요.")
        else:
            messagebox.showerror("동물 친구의 이름과 비밀번호가 맞지 않아요.")
































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


#         self.로그인정보불러오기(self.aniname,self.password)
#         self.update_character(self.aniname,)










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