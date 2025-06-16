

# 메인 페이지 틀

from tkinter import *
from PIL import Image, ImageTk
# from runbutton import RunButton
import os


class StudyDamagochiFrame():
    def __init__(self, win):
    
        self.win = win
        
        # 창 생성 및 설정
        win.geometry("770x800")
        win.title("오늘은 공부를 했나요?")
        win.configure(background="white")
        
        # 메세지 나타내기, 설정
        self.message = Label(width=30, height=1, text='오늘은 공부를 했나요?', font=('BM Jua',40), background='white', foreground='black') # 더 얇은 버전을 원해... 글씨체
        self.message.grid(row=0, column=0, columnspan=2, pady=20)


        # 레벨,경험치,공부시간 설정
        self.levelup = 1 #레벨
        # self.perexper = 0 #경험치 퍼센트
        self.studytime = 0 # 공부시간
        self.경험치값 =0 # 공부시간에 따른 경험치값


        #동물 그림 설정
        img = Image.open("/Users/ttalgi/Documents/study/교과목/수행평가/파이썬/studyDamagochi/image/egg.png")
        img = img.resize((200, 200))
        self.photo = ImageTk.PhotoImage(img)


        # 동물 그림 나타내기g
        self.label = Label(win, image=self.photo, bd=0, background="white")
        self.label.grid(row=1, column=0, columnspan=2, pady=30)


        # 동물 이름과 레벨 나타내기
        self.character=Label(win, text=f"삑삑이 lv. {self.levelup}({self.경험치값}%)", font=('um', 20), background='white', foreground='black')
        self.character.grid(row=3, column=0, columnspan=2, pady=10)


        # 공부시간 나타내기
        self.timer = Label(win, width=10, height=1, text='00:00', font=('BM Jua',80, 'normal'), background='white', foreground='red')
        self.timer.grid(row=4, column=0, columnspan=2, pady=20)


        # 버튼 생성
        self.bstart = Button(win, width=13, height=2, text="공부 시작", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.bend = Button(win, width=13, height=2, text="공부종료", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.bstop = Button(win, width=13, height=2, text="일시정지", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)
        self.breplay = Button(win, width=13, height=2, text="계속", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=None)


        #버튼 나타내기
        self.bstart.grid(row=5, column=0, padx=10, pady=10) # 버튼 간격 줄이고 싶은데 안됨 ㅜ
        self.bend.grid(row=5, column=1, padx=10, pady=10)
        self.bstop.grid(row=6, column=0, padx=10, pady=10)
        self.breplay.grid(row=6, column=1, padx=10, pady=10)
