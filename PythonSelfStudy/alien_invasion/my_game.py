import sys
import os
import pygame

def run_game():
    ''' 初始化 '''
    pygame.init()

    ''' 设置屏幕大小 '''
    screen = pygame.display.set_mode((600,400))

    ''' 设置屏幕的title '''
    pygame.display.set_caption("This is my test game!!")

    screen.fill((230,230,230))

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(THIS_FOLDER, 'images/ship.bmp')
    ship = pygame.image.load(filename)

    screen_rect = screen.get_rect()
    image_rect = ship.get_rect()
    
    image_rect.centerx = screen_rect.centerx
    image_rect.bottom = screen_rect.bottom

    ''' 在指定位置绘制飞船 '''
    screen.blit(ship,image_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ''' 让最新绘制的屏幕可见 '''
        pygame.display.flip()

run_game()