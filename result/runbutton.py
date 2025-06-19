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

        self.sec = 0
        self.playing = False
        self.stoping = False
        self.timer_id = None
        self.starting = False


    def 공부시작(self):
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
        self.sec = 0
        self.frame.timer.config(text="00:00")
        if self.timer_id:  # 타이머 중단
            self.frame.win.after_cancel(self.timer_id)
            self.timer_id = None

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
            self.timer_id = self.frame.win.after(1000, self.타이머업데이트)