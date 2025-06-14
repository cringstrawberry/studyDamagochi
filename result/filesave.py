from tkinter import *
from makeanimal import MakeAnimal


class SaveFile(MakeAnimal):

    def 생성(self, win):
        self.win = win

        with open("animal_name.txt", "w", encoding="utf-8") as f:
            f.write(self.aniname.get()+"\n") 
            f.write(self.password.get() + "\n")

    def 로그인(self, aniname, password):
        try:
            with open("users.txt", "r") as f:
                for line in f:
                    id, pw = line.strip().split(",")
                if id == aniname and pw == password:
                    return True  # 로그인 성공
            return False  # 로그인 실패
        except FileNotFoundError:
            print("사용자 파일이 없습니다.")
            return False