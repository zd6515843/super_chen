import sys

import pygame
from bullet import Bullet
from alien import Alien

# def check_keydown_events(event, ship):


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    ''' 响应按键 '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fiire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

        # ''' 创建一颗子弹,并将其加入到编组bullets中 '''
        # if len(bullets) < ai_settings.bullet_allowed:
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)


def fiire_bullet(ai_settings, screen, ship, bullets):
    ''' 如果还没有到达限制，就发射一颗子弹 '''
    ''' 创建一颗子弹,并将其加入到编组bullets中 '''
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    ''' 响应按键 '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

# def check_event(ship):


def check_event(ai_settings, screen, ship, bullets):
    ''' 响应按键和鼠标事件 '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # check_keydown_events(event, ship)
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

# def update_screen(ai_settings, screen, ship):


def update_screen(ai_settings, screen, ship, alien, bullets):
    ''' 重绘屏幕背景色 '''
    screen.fill(ai_settings.bg_color)

    ''' 在飞船和外星人后面重绘所有子弹 '''
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.draw(screen)
    # alien.blitme()

    ''' 让最新绘制的屏幕可见 '''
    pygame.display.flip()


def update_bullets(aliens, bullets):
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中了外星人 并删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)



def get_number_aliens_x(ai_settings, alien_width):
    ''' 计算一行可容纳多少个外星人 '''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    ''' 计算屏幕能容纳多少行外星人 '''
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    ''' 创建一个外星人并将其放在当前行 '''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    ''' 创建外星人群 '''
    ''' 创建一个外星人，并计算一行可容纳多少个外星人 '''
    ''' 外星人间距为外星人的宽度 '''
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    ''' 创建外星人群 '''
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    ''' 有外星人到达边缘时采取相应措施 '''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    ''' 将所有外星人向下移动，并改变他们的方向 '''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    ''' 检查是否有外星人位于屏幕边缘并更新所有外星人的位置 '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
