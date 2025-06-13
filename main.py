# 메인 페이지 틀

from tkinter import *
from PIL import Image, ImageTk
import os


class StudyDamagochi:
    def __init__(self, win):
        
        self.win = win
        self.sec = 0
        self.playing = False
        self.stoping = False
        
        # 창 생성 및 설정
        win.geometry("770x760")
        win.title("오늘은 공부를 했나요?")
        win.configure(background="white")
        
        # 메세지 나타내기, 설정
        self.message = Label(width=30, height=1, text='오늘은 공부를 했나요?', font=('BM Jua',40), background='white', foreground='black') # 더 얇은 버전을 원해... 글씨체
        self.message.grid(row=0, column=0, columnspan=2, pady=20)


        # 레벨 설정
        self.levelnum = 'lv. 1'


        #동물 그림 설정
        img = Image.open("egg.jpg")
        img = img.resize((200, 200))
        self.photo = ImageTk.PhotoImage(img)


        # 동물 그림 나타내기
        self.label = Label(win, image=self.photo, bd=0, background="white")
        self.label.grid(row=1, column=0, columnspan=2, pady=30)


        # 동물 이름과 레벨 나타내기
        self.aniname=Label(win, text=f"삑삑이 {self.levelnum}", font=('um', 20), background='white', foreground='black')
        self.aniname.grid(row=3, column=0, columnspan=2, pady=10)


        # 공부시간 나타내기
        self.timer = Label(win, width=10, height=1, text='00:00', font=('BM Jua',80, 'normal'), background='white', foreground='red')
        self.timer.grid(row=4, column=0, columnspan=2, pady=20)


        # 버튼 생성
        self.bstart = Button(win, width=13, height=2, text="공부 시작", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=self.공부시작)
        self.bend = Button(win, width=13, height=2, text="공부종료", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=self.공부종료)
        self.bstop = Button(win, width=13, height=2, text="일시정지", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=self.일시정지)
        self.breplay = Button(win, width=13, height=2, text="계속", font=('BM Jua', 30), activebackground="yellow", highlightthickness=2, highlightbackground='yellow', command=self.계속)


        #버튼 나타내기
        self.bstart.grid(row=5, column=0, padx=10, pady=10) # 버튼 간격 줄이고 싶은데 안됨 ㅜ
        self.bend.grid(row=5, column=1, padx=10, pady=10)
        self.bstop.grid(row=6, column=0, padx=10, pady=10)
        self.breplay.grid(row=6, column=1, padx=10, pady=10)
        
    #시간 측정
        
    def 공부시작(self): # 여러번 누르면 왜 누적되내
        if not self.playing and not self.stoping:   # 타이머가 실행중이 아닐 때만 시작
            self.playing = True
            self.타이머업데이트()
    def 공부종료(self):
        self.playing = False
        self.sec = 0
        self.timer.config(text="00:00")

    def 일시정지(self):
        self.playing = False
        self.stoping = True

    def 계속(self):
        if not self.playing:
            self.playing = True
            self.stoping = False
            self.타이머업데이트()

    def 타이머업데이트(self):
        if self.playing:
            self.sec += 1
            minutes = self.sec // 60
            seconds = self.sec % 60
            self.timer.config(text=f"{minutes:02}:{seconds:02}")
            self.win.after(1000, self.타이머업데이트)

if __name__ == '__main__':
    root = Tk()
    app = StudyDamagochi(root)
    root.mainloop()
print('hello')