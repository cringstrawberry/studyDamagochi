from tkinter import *
from frame import StudyDamagochiFrame
from runbutton import RunButton # RunButton이 있다고 가정합니다.
from makeanimal import MakeAnimal
from filesave import SaveFile

if __name__== "__main__":
    win = Tk()

    # 1. 파일에서 초기 동물 데이터 불러오기
    saver = SaveFile() # SaveFile 인스턴스 생성
    initial_animal_data = saver.불러오기() # 저장된 데이터 불러오기

    # 2. StudyDamagochiFrame을 생성할 때 불러온 데이터를 전달
    #    데이터가 없으면 StudyDamagochiFrame 내부의 기본값이 사용됩니다.
    app = StudyDamagochiFrame(win, initial_animal_data=initial_animal_data)
    
    # RunButton이 StudyDamagochiFrame 인스턴스(app)를 필요로 하는 경우 이렇게 전달합니다.
    # RunButton 클래스 내부의 __init__ 정의가 RunButton(self, study_damagochi_frame) 형태여야 합니다.
    logic = RunButton(app) 
    
    # 3. MakeAnimal을 생성할 때 win과 함께 app(StudyDamagochiFrame 인스턴스)을 전달
    real = MakeAnimal(win, app) # <-- 이 부분이 가장 중요합니다.

    # 저장된 동물이 없는 경우 (initial_animal_data가 None일 경우),
    # MakeAnimal 창을 자동으로 띄우는 로직을 추가합니다.
    if initial_animal_data is None:
        real.aniset(win) # 처음 실행 시 저장된 데이터가 없으면 자동 팝업

    # "새로운 친구 만나기" 버튼은 여전히 수동으로 창을 띄울 수 있게 합니다.
    open_button = Button(win, text="새로운 친구 만나기", command=lambda: real.aniset(win), width=10,height=2)
    open_button.grid(row=7 , column=0, columnspan=2)

    win.mainloop()



# from tkinter import *
# # from PIL import Image, ImageTk
# from frame import StudyDamagochiFrame
# from runbutton import RunButton
# from makeanimal import MakeAnimal
# from filesave import SaveFile

# if __name__== "__main__":
#     win=Tk()
#     app = StudyDamagochiFrame(win)
#     logic = RunButton(app)
#     real = MakeAnimal(win)

#     open_button = Button(win, text="새로운 친구 만나기", command=lambda: real.aniset(win), width=10,height=2)
#     open_button.grid(row=7 , column=0, columnspan=2)


#     saver = SaveFile()
#     win.mainloop()