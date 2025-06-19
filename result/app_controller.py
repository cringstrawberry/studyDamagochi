from tkinter import messagebox, Button
from tkinter import Tk
from frame import StudyDamagochiFrame
from setanimal import MakeAnimal
from levelup import LevelUp
from runbutton import RunButton
from filesave import SaveFile

# 클래스 인자 전달 그리고 시작
class AppController:
    def __init__(self, win):
        self.win = win
        
        # 데이터 저장, 불러오기 담당
        self.saver = SaveFile()
        
        # 기존 동물 목록 불러오기
        self.all_animals = self.saver.목록불러오기()
        
        # 틀
        self.view = StudyDamagochiFrame(win)
        
        # 동물 관리
        self.make_animal = MakeAnimal(win, self.view)

        #레벨 업데이트
        savefile_instance = SaveFile()
        
        # 레벨업 관리
        self.level_up = LevelUp(win, self.view, self.make_animal, savefile_instance)
        
        # 공부 타이머 로직
        self.logic = RunButton(self.view, self.level_up)
        
        # runbutton 인스턴스를 make_animal에 나중에 연결
        self.make_animal.logic = self.logic
        
        # 시작 시 새로운 친구 안내
        messagebox.showinfo("시작", "환영합니다! 처음이신가요? \n새로운 동물 친구를 만들어주세요.")
        self.make_animal.aniset(win)
        
        # 버튼 UI를 main.py 대신 여기서 생성/관리해도 되고
        self.setup_buttons()
    
    def setup_buttons(self):
        # 새로운 친구 버튼
        new_friend_btn = Button(self.win, text="새로운 친구 만나기", command=lambda: self.make_animal.aniset(self.win),
                                width=15, height=2, font=('BM Jua', 15))
        new_friend_btn.grid(row=7, column=0, columnspan=2, pady=10)
        
        # 친구 떠나보내기 버튼
        delate_friend_btn = Button(self.win, text="친구랑 헤어지기", command=lambda: self.make_animal.계정삭제창(self.win),
                                   width=15, height=2, font=('BM Jua', 15))
        delate_friend_btn.grid(row=8, column=0, columnspan=2)

    # 컨트롤러가 필요하면 중간에서 이벤트 핸들링 함수도 둘 수 있음
