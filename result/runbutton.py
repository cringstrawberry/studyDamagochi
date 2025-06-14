from tkinter import *
from PIL import Image, ImageTk
import os

from frame import StudyDamagochiFrame


class RunButton(StudyDamagochiFrame):
    def __init__(self, frame):
        self.frame = frame
        self.frame.bstart.config(command=self.공부시작)
        self.frame.bend.config(command=self.공부종료)
        self.frame.bstop.config(command=self.일시정지)
        self.frame.breplay.config(command=self.계속)

        self.sec=0
        self.playing=False
        self.stoping = False

    def 공부시작(self): # 여러번 누르면 왜 누적되내
        if not self.playing and not self.stoping:   # 타이머가 실행중이 아닐 때만 시작
            self.playing = True
            self.타이머업데이트()

    def 공부종료(self):
        self.playing = False
        self.sec = 0
        self.frame.timer.config(text="00:00")

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
            self.minutes = self.sec // 60
            self.seconds = self.sec % 60
            self.frame.timer.config(text=f"{self.minutes:02}:{self.seconds:02}")
            self.frame.win.after(1000, self.타이머업데이트)