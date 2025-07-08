# 메인 페이지 틀

from tkinter import *
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

class StudyDamagochiFrame():
    def __init__(self, win, initial_animal_data=None):
        self.win = win
        self.image_size = 150

        def confirm_exit():
            if messagebox.askokcancel("종료 확인", "정말 종료하시겠어요?"):
                win.destroy()

        win.geometry("770x880")
        win.title("오늘은 공부를 했나요?")
        win.configure(background="white")

        # 루트 윈도우 그리드 확장 설정
        win.grid_rowconfigure(0, weight=1)
        win.grid_columnconfigure(0, weight=1)

        mainframe = Frame(win)
        mainframe.grid(row=0, column=0, sticky="nsew")

        # mainframe 그리드 확장 설정
        mainframe.grid_rowconfigure(0, weight=1)  # 이미지 프레임 확장
        mainframe.grid_rowconfigure(1, weight=0)  # 버튼 프레임 고정
        mainframe.grid_columnconfigure(0, weight=1)

        imageframe = Frame(mainframe, relief="solid", bg='white')
        imageframe.grid(row=0, column=0, columnspan=2, sticky='nsew')

        buttonframe = Frame(mainframe, relief="solid", bg='white')
        buttonframe.grid(row=1, column=0, columnspan=2, sticky='nsew')

        # imageframe 행,열 weight 설정 (이미지와 종료버튼 중앙 정렬 및 확장 허용)
        imageframe.grid_rowconfigure(1, weight=1)
        imageframe.grid_columnconfigure(0, weight=1)
        imageframe.grid_columnconfigure(1, weight=1)

        # 버튼 프레임 자동 크기 조절 방지 및 높이 지정
        buttonframe.grid_propagate(False)
        buttonframe.config(height=350)

        # 버튼프레임 행,열 weight 균등 분배
        for i in range(5):
            buttonframe.grid_rowconfigure(i, weight=1)
        buttonframe.grid_columnconfigure(0, weight=1)
        buttonframe.grid_columnconfigure(1, weight=1)

        # 메시지 (imageframe 상단)
        self.message = Label(imageframe, width=30, height=1, text='오늘은 공부를 했나요?', font=('BM Jua', 40), background='white', foreground='black')
        self.message.grid(row=0, column=0, columnspan=2, pady=20)

        # 초기값 세팅
        if initial_animal_data:
            self.levelup = initial_animal_data.get("level", 1)
            self.경험치값 = initial_animal_data.get("경험치", 0)
            self.animal_name = initial_animal_data.get("name", "삑삑이")
        else:
            self.levelup = 1
            self.경험치값 = 0
            self.animal_name = "삑삑이"

        self.studytime = 0

        # 수정된 부분: 파일 경로만 먼저 추출하고 존재 여부 검사
        img_file_path = resource_path("egg.jpg")
        if os.path.exists(img_file_path):
            img = Image.open(img_file_path)
            img = img.resize((150, 150))
            self.photo = ImageTk.PhotoImage(img)
        else:
            messagebox.showerror("오류", f"이미지가 존재하지 않아요. {img_file_path}")
            self.photo = None

        # 이미지 라벨 (imageframe 중앙)
        self.label = Label(imageframe, bd=0, background="white", anchor="center")
        self.label.grid(row=1, column=0, columnspan=2, pady=30, sticky="nsew")
        self.update_animal_image()

        # 종료 버튼 (imageframe 우측 하단)
        self.windowend = Button(imageframe, width=3, height=1, text="종료", font=("BM Jua", 20),
                                highlightthickness=2, highlightbackground='black', command=confirm_exit)
        # 종료 버튼은 우측 에 붙임
        self.windowend.grid(row=0, column=1, sticky="se", padx=10, pady=10)

        # character 라벨 (buttonframe)
        self.character = Label(buttonframe, text=f"{self.animal_name} lv. {self.levelup}({self.경험치값}%)",
                               font=('um', 20), background='white', foreground='black')
        self.character.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        # timer 라벨 (buttonframe)
        self.timer = Label(buttonframe, width=10, height=1, text='00:00', font=('BM Jua', 80, 'normal'),
                           background='white', foreground='red')
        self.timer.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        # 버튼들 (buttonframe)
        self.bstart = Button(buttonframe, width=10, height=2, text="공부 시작", font=('BM Jua', 25),
                             activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.bend = Button(buttonframe, width=10, height=2, text="공부종료", font=('BM Jua', 25),
                           activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.bstop = Button(buttonframe, width=10, height=2, text="일시정지", font=('BM Jua', 25),
                            activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.breplay = Button(buttonframe, width=10, height=2, text="계속", font=('BM Jua', 25),
                              activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)

        # 버튼 그리드 배치
        self.bstart.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.bend.grid(row=2, column=1, padx=20, pady=10, sticky="ew")
        self.bstop.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.breplay.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

    def update_character_display(self, name, level, exp):
        self.animal_name = name
        self.levelup = level
        self.경험치값 = exp
        self.character.config(text=f"{self.animal_name} lv. {self.levelup}({self.경험치값}%)")

    def update_animal_image(self):
        # 수정된 부분: 파일 경로만 먼저 추출하고 존재 여부 검사
        img_file_path = resource_path("egg.jpg")
        if os.path.exists(img_file_path):
            img = Image.open(img_file_path)
            img = img.resize((self.image_size, self.image_size))
            self.photo = ImageTk.PhotoImage(img)
            self.label.config(image=self.photo)
            self.label.image = self.photo
        else:
            messagebox.showerror("오류", f"이미지가 존재하지 않아요. {img_file_path}")
            self.photo = None