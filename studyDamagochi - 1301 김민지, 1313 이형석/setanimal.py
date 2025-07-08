
from tkinter import *
from filesave import SaveFile 
from PIL import Image, ImageTk
import os
import sys

try:
    from tkinter import messagebox
except ImportError:
    import tkMessageBox as messagebox



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller로 패키징된 경우
    except Exception:
        base_path = os.path.abspath(".")  # 개발 중

    return os.path.join(base_path, relative_path)




class MakeAnimal: 
    def __init__(self, main_win, study_damagochi_frame_instance): 
        self.main_win = main_win # 메인 Tk 윈도우 인스턴스

        self.study_damagochi_frame = study_damagochi_frame_instance # 공부다마고치프레임 인스턴스 저장
        # self.run_button = run_button_instance #run button 인스턴스 저장

        self.aniname_entry = None
        self.password_entry = None
        
        self.saver = SaveFile()
        self.aniset_open = False
        self.로그인_open = False
        self.계정삭제창_open = False

    def aniset(self, create_win):
        if self.logic.starting:
            if messagebox.askokcancel("공부 종료 및 친구 만나기", '공부 종료하고 다른 친구를 만날까요?'):
                self.logic.공부종료()
            else:
                return
            
        self.on_aniset_close()
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
                self.saver.tray(name, pw, level=1, exp=0, big=200)  # 파일 저장 (이름, 비밀번호, 레벨 1, 경험치 0)
                self.anisetwin.destroy() # 현재 Toplevel 창 닫기
                self.aniset_open = False
                # StudyDamagochiFrame의 메서드를 호출하여 메인 화면의 라벨을 업데이트
                self.study_damagochi_frame.update_character_display(name, 1, 0)
            else:
                messagebox.showerror("중복 오류","이미 같은 이름의 동물 친구가 있어요. 다른 이름은 어떨까요?")
        else:
            # 사용자에게 입력 누락 메시지 표시 (필요시 라벨 사용)
            messagebox.showerror("입력 오류","동물 친구의 이름과 비밀번호는 꼭 필요해요")


    def 로그인(self):  # 로그인 창 띄우기
        # 이전에 열린 Toplevel 창이 있다면 닫기
        self.on_aniset_close()
        self.on_login_close()
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
            bg='white', fg='black', font=('BM Jua', 20), width=11
        ).pack()

        self.로그인_open=True

    def on_login_close(self):
        self.로그인_open = False
        if hasattr(self, 'loginwin') and self.loginwin.winfo_exists():
            self.loginwin.destroy()


    def 로그인확인(self): # 파일에서 불러온 정보와 비교
        name = self.aniname_entry.get() # Entry 위젯에서 값 가져오기
        pw = self.password_entry.get() # Entry 위젯에서 값 가져오기
        user = self.saver.특정불러오기(name)  # 저장된 정보 불러오기

        if name and pw:
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
                messagebox.showerror("로그인 오류","동물 친구의 이름과 비밀번호가 일치하지 않아요.")
        else:
            messagebox.showerror("입력 오류","동물 친구의 이름과 비밀번호는 꼭 필요해요")


    def 계정삭제창(self, delate_win):
        if self.logic.starting:
            if messagebox.askokcancel("공부 종료 및 친구헤어지기", "공부를 종료하고 친구와 헤어질까요?"):
                self.logic.공부종료()
            else:
                return  # 사용자가 '취소' 눌렀을 경우 창 열지 않음

        # 공부가 종료됐든 안 됐든 삭제창은 열기
        self.on_aniset_close()
        self.on_login_close()
        self.on_delate_close()
        self.계정삭제창_open = True

        self.delatewin = Toplevel(delate_win)
        self.delatewin.title('친구랑 헤어지기')
        self.delatewin.geometry('220x450')
        self.delatewin.configure(bg='white')


        img_path = resource_path("egg.jpg")  # 문자열 경로

        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((150, 150))
            self.photo = ImageTk.PhotoImage(img)
        else:
            messagebox.showerror("오류", f"이미지가 존재하지 않아요. {img_path}")
            self.photo = None


        Label(self.delatewin, text="정말.. 떠나실 건가요?", bg='white', fg='black', font=('BM Jua', 20)).grid(row=0, column=0, columnspan=2, padx=20)

        Label(self.delatewin, image=self.photo, bd=0, background="white").grid(row=1, column=0, columnspan=2)

        Label(self.delatewin, text="동물 이름", bg="white", fg='black', font=('BM Jua', 20)).grid(row=2, column=0, columnspan=2)
        self.delate_aniname_entry = Entry(self.delatewin)
        self.delate_aniname_entry.grid(row=3, column=0, columnspan=2)

        Label(self.delatewin, text="비밀번호", bg="white", fg='black', font=('BM Jua', 20)).grid(row=4, column=0, columnspan=2)
        self.delate_password_entry = Entry(self.delatewin, show="*")
        self.delate_password_entry.grid(row=5, column=0, columnspan=2)

        Button(
            self.delatewin,
            text="삭제하기",
            command=self.계정삭제,
            bg='white', fg='black', font=('BM Jua', 15)
        ).grid(row=6, column=0, columnspan=2, pady=20)

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
            삭제성공 = self.saver.삭제하기(name, level, exp)

            if 삭제성공:
                self.delatewin.destroy()
                self.계정삭제창_open = False
                messagebox.showinfo("알림", "동물 친구와 헤어지게 되었습니다. 그동안 고마웠어요.")
                self.study_damagochi_frame.update_character_display("삑삑이", 1, 0)  # 기본값으로 대치
                self.study_damagochi_frame.image_size = 150  # 이미지 크기 초기화
                self.study_damagochi_frame.update_animal_image()  # 실제 화면 반영

            else:
                messagebox.showerror("오류", "계정을 삭제하는 데 문제가 발생했어요.")
        else:
            messagebox.showerror("오류", "동물 친구의 이름과 비밀번호가 맞지 않아요.")