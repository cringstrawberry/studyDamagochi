from tkinter import Tk
from app_controller import AppController
#실행
if __name__ == "__main__":
    win = Tk()
    app = AppController(win)
    win.mainloop()