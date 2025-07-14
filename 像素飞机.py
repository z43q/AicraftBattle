import pygame as pg

HP = 100
# TODO: 添加攻击力
# TODO: 添加
STATE = 0
#0 飞行正常 1 飞机受损 2 飞机无敌 3 飞机开火
#飞机攻击模式
ATKSTATE = 0
#0 关火 1 普通子弹 2 导弹 3 激光
#敌机类型
KIND = 0
#1 普通飞机 2 中型飞机 3 大型飞机 4 巨型飞机 5 boss
#鼠标位置储存
x,y = 0,0

FPS = 60

pg.init()

#图片库
#玩家飞机
imgplayer = pg.image.load("player.png")
#玩家飞机受损
imgplayerhpdown = pg.image.load("playerhpdown.png")
#玩家飞机无敌
imgplayerinvincible = pg.image.load("playerinvincible.png")
#玩家飞机攻击
imgplayeratk = pg.image.load("playeratk.png")
#玩家子弹
imgplayerbullet1 = pg.image.load("playerbullet1.png")
#创建一个数组来存放子弹坐标
#玩家精灵组
#敌人精灵组1
#敌人精灵组2
#敌人精灵组3
#敌人精灵组4
#敌人精灵组5
#游戏帧率clock
clock = pg.time.Clock()
#鼠标位置实时跟踪
pg.display.set_caption("")
#窗口内隐藏光标
pg.mouse.set_visible(False)
#创建窗口
screen = pg.display.set_mode((600, 800))#窗口大小
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False#点击x退出
    screen.fill((0, 0, 0))#背景颜色 白
    pg.draw.rect(screen, (255, 255, 255), (0, 0, 600, 800))
    # #获取鼠标实时位置
    x,y = pg.mouse.get_pos()
    #鼠标事件
    #鼠标左键按下 玩家攻击
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:#1表示左键
            STATE = 3
            ATKSTATE = 1
    #显示玩家
    if STATE == 0:
        screen.blit(imgplayer, (x, y))
    elif STATE == 1:
        screen.blit(imgplayerhpdown, (x, y))
    elif STATE == 2:
        screen.blit(imgplayerinvincible, (x, y))
    elif STATE == 3:
        screen.blit(imgplayeratk, (x, y))
    #ATKSTATE = 0
    #子弹发射显示
    #if ATKSTATE == 1 :
    if ATKSTATE == 1:
        a,b = x,y
        while b > 0:
            screen.blit(imgplayerbullet1, (a, b-40))
            b-=10
    #pg.time.wait(500)
    print(x, y)
    #退出
    #恢复飞机状态
    STATE = 0
    ATKSTATE = 0
    #游戏帧率
    clock.tick(FPS)
    #更新显示
    pg.display.flip()
pygame.quit()