# 레벨업

from tkinter import *


class LevelUp:
    def __init__(self, win, study_frame, animal_maker, savefile_instance):
        self.win = win
        self.study_frame = study_frame # 경험치값, levelup 변수 가져오기
        self.animal_maker = animal_maker
        self.SaveFile = savefile_instance


        self.stoping = True

    def exper(self, minutes):
        if self.stoping:
            self.studytime = minutes #분마다 계산
            self.howmany = self.studytime
            if self.howmany>=1:
                # 현재 경험치값 지정
                current_exp = self.study_frame.경험치값
                current_level = self.study_frame.levelup

                # 경험치 누적
                current_exp += self.howmany*5 #사실은 1
                self.study_frame.경험치값 = current_exp #1분마다 경험치 1 해당

                # 레벨업 처리
                while current_exp >= 10: #사실은 100%
                    current_level += 1 #1레벨 상승
                    self.imageup() #이미지 크기 조절
                    current_exp -= 10 # 레벨업한 후 경험치 초기화
                    print(f"레벨업! 현재 레벨: {current_level}")

                # 변경된 경험치 및 레벨 저장
                self.study_frame.경험치값 = current_exp
                self.study_frame.levelup = current_level

                # 화면에 변경 사항 반영
                self.study_frame.update_character_display(
                    self.study_frame.animal_name, current_level, current_exp
                    
                )
                self.SaveFile.업데이트(self.study_frame.animal_name, current_level, current_exp)
            else:
                print(f"1분 단위로 경험치가 오릅니다. 현재 공부 시간: {minutes}분") # print 다 메세지로 바꾸기

    def imageup(self):
        # 레벨업마다 이미지 크기를 25씩 증가
        self.study_frame.image_size += 25 #얼마나 커지는지 테스트 해보기, 창도 커지게 만들기
        # 변경된 크기로 이미지 다시 그리기
        self.study_frame.update_animal_image()