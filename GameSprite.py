
from pygame import *

class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x  , size_y , player_speed , width , height , window):
       super().__init__()
       self.window = window
       self.win_width = width
       self.win_height = height
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       self.window.blit(self.image, (self.rect.x, self.rect.y))
 