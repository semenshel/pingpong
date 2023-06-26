from pygame import *
from random import randint

#Основ. окно игры
win_width = 1000 #ширина
win_height = 800 #высота
window = display.set_mode((win_width, win_height))
display.set_caption('Try to dodge a brick')
background = transform.scale(image.load('background.png'), (win_width, win_height))

#Константы
run = True
finish = False
#clock = time.Clock()
life = 3
score = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100, 120))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Класс игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 1:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 900:
            self.rect.x += self.speedd

#Класс кирпича(врага)
class Brick(GameSprite):
    def update(self):
        self.rect.y += self.speed
        #Исчезновение при прикосновение границы экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

#Сам игрок
player = Player('player.png', 500, 680, 7, 80, 120)

#Кирпичи летят
bricks = sprite.Group()
for i in range(1, 4):
    brick = Brick('brick.png', randint(-5, win_width - 95), -140, randint(3, 6), 50, -40)
    bricks.add(brick)

#Текст
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
lose = font1.render('Get the L', True, (180, 0, 0))

#Музыка и звуки
mixer.init()
mixer.music.load('background_music.mp3')
mixer.music.play()
hit_sound = mixer.Sound('hit.mp3')

#Цикл игры
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0,0))

        #Очки
        '''text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        #Кол-во жизней
        text = font2.render("Кол-во жизней: " + str(life), 1, (255, 255, 255))
        window.blit(text, (10, 45))'''

        #Столкновение игрока с кирпичом
        if sprite.spritecollide(player, bricks, False): #or life <= 0
            finish = True
            window.blit(lose, (260, 200))
 
        #Обновление игрока и кирпича
        player.update()
        player.reset()
        bricks.update()
        bricks.draw(window)
        
    display.update()