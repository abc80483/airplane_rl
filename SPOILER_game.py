import pygame as pg,time

#建立飛機-------------------------------------------------------

class Ap(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("ap.png")  #飛機圖片
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((window.get_width() - self.rect.width)/2)  #起始位置
        self.rect.y = window.get_height() - self.rect.height - 30

    def update(self):  

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                print("left")
                self.rect.x -= 10
            elif event.key == pg.K_RIGHT:
                print("right")
                self.rect.x += 10
        #邊界

# 初始化
pg.init()
height, width= 600, 500
# 建立 window 視窗畫布，大小為 800x600
window = pg.display.set_mode((width, height))
# 設置視窗標題為 Hello World:)
pg.display.set_caption('酥酥飛機')

#建立畫布
bg = pg.Surface(window.get_size())
bg = bg.convert()
bg.fill((0,0,0))
allsprite = pg.sprite.Group()  #建立全部角色群組

ap = Ap()
allsprite.add(ap)   #加入全部角色群組


# 事件迴圈監聽事件，進行事件處理
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        else:
            window.blit(bg,(0,0))
            allsprite.draw(window)  #繪製所有角色
            ap.update()
            pg.display.update()
pg.quit()   