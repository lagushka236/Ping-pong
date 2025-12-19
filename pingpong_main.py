from pygame import *
mixer.init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
bg = transform.scale(image.load('background.png'), (win_width, win_height))
mixer.music.load('bg_music.mp3')
mixer.music.set_volume(0.4)
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, img: str, x: int, y: int, w: int, h: int, speed: int):
        self.w = w
        self.h = h
        self.img = transform.scale(image.load(img), (w, h))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height - self.h:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height - self.h:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

class Ball(GameSprite):
    def __init__(self, img: str, x: int, y: int, w: int, h: int, speed: int):
        super().__init__(img, x, y, w, h, speed)
        self.speed_x = speed
        self.speed_y = speed

    def rand_movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if s


player1 = Player('platform_left.png', win_width * 0.01, win_height // 2, win_width // 35, win_height // 5, win_height // 100)
player2 = Player('platform_right.png', win_width - win_width * 0.04, win_height // 2, win_width // 35, win_height // 5, win_height // 100)
ball = Ball('tennis_ball.png', win_width // 2, win_height // 2, win_width // 14, win_height // 10, win_height // 100)


clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(bg, (0, 0))
    if not finish:
        player1.update_left()
        player2.update_right()
        ball.rand_movement()
        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(60)









