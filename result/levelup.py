# 레벨업

from tkinter import *
from frame import StudyDamagochiFrame
from studyDamagochi.result.setanimal import MakeAnimal

class LevleUp(StudyDamagochiFrame, MakeAnimal):
    def exper(self):
        if self.stoping:
            self.studytime = self.minutes
            self.howmany = self.studytime//10
            if self.howmany>=1:
                self.경험치값+=self.howmany*5 #10분마다 경험치 5 해당
                if self.경험치값==100:
                    print('레벨업하였습니다!')
                    # levelup()
                else:
                    print('경험치가 올랐습니다.')
            else:
                print('10분 단위로 경험치가 오릅니다. 좀 더 공부하세요!')

    # def levelup(self):
    #     self.levelup+=1
        

    # def imagesize(self, width, height):
        








 # def exper(self):
    #     if self.stoping:
    #         self.studytime = self.minutes+(self.seconds//60) #분 + 초//60
    #         self.perexper = f'{self.studytime//60:.1f}' #
    #     if self.perexper//10>=1:
    #         self.경험치값 +=self.perexper//10
    #         if self.경험치값 == 100:
    #             self.levelup+=1
    #             print('1레벨 올랐습니다')
    #             # self.(대충 이미지 연결)

    #         else:
    #             print('경험치가 올랐습니다.')
    #     else:
    #         print('10분 단위로 경험치가 오릅니다. 좀 더 공부하세요!')