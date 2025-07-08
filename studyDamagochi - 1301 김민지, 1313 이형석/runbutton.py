from tkinter import *
from PIL import Image, ImageTk
import os

from frame import StudyDamagochiFrame

# 버튼 실행 기능
class RunButton(StudyDamagochiFrame):
    def __init__(self, frame, levelup_instance):
        self.frame = frame
        self.levelup_instance = levelup_instance # 레벨업 객체 들고오기
        self.frame.bstart.config(command=self.공부시작)
        self.frame.bend.config(command=self.공부종료)
        self.frame.bstop.config(command=self.일시정지)
        self.frame.breplay.config(command=self.계속)

        self.sec = 0
        self.playing = False
        self.stoping = False
        self.timer_id = None
        self.starting = False


    def 공부시작(self):
        # if messagebox.askokcancel("종료 확인", "정말 종료하시겠어요?"):
            if not self.stoping and not self.starting:
                self.playing = True
                self.stoping = False
                self.starting = True
                if self.timer_id:  # 이전 타이머가 있다면 취소
                    self.frame.win.after_cancel(self.timer_id)
                    self.timer_id = None
                self.타이머업데이트()

    def 계속(self):
        if self.playing and self.stoping:
            self.playing = True
            self.stoping = False
            if self.timer_id:  # 이전 타이머가 있다면 취소
                self.frame.win.after_cancel(self.timer_id)
                self.timer_id = None
            self.타이머업데이트()

    def 공부종료(self):
        self.playing = False
        self.stoping = False
        self.starting = False

        total_minutes = self.sec // 60 # 분으로 계산
        self.sec = 0
        self.frame.timer.config(text="00:00")

        if self.timer_id:  # 타이머 중단
            self.frame.win.after_cancel(self.timer_id)
            self.timer_id = None

        self.levelup_instance.exper(total_minutes) #공부시간 계산해서 레벨업인스턴스에 전달

        self.levelup_instance.SaveFile.업데이트(
        self.frame.animal_name,
        self.frame.levelup,
        self.frame.경험치값,
        self.frame.image_size  # 현재 이미지 크기(동물덩치)
    )


    def 일시정지(self):
        if self.playing:
            self.stoping = True
            if self.timer_id:
                self.frame.win.after_cancel(self.timer_id)
                self.timer_id = None
            
    def 타이머업데이트(self):
        if self.playing:
            self.sec += 1
            minutes = self.sec // 60
            seconds = self.sec % 60
            self.frame.timer.config(text=f"{minutes:02}:{seconds:02}")
            self.timer_id = self.frame.win.after(1000, self.타이머업데이트) # 흐르는 시간 출력