from tkinter import *

class SaveFile:
    def __init__(self, make_animal_instance):
        self.make_animal = make_animal_instance  # MakeAnimal 인스턴스를 전달받음

    def 생성(self, win):
        self.win = win

        # Entry 위젯은 MakeAnimal 쪽에 있으므로, 그걸 참조해서 get()
        with open("animal_name.txt", "w", encoding="utf-8") as f:
            f.write(self.make_animal.aniname.get() + "\n") 
            f.write(self.make_animal.password.get() + "\n")

    def 로그인(self, aniname, password):
        try:
            with open("users.txt", "r", encoding="utf-8") as f:
                for line in f:
                    id, pw = line.strip().split(",")
                    if id == aniname and pw == password:
                        return True  # 로그인 성공
            return False  # 로그인 실패
        except FileNotFoundError:
            print("사용자 파일이 없습니다.")
            return False