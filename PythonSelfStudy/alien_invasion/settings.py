class Settings():
    ''' 存储<<外星人入侵>>的所有设置的类 '''

    def __init__(self):
        ''' 初始化游戏设置 '''
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船速度设置
        self.ship_speed_factor = 1.5

        ''' 子弹设置 '''
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        ''' 外星人设置 '''
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        ''' fleet_direction为1表示向右移动, 为-1表示左移 '''
        self.fleet_direction = 1
