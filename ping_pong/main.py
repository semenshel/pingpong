from pygame import *
width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('Ping pong')

FPS = 60
clock = time.Clock()

game = True

fon = transform.scale(image.load('maxer.jpg'), (700, 500))



font.init()
font1 = font.SysFont('Arial', 50)
win = font1.render("Игра окончена!", True, (200, 10, 50))


mixer.init()
mixer.music.load('fon_music.mp3')
mixer.music.play()
#otbev = mixer.Sound('otbev.mp3')









class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y , player_speed_x, player_speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)





class Wall (sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, rect_x, rect_y, speed):
        super().__init__()
        self.color_1 = color_1
        self.color_3 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
















platform_1 = Wall(100, 60, 30, 10, 100, 50, 50, 5)
platform_2 = Wall(100, 90, 90, 10, 100, 650, 350, 5)

ball = GameSprite('ball_stal.png', 350, 250, 30, 30, 3, 3)




finish = False

while game == True:

    keys = key.get_pressed()
    


    for e in event.get():
        if e.type == QUIT:
            game = False


    

    if finish != True:
        window.blit(fon, (0, 0))

        platform_1.draw_wall()
        platform_2.draw_wall()
        ball.reset()
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y

        if ball.rect.y < 0:
            ball.speed_y *= -1
        if ball.rect.y > 475:
            ball.speed_y *= -1
        
        if ball.rect.x > 690:
            window.blit(win, (200, 200))
            finish = True
        if ball.rect.x < 10:
            window.blit(win, (200, 200))
            finish = True

        if ball.colliderect(platform_1.rect):
            #otbev.play()
            ball.speed_x -= 1.2
            ball.speed_x *= -1
            
        if ball.colliderect(platform_2.rect):
            #otbev.play()
            ball.speed_x += 1.2
            ball.speed_x *= -1
            
        

        

        

        if keys[K_w] and platform_1.rect.y > 0:
            platform_1.rect.y -= platform_1.speed
        if keys[K_s] and platform_1.rect.y < 400:
            platform_1.rect.y += platform_1.speed

        if keys[K_UP] and platform_2.rect.y > 0:
            platform_2.rect.y -= platform_2.speed
        if keys[K_DOWN] and platform_2.rect.y < 400:
            platform_2.rect.y += platform_2.speed

        




    
    
    clock.tick(FPS)
    display.update()