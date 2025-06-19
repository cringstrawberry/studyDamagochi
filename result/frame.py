# 메인 페이지 틀

from tkinter import *
from PIL import Image, ImageTk
import os

try:
    from tkinter import messagebox
except ImportError:
    import tkMessageBox as messagebox

class StudyDamagochiFrame():
    # initial_animal_data 매개변수가 반드시 여기에 포함되어야 합니다.
    def __init__(self, win, initial_animal_data=None): 
        self.win = win
        
        def confirm_exit():
            if messagebox.askokcancel("종료 확인", "정말 종료하시겠어요?"):
                win.destroy()
        # 창 생성 및 설정
        win.geometry("770x880")
        win.title("오늘은 공부를 했나요?")
        win.configure(background="white")
        
        # 메세지 나타내기, 설정
        self.message = Label(width=30, height=1, text='오늘은 공부를 했나요?', font=('BM Jua',40), background='white', foreground='black')
        self.message.grid(row=0, column=0, columnspan=2, pady=20)

        # 레벨, 경험치, 공부시간 설정
        # initial_animal_data에서 값을 가져오거나 기본값 사용
        if initial_animal_data:
            self.levelup = initial_animal_data.get("level", 1)
            self.경험치값 = initial_animal_data.get("경험치", 0)
            self.animal_name = initial_animal_data.get("name", "삑삑이")
        else:
            self.levelup = 1
            self.경험치값 = 0
            self.animal_name = "삑삑이" # 데이터가 없을 경우 기본값

        self.studytime = 0 # 공부시간

        # 동물 그림 설정
        img_path = "result/egg.jpg"
        # 파일이 존재하는지 확인하는 것이 좋습니다.
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((200, 200))
            self.photo = ImageTk.PhotoImage(img)
        else:
            # 이미지가 없을 경우를 대비한 처리 (예: 빈 이미지 또는 에러 메시지)
            print(f"에러: 해당 파일 못찾겠음 {img_path}")
            self.photo = None # 또는 기본 제공되는 투명 이미지 등

        # 동물 그림 나타내기
        self.label = Label(win, image=self.photo, bd=0, background="white")
        self.label.grid(row=1, column=0, columnspan=2, pady=30)

        # 동물 이름과 레벨 나타내기
        # self.animal_name, self.levelup, self.경험치값 사용
        self.character = Label(win, text=f"{self.animal_name} lv. {self.levelup}({self.경험치값}%)", font=('um', 20), background='white', foreground='black')
        self.character.grid(row=3, column=0, columnspan=2, pady=10)

        # 공부시간 나타내기
        self.timer = Label(win, width=10, height=1, text='00:00', font=('BM Jua',80, 'normal'), background='white', foreground='red')
        self.timer.grid(row=4, column=0, columnspan=2, pady=20)

        # 버튼 생성
        self.bstart = Button(win, width=13, height=2, text="공부 시작", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.bend = Button(win, width=13, height=2, text="공부종료", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.bstop = Button(win, width=13, height=2, text="일시정지", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.breplay = Button(win, width=13, height=2, text="계속", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.windowend = Button(win, width=3, height=1, text="종료", font=("BM Jua", 20), highlightthickness=2, highlightbackground='black', command=confirm_exit)

        # 버튼 나타내기
        self.bstart.grid(row=5, column=0, padx=10, pady=10)
        self.bend.grid(row=5, column=1, padx=10, pady=10)
        self.bstop.grid(row=6, column=0, padx=10, pady=10)
        self.breplay.grid(row=6, column=1, padx=10, pady=10)
        self.windowend.grid(row=1, column=1)



    # 캐릭터 라벨을 업데이트하는 새로운 메서드 추가
    def update_character_display(self, name, level, exp):
        self.animal_name = name
        self.levelup = level
        self.경험치값 = exp
        self.character.config(text=f"{self.animal_name} lv. {self.levelup}({self.경험치값}%)")
