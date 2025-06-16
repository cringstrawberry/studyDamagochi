from tkinter import *

class SaveFile:
    def __init__(self, make_animal_instance):
        self.make_animal = make_animal_instance  # MakeAnimal 인스턴스를 전달받음

    def 생성(self, win, aniname,password,level=1,경험치=0):
        self.win = win
        self.aniname=aniname
        self.password=password
        self.level=level
        self.경험치=경험치

        # Entry 위젯은 MakeAnimal 쪽에 있으므로, 그걸 참조해서 get()
        with open("animal.txt", "w", encoding="utf-8") as f:
            f.write("{")
            f.write(str(aniname) + ",\n") 
            f.write(str(password) + ",\n")
            f.write(str(level) + ",\n")
            f.write(str(경험치) + ",\n")
            f.write("}")

    def 로그인정보불러오기(self, aniname, password):
        try:
            with open("animal.txt", "r", encoding="utf-8") as f:
                for line in f:
                    id, pw = line.strip().split(",")
                    if id == aniname and pw == password:
                        return True  # 로그인 성공
            return False  # 로그인 실패
        except FileNotFoundError:
            print("사용자 파일이 없습니다.")
            return False