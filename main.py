from tkinter import *
from PIL import ImageTk
from PIL import Image as Img
from random import randint


class Game:
    # Инициализация класса.
    def __init__(self):
        self.width, self.height = 460, 660
        self.game = Tk()  # Создание окна
        self.game.title('Shashki')  # Название программы
        # self.ma1n.iconbitmap('favicon.ico')  # Добавляем иконку
        self.game.geometry(f'{self.width}x{self.height}')  # Определяем размер окна
        self.game.resizable(False, False)  # Окно нельзя расширять по осям Х и У
        self.game.attributes('-topmost', True)  # Окно при запуске уходит на передний план
        self.game.bind('<KeyRelease-Left>', lambda event: self.left())
        self.game.bind('<KeyRelease-a>', lambda event: self.left())
        self.game.bind('<KeyRelease-A>', lambda event: self.left())
        self.game.bind('<KeyRelease-Right>', lambda event: self.right())
        self.game.bind('<KeyRelease-d>', lambda event: self.right())
        self.game.bind('<KeyRelease-D>', lambda event: self.right())

        self.status = True
        self.player_position = 1
        self.speed = 5
        self.car_position = 0
        self.car_y = 0
        self.hole_position = 0
        self.hole_y = 0
        self.score = 0
        self.y = 0

        self.background_image = ImageTk.PhotoImage(Img.open('wallpaper.png'))
        self.background = Label(self.game, image=self.background_image)
        self.player_image = ImageTk.PhotoImage(Img.open('player.png'))
        self.player = Label(self.game, image=self.player_image, border='0', relief=FLAT)
        self.car_image = ImageTk.PhotoImage(Img.open('car.png'))
        self.car = Label(self.game, image=self.car_image, border='0', relief=FLAT)
        self.hole_image = ImageTk.PhotoImage(Img.open('hole.png'))
        self.hole = Label(self.game, image=self.hole_image, border='0', relief=FLAT)
        self.score_label = Label(self.game, text=self.score, font=('Arial', 20))

        self.lose_label = Label(self.game)
        self.lose_button = Button(self.game, text='Повторить', border='0', relief=FLAT, command=self.start)

        self.start()
        self.game.mainloop()

    def start(self):
        self.lose_label.place_forget()
        self.lose_button.place_forget()
        self.status = True
        self.player_position = 1
        self.car_y = 0
        self.hole_y = 0
        self.score = 0
        self.y = 0
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.player.place(x=130, y=550)
        self.score_label.place(x=360, y=50, width=50)
        self.spawn('car')
        self.spawn('hole')
        self.loop()

    def lose(self):
        self.lose_label.place(x=24, y=200, width=310, height=120)
        self.lose_button.place(x=130, y=295, width=100)
        self.status = False

    def spawn(self, obstacle):
        self.y = 0
        if obstacle == 'hole':
            self.hole_y = randint(0, 100) + 10 * self.y
            self.hole_position = randint(0, 2)
            self.hole.place(x=25 + 105 * self.hole_position, y=self.hole_y)
        if obstacle == 'car':
            self.car_y = randint(0, 100) + 10 * self.y
            while self.car_position == self.hole_position:
                self.car_position = randint(0, 2)
            self.car.place(x=25 + 105 * self.car_position, y=self.car_y)

    def loop(self):
        if self.status:
            self.y += 1
            self.hole_y += self.speed
            self.car_y += self.speed
            self.hole.place_forget()
            self.hole.place(x=25 + 105 * self.hole_position, y=self.hole_y)
            self.car.place_forget()
            self.car.place(x=25 + 105 * self.car_position, y=self.car_y)
            if self.hole_position == self.player_position and 647 >= self.hole_y >= 454:
                self.lose_label.config(text=f'Вы проиграли!\nВаши очки: {self.score}.')
                self.lose()
            if self.car_position == self.player_position and 647 >= self.car_y >= 454:
                self.lose_label.config(text=f'Вы проиграли!\nВаши очки: {self.score}.')
                self.lose()
            if self.hole_y >= self.height:
                self.spawn('hole')
                self.score += 1
            if self.car_y >= self.height:
                self.spawn('car')
                self.score += 1
            self.score_label['text'] = self.score

            self.game.after(150, self.loop)

    def left(self):
        if self.player_position == 0:
            pass
        elif self.player_position == 1:
            self.player.place(x=25, y=550)
            self.player_position = 0

        else:
            self.player.place(x=130, y=550)
            self.player_position = 1

    def right(self):
        if self.player_position == 0:
            self.player.place(x=130, y=550)
            self.player_position = 1
        elif self.player_position == 1:
            self.player.place(x=235, y=550)
            self.player_position = 2
        else:
            pass


if __name__ == '__main__':
    _ = Game()
