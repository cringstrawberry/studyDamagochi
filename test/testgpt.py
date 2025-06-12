import tkinter as tk
from PIL import Image, ImageTk
import os
import time # 타이머 기능 구현을 위해 time 모듈 임포트

class StudyTimerApp:
    def __init__(self, master):
        self.master = master
        master.title("오늘은 공부를 했나요?")
        master.geometry("600x700") # 창 크기
        master.configure(background="white")

        # --- 이미지 파일 경로 설정 ---
        # 현재 스크립트 파일이 있는 디렉토리를 기준으로 'image' 폴더를 찾습니다.
        current_dir = os.path.dirname(__file__)
        self.egg_image_path = os.path.join(current_dir, "image", "egg.png")
        self.yellow_button_image_path = os.path.join(current_dir, "image", "button_yellow.png")

        # --- 이미지 로드 및 PhotoImage 변환 ---
        self.egg_photo = self._load_image(self.egg_image_path, (200, 200))
        self.yellow_button_photo = self._load_image(self.yellow_button_image_path, (200, 60)) # 버튼 크기에 맞게 조절

        # --- 위젯 생성 및 배치 ---

        # 1. "오늘 공부를 했나요?" 제목
        self.title_label = tk.Label(master, text="오늘은 공부를 했나요?", font=("Arial", 20), background="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(30, 10)) # 상단 여백 좀 더 줌

        # 2. 병아리 이미지 (Label)
        self.image_label = tk.Label(master, image=self.egg_photo, bd=0, background="white")
        self.image_label.grid(row=1, column=0, columnspan=2, pady=5)

        # 3. "삑삑이 lv. 1" 라벨
        self.aniname_label = tk.Label(master, text="삑삑이 lv. 1", font=("Arial", 16), background="white")
        self.aniname_label.grid(row=2, column=0, columnspan=2, pady=5)

        # 4. 타이머 (Label, 처음에는 "00:00"으로 표시)
        self.time_left = 0 # 남은 시간 (초 단위)
        self.running = False # 타이머 실행 상태
        self.timer_label = tk.Label(master, text="00 : 00", font=("Arial", 40, "bold"), fg="red", background="white")
        self.timer_label.grid(row=3, column=0, columnspan=2, pady=20) # 타이머 상하 여백

        # 5. 버튼 4개
        # 테두리 설정
        border_thickness = 2 # 테두리 굵기 (이미지에서 얇게 보임)
        border_color = 'black' # 테두리 색상

        # 버튼들을 담을 프레임 (간격 조절 용이, 중앙 정렬 용이)
        self.button_frame = tk.Frame(master, bg="white")
        self.button_frame.grid(row=4, column=0, columnspan=2, pady=10) # 버튼 프레임 상하 여백

        # 버튼 생성
        self.bstart = tk.Button(self.button_frame, text="공부시작",
                                image=self.yellow_button_photo, compound="center",
                                fg='black',
                                borderwidth=border_thickness, relief="solid", bd=border_thickness,
                                highlightthickness=0,
                                background=border_color,
                                command=self.start_study) # command 연결

        self.bend = tk.Button(self.button_frame, text="공부종료",
                              image=self.yellow_button_photo, compound="center",
                              fg='black',
                              borderwidth=border_thickness, relief="solid", bd=border_thickness,
                              highlightthickness=0,
                              background=border_color,
                              command=self.end_study) # command 연결

        self.bstop = tk.Button(self.button_frame, text="일시정지",
                               image=self.yellow_button_photo, compound="center",
                               fg='black',
                               borderwidth=border_thickness, relief="solid", bd=border_thickness,
                               highlightthickness=0,
                               background=border_color,
                               command=self.pause_study) # command 연결

        self.breplay = tk.Button(self.button_frame, text="계속",
                                 image=self.yellow_button_photo, compound="center",
                                 fg='black',
                                 borderwidth=border_thickness, relief="solid", bd=border_thickness,
                                 highlightthickness=0,
                                 background=border_color,
                                 command=self.resume_study) # command 연결

        # 버튼 배치 (프레임 내에서 padx, pady로 간격 조절)
        button_padx = 5 # 버튼 가로 간격
        button_pady = 5 # 버튼 세로 간격

        self.bstart.grid(row=0, column=0, padx=button_padx, pady=button_pady)
        self.bend.grid(row=0, column=1, padx=button_padx, pady=button_pady)
        self.bstop.grid(row=1, column=0, padx=button_padx, pady=button_pady)
        self.breplay.grid(row=1, column=1, padx=button_padx, pady=button_pady)

        # --- 타이머 기능 초기화 및 업데이트 ---
        # self.update_timer() # 앱 시작 시 타이머 바로 시작하고 싶다면 주석 해제

    # --- 헬퍼 함수: 이미지 로드 ---
    def _load_image(self, path, size):
        if not os.path.exists(path):
            print(f"경고: 이미지 파일 '{path}'을(를) 찾을 수 없습니다. 해당 이미지는 표시되지 않습니다.")
            return None
        try:
            img_raw = Image.open(path)
            img_resized = img_raw.resize(size, Image.Resampling.LANCZOS) # 품질 향상된 리사이징
            return ImageTk.PhotoImage(img_resized)
        except Exception as e:
            print(f"오류: 이미지 '{path}' 로드 또는 리사이징 중 오류 발생: {e}")
            return None

    # --- 타이머 관련 메서드 ---
    def update_timer(self):
        if self.running:
            self.time_left -= 1
            if self.time_left < 0:
                self.time_left = 0
                self.running = False # 타이머 종료

            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.timer_label.config(text=f"{minutes:02d} : {seconds:02d}")
            self.master.after(1000, self.update_timer) # 1초마다 업데이트

    def start_study(self):
        if not self.running:
            # 예시로 10분(600초) 설정. 실제로는 사용자 입력 등으로 설정할 수 있습니다.
            self.time_left = 600
            self.running = True
            self.update_timer()
            print("공부 시작!")

    def end_study(self):
        self.running = False
        self.time_left = 0
        self.timer_label.config(text="00 : 00")
        print("공부 종료!")

    def pause_study(self):
        if self.running:
            self.running = False
            print("일시정지!")

    def resume_study(self):
        if not self.running and self.time_left > 0: # 멈춰있고, 남은 시간이 있을 때만 계속
            self.running = True
            self.update_timer()
            print("계속!")

# --- 앱 실행 ---
if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimerApp(root)
    root.mainloop()