from pygame import *
mixer.init()
font.init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
bg = transform.scale(image.load('background.jpg'), (win_width, win_height))

mixer.music.load('bg_music.mp3')
mixer.music.set_volume(0.4)
mixer.music.play()
wall = mixer.Sound('wall.mp3')
platform = mixer.Sound('platform.mp3')
win = mixer.Sound('win_yaaaay.mp3')
win.set_volume(0.15)
true_win = mixer.Sound('absolute_win.mp3')

score_1 = 0
score_2 = 0

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
        self.weit = 0

    def rand_movement(self):
        global score_1, score_2        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= win_height - self.h:
            self.speed_y *= -1
            wall.play()
        if sprite.collide_rect(self, player1) or sprite.collide_rect(self, player2):
            if self.weit == 0:    
                self.speed_x *= -1
                platform.play()
                self.weit = 20
        if self.weit > 0:
            self.weit -= 1
        if self.rect.x <= 0:
            self.rect.x = win_width // 2
            self.rect.y = win_height // 2
            score_2 += 1
            self.speed_x *= -1
            win.play()
        if self.rect.x >= win_width - self.w:
            self.rect.x = win_width // 2
            self.rect.y = win_height // 2 
            score_1 += 1
            self.speed_x *= -1
            win.play()
            


player1 = Player('platform_left.png', win_width * 0.01, win_height // 2, win_width // 35, win_height // 5, win_height // 100)
player2 = Player('platform_right.png', win_width - win_width * 0.04, win_height // 2, win_width // 35, win_height // 5, win_height // 100)
ball = Ball('tennis_ball.png', win_width // 2, win_height // 2, win_width // 14, win_height // 10, win_height // 100)

font1 = font.Font(None, win_width // 15)
font2 = font.Font(None, win_width // 12)

clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(bg, (0, 0))
    if not finish:
        point1 = font1.render('Очки: ' + str(score_1), True, (255, 0, 0))
        window.blit(point1, (win_width // 70, win_height // 50)) 

        point2 = font1.render('Очки: ' + str(score_2), True, (0, 0, 255))
        window.blit(point2, (win_width - win_width // 6, win_height // 50))

        player1.update_left()
        player2.update_right()
        ball.rand_movement()
        player1.reset()
        player2.reset()
        ball.reset()

        if score_1 >= 5:
            win = font2.render('ПОБЕДИЛ ИГРОК СЛЕВА', True, (255, 0, 0))
            true_win.play()
            finish = True
        if score_2 >= 5:
            win = font2.render('ПОБЕДИЛ ИГРОК СПРАВА', True, (0, 0, 255))
            true_win.play()
            finish = True
    else:
        window.blit(win, (win_width // 10, win_height // 1.7))
         

    display.update()
    clock.tick(60)









