import pygame
from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, w, h):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

menu_bg = GameSprite('images\picture 800 x 8 4f5795c0-6a9e-41f5-bba1-06ec9ba43fd5.png',0,0,0,800,800)
btn_play = GameSprite('images\start-button.png',400, 390, 0, 100, 60)

btn_menu = GameSprite('images\free-icon-menu-5949637.png',)

def menu():
    menu_bg.reset()
    
FPS = 60 #змінна,яка відровідає за частоту кадрів
clock= time.Clock() #змінна часу

for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = True






display.update() #обновлення події дисплею
clock.tick(FPS) #встановлення частоти кадрів