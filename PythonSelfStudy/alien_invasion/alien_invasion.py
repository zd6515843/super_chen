import sys
''' 玩家退出时我们将使用sys来退出游戏 '''

import pygame
''' pygame包含开发游戏所需要的功能 '''

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group



def run_game():
    ''' 初始化游戏并创建一个屏幕对象 '''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    ''' 创建一艘飞船 '''
    ship = Ship(ai_settings, screen)
    ''' 创建一个用于存储子弹的编组 '''
    bullets = Group()
    ''' 创建外星人的编组 '''
    # alien = Alien(ai_settings, screen)
    aliens = Group()

    ''' 创建外星人群 '''
    gf.create_fleet(ai_settings, screen,ship, aliens)

    ''' 开始游戏的主循环 '''
    while True:

        # gf.check_event(ship)
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
