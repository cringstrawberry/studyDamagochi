# from tkinter import *
# win = Tk() #창 생성
# win.geometry("2000x2000") # 창 크기
# win.title("chobo_coding") #창 제목
# win.option_add("*Font","맑은고딕 25") #전체 폰트
# win.mainloop() #창 실행

from tkinter import * # tkinter 불러오기
win = Tk() # 창 생성
win.geometry("500x500") # 창 크기
win.title("집에 보내주세요") # 창 제목
win.option_add("*font", "굴림 20") # 폰트, 글자 크기 설정

btn = Button(win, text="버튼") # 버튼 생성
btn.pack() # 버튼 실행

win.mainloop() # 창 실행