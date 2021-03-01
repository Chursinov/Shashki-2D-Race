from tkinter import *
from PIL import ImageTk
from PIL import Image as Img
from random import randint


class Game:
    # Инициализация класса.
    def __init__(self):
        self.game = Tk()  # Создание окна
        self.game.title('Shashki')  # Название программы
        # self.ma1n.iconbitmap('favicon.ico')  # Добавляем иконку
        self.game.geometry('460x660')  # Определяем размер окна
        self.game.resizable(False, False)  # Окно нельзя расширять по осям Х и У
        self.game.attributes('-topmost', True)  # Окно при запуске уходит на передний план
        self.game.bind('<KeyRelease-Left>', lambda event: self.left())
        self.game.bind('<KeyRelease-a>', lambda event: self.left())
        self.game.bind('<KeyRelease-A>', lambda event: self.left())
        self.game.bind('<KeyRelease-Right>', lambda event: self.right())
        self.game.bind('<KeyRelease-d>', lambda event: self.right())
        self.game.bind('<KeyRelease-D>', lambda event: self.right())
        self.car_position = 1
        self.score = 0

        self.background_image = ImageTk.PhotoImage(Img.open('wallpaper.png'))
        self.background_label = Label(self.game, image=self.background_image)
        self.car_image = ImageTk.PhotoImage(Img.open('car.png'))
        self.car_label = Label(self.game, image=self.car_image, border='0', relief=FLAT)
        self.score_label = Label(self.game, text=self.score, font=('Arial', 20))

        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.car_label.place(x=130, y=550)
        self.score_label.place(x=360, y=50, width=50)

        self.game.mainloop()

    def left(self):
        if self.car_position == 0:
            pass
        elif self.car_position == 1:
            self.car_label.place(x=25, y=550)
            self.car_position = 0

        else:
            self.car_label.place(x=130, y=550)
            self.car_position = 1

    def right(self):
        if self.car_position == 0:
            self.car_label.place(x=130, y=550)
            self.car_position = 1
        elif self.car_position == 1:
            self.car_label.place(x=235, y=550)
            self.car_position = 2
        else:
            pass


if __name__ == '__main__':
    _ = Game()
