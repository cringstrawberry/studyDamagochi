from tkinter import *
try:
    from tkinter import messagebox
except ImportError:
    import tkMessageBox as messagebox

class LevelUp:
    def __init__(self, win, study_frame, animal_maker, savefile_instance):
        self.win = win
        self.study_frame = study_frame  # 경험치값, levelup 변수 가져오기
        self.animal_maker = animal_maker
        self.SaveFile = savefile_instance

        self.stoping = True
        self.last_checked_minute = 0  # 이전에 경험치 반영한 공부 시간 분 저장

    # minutes 는 "전체 누적 공부 시간" 으로 받는다고 가정
    # 내부에서 증가분만 계산하여 경험치 올림
    def exper(self, total_minutes):
        if self.stoping:
            studytime = total_minutes - self.last_checked_minute  # 새로 추가된 분
            if studytime >= 1:
                current_exp = self.study_frame.경험치값
                current_level = self.study_frame.levelup
                current_big = self.study_frame.image_size

                # 경험치 증가
                current_exp += studytime * 1  # 1분에 1% 경험치 증가

                # 레벨업 처리
                while current_exp >= 100:
                    if current_level == 10:
                        messagebox.showinfo("만렙", "당신은 만렙입니다!")
                        current_exp = 0
                        break
                    current_level += 1
                    self.imageup()
                    current_big = self.study_frame.image_size  # ★ 변경된 이미지 크기 다시 반영
                    current_exp -= 100
                    print(f"레벨업! 현재 레벨: {current_level}")

                # 상태 저장
                self.study_frame.경험치값 = current_exp
                self.study_frame.levelup = current_level
                self.study_frame.image_size = current_big

                # 화면 갱신
                self.study_frame.update_character_display(
                    self.study_frame.animal_name, current_level, current_exp
                )
                self.SaveFile.업데이트(
                    self.study_frame.animal_name,
                    current_level,
                    current_exp,
                    current_big
                )

                # 마지막으로 체크한 공부 시간 갱신
                self.last_checked_minute = total_minutes
            else:
                print(f"1분 단위로 경험치가 오릅니다. 현재 추가 공부 시간: {studytime}분")

    def imageup(self):
        # 레벨업마다 이미지 크기 25 증가
        self.study_frame.image_size += 25
        self.study_frame.update_animal_image()
