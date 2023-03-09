from pygame import *                                                                           
from random import randint 
from time import time as t

WIN_SIZE = (700, 500)
SPRITE_SIZE = (50, 50)
FPS = 60
WHITE = (250, 250, 250)
timer = t()
DOWN = 1
LEFT = 2

window = display.set_mode(WIN_SIZE)
font.init()
font_lichik = font.Font(None, 18)
font_message = font.SysFont('Times New Roman', 70, True)

win = font_message.render('Win!', 1, WHITE)
lose = font_message.render('Lose...', 1, WHITE)


bullets = sprite.Group()

class Lichik():
    def __init__(self):
        self.lost_enemy = 0
        self.died_enemy = 0
    def show(self):
        self.lost_enemy_label = font_lichik.render('Пропущено:  ' + str(self.lost_enemy), 1, WHITE)
        self.kill_enemy_label = font_lichik.render('Знищено:  ' + str(self.died_enemy), 1, WHITE)
        window.blit(self.lost_enemy_label, (0, 0))
        window.blit(self.kill_enemy_label, (0, 35))
counter = Lichik()


class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x_pos, y_pos, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), SPRITE_SIZE)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos 
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y <= 0:
            self.kill()


class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WIN_SIZE[1] - SPRITE_SIZE[1]:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIN_SIZE[0] - SPRITE_SIZE[0]:
            self.rect.x += self.speed
    
    def fire(self):
        keys = key.get_pressed()
        global timer
            
        
        if keys[K_SPACE] and t() - timer > 0.1:
            bullets.add(Bullet('bullet.png', self.rect.x - 11, self.rect.y + 18, 4))
            
            timer = t()



class Enemy(GameSprite):
    def __init__(self, image_name, x_pos, y_pos, speed, direction):
        super().__init__(image_name, x_pos, y_pos, speed)
        self.direction = direction
    
    def update(self):
        if self.direction == DOWN:
            global lost_enemy
            if self.rect.y < WIN_SIZE[1]:
                self.rect.y += self.speed
            else:
                self.rect.y = 0
                self.rect.x = randint(0, WIN_SIZE[0] - SPRITE_SIZE[0])
                counter.lost_enemy += 1
        elif self.direction == LEFT:
            if self.rect.x > 0:
                self.rect.x -= self.speed    
            elif self.rect.x < WIN_SIZE[0]:
                self.rect.x = WIN_SIZE[0]
                self.rect.y = randint(0, WIN_SIZE[1] - (SPRITE_SIZE[1] * 2 - 20))

