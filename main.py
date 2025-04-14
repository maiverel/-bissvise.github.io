import pygame
import math
from movement import movement

#Начало и размер окна
pygame.init()
DISPLAY_W, DISPLAY_H = 1800, 900
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
clock = pygame.time.Clock()

############## Объекты игры #############
objs = []
hud = [movement.Message(["тест"], 900, 800, False)]

hud_tutorial = [
    movement.Message(["52"], 900, 800, False),
    movement.Message(["Картина"], 4345, -330, False, False)
]

hud_1 = [
    movement.Message(["Видимо, рычаг сломан"], 4100, 287, False, False),
    movement.lockHud(6600, -300, "Ответ", "42")
]

hud_blya = [ 
    movement.Message(["КАРТИНКА", "НОМЕР РАЗ"], 950, -300, False, False), 
    movement.Message(["КАРТИНКА НОМЕР ДВА"], 1850, -400, False, False), 
    movement.Message(["КАРТИНКА НОМЕР ТРИ"], 2025, 400, False, False), 
    movement.Message(["КАРТИНКА НОМЕР ЧЕТЫРЕ"],-225, 550, False, False), 
    movement.Message(["КАРТИНКА НОМЕР ПЯТЬ"], -700, 1200, False, False), 
    movement.lockHud(6600, -300, "Ответ", "42") 
] 
 
hud_suka = [ 
    movement.Message(["КАРТИНКА НОМЕР РАЗ"], 1300, -400, False, False), 
    movement.Message(["КАРТИНКА НОМЕР ДВА"], 900, -700, False, False), 
    movement.Message(["КАРТИНКА НОМЕР ТРИ"], 580, -150, False, False), 
    movement.lockHud(6600, -300, "Ответ", "42") 
] 

scene_test_objs = [
    movement.Sprite("azure4", 400, 500, 600, 50, True, True), #0
    movement.Sprite("azure4", 400, 350, 50, 300, True, True), #1
    movement.Sprite("azure3", 300, 400, 50, 50, True, True),  #2
    movement.Sprite("azure3", 150, 300, 50, 50, True, True),  #3
    movement.Sprite("azure3", 300, 150, 50, 50, True, True),  #4
    movement.Sprite("azure3", 500, 400, 50, 50, True, True),  #5
    movement.Sprite("azure3", 650, 300, 50, 50, True, True),  #6
    movement.Sprite("azure3", 500, 150, 50, 50, True, True),  #7
    movement.Sprite("azure4", 1000, 500, 600, 50, True, True),#8
    movement.Door("azure2", 1000, 325, 1000, 100, 50, 300),   #9
    movement.Lever("azure2", 900, 462, 50, 25, 850, 425, 150, 100, True),#10
    movement.Sprite("azure4", -100, 500, 600, 50, True, True), #11
    movement.Sprite("azure4", 1000, 200, 300, 50, True, True), #12
]

scene_tutorial_objs = [
    movement.Sprite("azure4", 400, 700, 1000, 500, True, True), #пол
    movement.Sprite("azure4", -600, 700, 1000, 500, True, True), #пол справа
    movement.Door("azure3", -150, 300, -150, 10, 50, 300), #Дверь
    movement.Sprite("azure4", -600, -100, 1000, 500, True, True), #потолок слева
    movement.Sprite("azure4", 1150, -400, 3500, 500, True, True), #потолок
    movement.Sprite("azure4", 4150, -900, 4500, 500, True, True), #потолок справа
    movement.Sprite("azure4", 900, 1200, 2000, 500, True, True), #0
    movement.Sprite("azure4", 2900, 950, 2000, 1000, True, True), #пол справа
    movement.Sprite("azure4", 4900, 1200, 2000, 2500, True, True), #пол справа справа
    movement.Door("azure3", 2300, 300, 2300, 10, 50, 300), #дверь справа
    movement.Sprite("azure4", 2300, 0, 80, 300, True, True), #стена справа
    movement.Trigger(2125, 150, 300, 600, False), #триггер и сообщение справа 11
    movement.Door("azure3", 4800, -200, 4800, -490, 50, 300), #дверь справа справа
    movement.Sprite("azure4", 4800, -500, 80, 300, True, True), #стена справа справа
    movement.Lever("azure3", 4600, -63, 50, 25, 4575, -125, 200, 150, False), #рычаг справа справа
    movement.Sprite("azure4", 6900, 600, 1000, 3500, True, True), #стена конец
    movement.Sprite("azure4", 6150, 2325, 500, 50, True, True), #пол конец
    movement.Trigger(6150, 2050, 500, 500, False), #триггер конец
    movement.Trigger(600, 150, 50, 600, False), #сообщение начало
    movement.Trigger(1400, 925, 1000, 50, False), #сообщение яма
    movement.Trigger(2950, 150, 100, 600, False), #сообщение стена
    movement.Trigger(4100, -350, 150, 600, False), #сообщение рычаг
    movement.Trigger(5600, -350, 150, 600, False), #сообщение slam
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 4345, -180, 60, 60, 4325, -175, 200, 250, False), #картина
    movement.Trigger(-450, 300, 200, 300, False),
    #movement.Sprite("seagreen", 400, 300, 50, 172, False, True), #0
    #movement.Sprite("seagreen", 0, 0, 50, 50, False, True), #0
    movement.Sprite("azure4", -850, -500, 500, 300, True, True),
    movement.Sprite("azure4", -1850, 700, 1500, 500, True, True),   
    movement.Sprite("azure4", -2075, -350, 1050, 1600, True, True), 
    movement.Sprite("azure4", -600, -900, 1000, 500, True, True),   
    movement.Sprite("azure4", -2075, -2000, 1050, 1700, True, True),
    movement.Sprite("azure4", -600, -2000, 1000, 1700, True, True),
]

scene_1_objs = [
    movement.Sprite("azure4", 400, 700, 1000, 500, True, True), #пол
    movement.Sprite("azure4", -850, 700, 1500, 500, True, True), #пол слева
    movement.Door("azure2", -150, 300, -150, 10, 50, 300), #дверь начало
    movement.Sprite("azure4", -600, -1300, 1000, 2900, True, True), #потолок слева
    movement.Sprite("azure4", 1150, -400, 3500, 500, True, True), #потолок
    movement.Sprite("azure4", 5150, -700, 4500, 500, True, True), #потолок справа             
    movement.Sprite("azure2", 1900, 1200, 4000, 500, True, True), #0
    movement.Sprite("azure4", 4900, 950, 2000, 1000, True, True), #пол справа
    movement.Sprite("azure4", 6900, 1200, 2000, 2500, True, True), #пол справа справа
    movement.Door("azure3", 4300, 300, 4300, 10, 50, 300), #дверь  справа
    movement.Sprite("azure4", 4300, 0, 80, 300, True, True), #стена справа
    movement.Door("azure3", 6800, -200, 6800, -490, 50, 300), #дверь справа справа
    movement.Sprite("azure4", 6800, -500, 80, 300, True, True), #стена справа справа
    movement.Lever("azure3", 4100, 437, 50, 25, 4100, 375, 150, 150, False), #рычаг справа справа
    movement.Sprite("azure4", 8850, 600, 1000, 3500, True, True), #стена конец
    movement.Sprite("azure4", 8150, 2325, 500, 50, True, True), #пол конец
    movement.Sprite("azure2", 1500, 600, 100,50, True, True),
    movement.Sprite("azure2", 2200, 600, 100,50, True, True),
    movement.Sprite("azure2", 2900, 600, 100,50, True, True),
    movement.Sprite("azure2", 4600, 0, 100,50, True, True),
    movement.Lever("azure3", 6600, -150, 40, 60, 6600, -150, 100, 100, False), #рычаг справа справа
    movement.Sprite("azure4", -2100, -800, 1000, 3500, True, True), #cтена слева начало
    movement.Trigger(-500, 300, 300, 300, False), #Триггер начало
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 1500, 445, 60, 60, 1500, 450, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 2200, 445, 60, 60, 2200, 450, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 2900, 445, 60, 60, 2900, 450, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 150, 245, 60, 60, 150, 250, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 550, 245, 60, 60, 550, 250, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 4500, 295, 60, 60, 4500, 300, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 4600, -130, 60, 60, 4600, -125, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 4800, 295, 60, 60, 4800, 300, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 5200, 295, 60, 60, 5200, 300, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 5600, 295, 60, 60, 5600, 300, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 6350, -180, 60, 60, 6350, -175, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 7000, -180, 60, 60, 7000, -175, 100, 100, False),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 7300, -180, 60, 60, 7300, -175, 100, 100, False),
    movement.Trigger(8150, 1850, 500, 900, False) # Переход
]

scene_2_objs = [
    movement.Sprite("azure4", 400, 500, 600, 50, True, True), #0
    movement.Sprite("azure4", 400, 350, 50, 300, True, True), #1

    movement.Sprite("azure3", 300, 400, 50, 50, True, True),  #2
    movement.Sprite("azure3", 125, 325, 50, 50, True, True),  #3
    movement.Sprite("azure3", 300, 150, 50, 50, True, True),  #4

    movement.Sprite("azure3", 500, 400, 50, 50, True, True),  #5
    movement.Sprite("azure3", 650, 325, 50, 50, True, True),  #6
    movement.Sprite("azure3", 500, 1500, 50, 50, True, True),  #7

    movement.Sprite("azure4", 1000, 500, 600, 50, True, True),#8
    movement.Door("azure2", 1000, 325, 1000, 100, 50, 300),   #9
    movement.Lever("azure3", 1000, 462, 50, 25, 1000, 425, 200, 100, True),#10
    
    movement.Sprite("azure2", 600, 200, 1000, 50, True, True), #11
    movement.Sprite("azure2", 800, 100, 50, 50, True, True), #12

    movement.Lever("azure2", 650, 275, 50, 25, 650, 275, 50, 50, True),#13

    movement.Lever("azure2", 125, 275, 50, 25, 125, 275, 50, 50, True),#13
]

scene_3_objs = [
    movement.Sprite("azure4", 400, 700, 1000, 500, True, True), #пол
    movement.Sprite("azure4", -600, 700, 1000, 500, True, True), #пол справа
    movement.Sprite("azure4", -600, -100, 1000, 500, True, True), #потолок слева
    movement.Sprite("azure2", -150, 300, 50, 300, True, True), #0
    movement.Sprite("azure4", 1150, -400, 3500, 500, True, True), #потолок
    movement.Sprite("azure4", 5150, -700, 4500, 500, True, True), #потолок справа
    movement.Sprite("azure2", 1900, 1200, 4000, 500, True, True), #0
    movement.Sprite("azure4", 4900, 950, 2000, 1000, True, True), #пол справа
    movement.Sprite("azure4", 6900, 1200, 2000, 2500, True, True), #пол справа справа
    movement.Door("azure3", 4300, 300, 4300, 10, 50, 300), #дверь справа
    movement.Sprite("azure4", 4300, -300, 80, 900, True, True), #стена справа
    movement.Trigger(4125, 150, 300, 600, True), #триггер и сообщение справа 11
    movement.Door("azure3", 6800, -200, 6800, -490, 50, 300), #дверь справа справа
    movement.Sprite("azure4", 6800, -500, 80, 300, True, True), #стена справа справа
    movement.Lever("azure3", 6600, -63, 50, 25, 6600, -125, 150, 150, True), #рычаг справа справа
    movement.Sprite("azure4", 8650, 600, 500, 3500, True, True), #стена конец
    movement.Sprite("azure4", 8150, 2325, 500, 50, True, True), #пол конец
    movement.Trigger(8150, 2050, 500, 500, True), #триггер конец
    movement.Trigger(700, 150, 50, 600, True), #сообщение начало
    movement.Trigger(2400, 925, 3000, 50, True), #сообщение яма
    movement.Trigger(4950, 150, 100, 600, True), #сообщение стена
    movement.Trigger(6100, -350, 150, 600, True), #сообщение рычаг
    movement.Trigger(7600, -350, 150, 600, True), #сообщение slam

    movement.Sprite("azure2", 1500, 600, 100,50, True, True),
    movement.Sprite("azure2", 2200, 600, 100,50, True, True),
    movement.Sprite("azure2", 2900, 600, 100,50, True, True),
    movement.Sprite("azure2", 4600, 0, 100,50, True, True),
    movement.Sprite("seagreen", 400, 300, 50, 172, False, True), #0

    #картины
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 1500, 445, 60, 60, 1500, 450, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 2200, 445, 60, 60, 2200, 450, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 2900, 445, 60, 60, 2900, 450, 100, 100, True),

    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 150, 245, 60, 60, 150, 250, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 550, 245, 60, 60, 550, 250, 100, 100, True),


    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 4500, 295, 60, 60, 4500, 300, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 4600, -130, 60, 60, 4600, -125, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 4800, 295, 60, 60, 4800, 300, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 5200, 295, 60, 60, 5200, 300, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 5600, 295, 60, 60, 5600, 300, 100, 100, True),

    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 6350, -180, 60, 60, 6350, -175, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 7000, -180, 60, 60, 7000, -175, 100, 100, True),
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 7300, -180, 60, 60, 7300, -175, 100, 100, True),
]

scene_blya_objs = [ 
    movement.Door("azure2", 150, -100, 50, 300, 50, 300),  
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 950, -300, 60, 60, 950, -300, 250, 250, True), 
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 1850, -400, 60, 60, 1850, -400, 250, 250, True),   
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 2025, 400, 60, 60, 2025, 400, 250, 250, True),  
    # 0 этаж 
    movement.Sprite("azure4", 400, 200, 800, 300, True, True), #1st slice 
    movement.Sprite("azure4", 1500, 200, 800, 300, True, True), #2nd slice 
    movement.Sprite("azure4", 0, 20, 50, 1100, True, True), #left border 
    movement.Sprite("azure4", 1900, -150, 50, 1550, True, True), #right border 
    movement.Sprite("azure4", 2025, 600, 250, 50, True, True), #mini right platform outide 
    movement.Sprite("azure4", 1860, 50, 120, 400, True, True), #ladder 
    movement.Sprite("azure4", 800, 100, 50, 500, True, True), #portal   
    movement.Sprite("azure4", 1100, 100, 50, 500, True, True), #portal 
 
    movement.Door("azure2", 3950, 800, 50, 300, 50, 300), 
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), -225, 550, 60, 60, -225, 550, 250, 250, True),   
    # -1 пониже 
    movement.Sprite("azure4", 700, 1300, 2000, 300, True, True),#slice 
    movement.Sprite("azure4", 375, 1200, 150, 300, True, True), #1st left colon 
    movement.Sprite("azure4", 75, 1100, 150, 300, True, True), #2nd left colon 
    movement.Sprite("azure4", -225, 1000, 150, 300, True, True), #3rd left colon 
    movement.Sprite("azure4", 2000, 1300, 70, 300, True, True), #1st right colon 
    movement.Sprite("azure4", 2300, 1300, 70, 300, True, True), #2nd right colon 
    movement.Sprite("azure4", 2600, 1300, 70, 300, True, True), #3rd right colon 
    movement.Sprite("azure4", 3300, 1300, 700, 300, True, True), #upper right platform 
    movement.Sprite("azure4", 3650, 1100, 700, 300, True, True), #up-upper right platform  
 
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), -700, 1200, 60, 60, -700, 1200, 250, 250, True),  
    # пристройка левая к -1 этажу 
    movement.Sprite("azure4", 100, 1500, 2000, 300, True, True), #slice 
    movement.Sprite("azure4", -900, 1500, 50, 2100, True, True), #left border=

    movement.Sprite("azure4", -100, -2150, 1100, 2000, True, True),
    movement.Sprite("azure4", 1500, -2150, 1200, 2000, True, True),

    movement.Trigger(5325, 800, 150, 300, False), #Переход
    movement.Sprite("azure4", 4950, 175, 3300, 950, True, True),
    movement.Sprite("azure4", 4950, 1350, 3300, 800, True, True),
] 

scene_suka_objs = [ 
    movement.Door("azure2", 0, -720, 50, 300, 50, 300), 
    movement.Door("azure2", 0, -100, 50, 300, 50, 300),  
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 1300, -400, 60, 60, 1300, -400, 250, 250, True), 
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 900, -700, 60, 60, 900, -700, 250, 250, True),   
    movement.Lever(pygame.image.load("movement/sprites/60x60/картина3.png"), 580, -150, 60, 60, 580, -150, 250, 250, True),  
    # 0 этаж 
    movement.Sprite("azure4", 550, 200, 1600, 300, True, True), #slice 
    movement.Sprite("azure4", -230, -750, 50, 1000, True, True), #left border 
    movement.Sprite("azure4", 1400, -150, 50, 1550, True, True), #right border 
    movement.Sprite("azure4", 1300, 100, 150, 500, True, True), #1st block 
    movement.Sprite("azure4", 1050, -300, 150, 100, True, True), #2nd block 
    movement.Sprite("azure4", 1050, -300, 150, 100, True, True), #2nd block 
    movement.Sprite("azure4", 900, -400, 150, 100, True, True), #3rd block 
    movement.Sprite("azure4", 750, -500, 150, 100, True, True), #4th block 
    movement.Sprite("azure4", 210, -600, 930, 100, True, True), #5th block 
    
    movement.Sprite("azure4", -1275, 425, 2050, 750, True, True),
    movement.Sprite("azure4", -1275, -700, 2050, 900, True, True),
    movement.Sprite("azure2", -2265, -100, 50, 300, True, True),
] 

scene_test = movement.Scene("test",scene_test_objs, 250, -100, hud)
scene_tutorial = movement.Scene("tutorial",scene_tutorial_objs, -1325, -2025, hud_tutorial)
scene_1 = movement.Scene("1",scene_1_objs, -1325, -1300, hud_1)
scene_2 = movement.Scene("2",scene_2_objs, 250, -100, hud)
scene_3 = movement.Scene("3",scene_3_objs, 400, 300, hud)
scene_blya = movement.Scene("blya",scene_blya_objs, 675, -2350, hud_blya) 
scene_suka = movement.Scene("suka",scene_suka_objs, -1250, -50, hud_suka) 


#Игрок, сцена и смещение камеры


scene = scene_tutorial
player = movement.Player("seagreen", scene.x, scene.y, scene.objs)
current_scene = scene.name
objs = scene.objs
hud = scene.hud
player.sounds[7].set_volume(0.2)

scroll_x = player.rect.x
scroll_y = player.rect.y
scroll = 0
fbj = 0
editor = False
new_block = False
new_count = 0
step = 50
new_obj = None
cursor = movement.Sprite("seagreen", 0, 0, step, step, False, True)
cursor_img = pygame.image.load("movement/sprites/cursor.png")
cur_pos = (0, 0)

done = False

############# Цикл игры ##############
while not done:
    ########### Инпуты ###########
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT  and player.jumps > 1:
                if player.vel[0] == 0: break

                if player.vel[0] > 0:
                    player.vel = (16, -2)
                if player.vel[0] < 0:
                    player.vel = (-16, -2)
                player.jumps -= 1
                player.sounds[1].play()
            
            if (event.key == pygame.K_s or event.key == pygame.K_LCTRL) and not player.grounded:
                if player.vel[1] < 15: player.vel = (0, 15)
                player.slaming = True
    
            if current_scene == "test":
                if event.key == pygame.K_f and objs[10].triggered:
                    objs[9].switch()
            
            if current_scene == "tutorial":
                if event.key == pygame.K_f and objs[14].triggered and not objs[14].locked:
                    objs[12].open()
                    objs[14].locked = True
                if event.key == pygame.K_f and objs[23].triggered and not hud[1].active and not objs[23].locked:
                    player.sounds[8].play()
                    hud[1].active = True
                    objs[23].locked = True
            
            if current_scene == "1":
                if event.key == pygame.K_f and objs[13].triggered and not objs[13].locked:
                    hud[0].active = True
                    player.sounds[8].play()
                    objs[13].locked = True
                
                if event.key == pygame.K_f and objs[20].triggered and not objs[20].locked:
                    if hud[1].active:
                        if hud[1].input == hud[1].answer:
                            objs[11].open()
                            hud[1].active = False
                            objs[20].locked = True
                        else:
                            hud[1].sounds[0].play()
                    else: 
                        hud[1].active = True
                        player.sounds[8].play()
                    
                if hud[1].active and objs[20].triggered:
                    if event.key == pygame.K_BACKSPACE:
                        hud[1].errase()
                    elif 48 <= event.key <= 57:
                        hud[1].add(str(event.key - 48))

            if current_scene == "blya": 
                if event.key == pygame.K_f and objs[1].triggered and not hud[0].active and not objs[1].locked: 
                    player.sounds[8].play() 
                    hud[0].active = True 
                    objs[1].locked = True 
                if event.key == pygame.K_f and objs[2].triggered and not hud[1].active and not objs[2].locked: 
                    player.sounds[8].play() 
                    hud[1].active = True 
                    objs[2].locked = True 
                if event.key == pygame.K_f and objs[3].triggered and not hud[2].active and not objs[3].locked: 
                    player.sounds[8].play() 
                    hud[2].active = True 
                    objs[3].locked = True 
                if event.key == pygame.K_f and objs[13].triggered and not hud[3].active and not objs[13].locked: 
                    player.sounds[8].play() 
                    hud[3].active = True 
                    objs[13].locked = True 
                if event.key == pygame.K_f and objs[23].triggered and not hud[4].active and not objs[23].locked: 
                    player.sounds[8].play() 
                    hud[4].active = True 
                    objs[23].locked = True 
             
            if current_scene == "suka": 
                if event.key == pygame.K_f and objs[2].triggered and not hud[0].active and not objs[2].locked: 
                    player.sounds[8].play() 
                    hud[0].active = True 
                    objs[2].locked = True 
                if event.key == pygame.K_f and objs[3].triggered and not hud[1].active and not objs[3].locked: 
                    player.sounds[8].play() 
                    hud[1].active = True 
                    objs[3].locked = True 
                if event.key == pygame.K_f and objs[4].triggered and not hud[2].active and not objs[4].locked: 
                    player.sounds[8].play() 
                    hud[2].active = True 
                    objs[4].locked = True 
            
            if event.key == pygame.K_r:
                    player.reset(scene.x, scene.y, scene.objs, True, scroll_x, scroll_y)
                    scroll_x = player.rect.x
                    scroll_y = player.rect.y
                    current_scene = scene.name
                    objs = scene.objs
                    hud = scene.hud
            
            if event.key == pygame.K_KP_MULTIPLY:
                editor = not editor

            if event.key == pygame.K_z and editor and new_count:
                objs = objs[:-1]
                player.colliders = objs
                player.sounds[9].play()
                new_count -= 1

            if event.key == pygame.K_n and editor:
                player.noclip = not player.noclip
                player.vel = (0, 0)
                player.grounded = False
            
            if event.key == pygame.K_LEFTBRACKET and editor and step > 1: step /= 2
            if event.key == pygame.K_RIGHTBRACKET and editor: step *= 2
                

            if event.key == pygame.K_m and editor and new_count:
                print("Export begin")
                for i in range(new_count):
                    print('movement.Sprite("azure4", ',int(objs[-new_count + i].rect.x + int(objs[-new_count + i].size_x) / 2),', ',int(objs[-new_count + i].rect.y + int(objs[-new_count + i].size_y) / 2),', ', int(objs[-new_count + i].size_x),', ', int(objs[-new_count + i].size_y),', True, True),', sep ='')
                print("Export end")

        if editor:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_block = True
                    new_pos = ((event.pos[0] + scroll_x - 875) // step * step, (event.pos[1] + scroll_y - 375) // step * step)
                    new_obj = movement.Sprite("azure4", event.pos[0] + scroll_x - 875, event.pos[1] + scroll_y - 375, 0, 0, False, True)
                    objs.append(new_obj)

            if event.type == pygame.MOUSEMOTION:
                if new_block:
                    pos = ((event.pos[0] + scroll_x - 875) // step * step, (event.pos[1] + scroll_y - 375) // step * step)
                    x, y = new_pos[0], new_pos[1]
                    width = pos[0] - new_pos[0]
                    height = pos[1] - new_pos[1]
                    w, h = width, height
                    if w < 0:
                        w = -w
                        x = x - w
                    if h < 0:
                        h = -h
                        y = y - h
                    new_obj.rect.x = x  // step * step
                    new_obj.rect.y = y  // step * step
                    new_obj.size_x = w  // step * step
                    new_obj.size_y = h  // step * step
                    new_obj.rect.size = (w  // step * step, h // step * step)
                    new_obj.image = pygame.Surface((w  // step * step, h // step * step)).convert_alpha()
                    new_obj.image.fill((0,255,0,100))
                cursor.rect.x = (event.pos[0] + scroll_x - 875) // step * step
                cursor.rect.y = (event.pos[1] + scroll_y - 375) // step * step - step
                cur_pos = (cursor.rect.x, cursor.rect.y + step)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if new_obj.rect.size[0] * new_obj.rect.size[1] == 0:
                        objs = objs[:-1]
                        player.colliders = objs
                        new_block = False
                        new_obj = None
                    else:
                        new_obj.image.fill("azure4")
                        new_obj.collision = True
                        new_count += 1
                        new_block = False
                        print(new_obj.rect.x + int(new_obj.size_x) / 2, new_obj.rect.y + int(new_obj.size_y) / 2, new_obj.size_x, new_obj.size_y)
                        new_obj = None
                
    if current_scene == "tutorial":
        if objs[11].triggered:
            if not objs[9].opened:
                objs[9].open()
                player.sounds[8].play()
                hud[0].change(["Рывок тратит одну выносливость"])

        mes = ["Нажмите SHIFT для рывка"]
        if objs[18].triggered and not hud[0].message == mes:
            player.sounds[8].play()
            hud[0].change(mes)
            hud[0].active = True
        
        mes = ["Нажмите R чтобы вернутся в начало"]
        if objs[19].triggered and not hud[0].message == mes:
            hud[0].active = True
            player.sounds[8].play()
            hud[0].change(mes)

        mes = ["Нажимайте CTRL в прыжке, после чего","прыгайте сразу после приземления,","так вы будете набирать высоту"]
        if objs[20].triggered and not hud[0].message == mes:
            hud[0].active = True
            player.sounds[8].play()
            hud[0].change(mes)
        
        mes = ["Нажмите F чтобы взаимодействовать с объектами"]
        if objs[21].triggered and not hud[0].message == mes:
            hud[0].active = True
            player.sounds[8].play()
            hud[0].change(mes)

        mes = ["Нажмите CTRL для ускоренного падения"]
        if objs[22].triggered and not hud[0].message == mes:
            hud[0].active = True
            player.sounds[8].play()
            hud[0].change(mes)

        if objs[17].triggered and objs[17].active:
            scene = scene_1
            scroll_x -= 7500
            scroll_y += scene.y - player.rect.y - 86
            player.reset(player.rect.x - 7500 + 25, scene.y, scene.objs, False, scroll_x, scroll_y)
            current_scene = scene.name
            objs = scene.objs
            hud = scene.hud

        if objs[24].triggered and objs[24].active:
            objs[2].open()
            objs[24].active = False
    
    if current_scene == "1":
        if objs[22].triggered:
            if not objs[2].opened:
                objs[2].open()
        if objs[36].triggered and objs[36].active:
            scene = scene_blya
            scroll_x -= 7450
            scroll_y += scene.y - player.rect.y - 86
            player.reset(player.rect.x - 7450 + 25, scene.y, scene.objs, False, scroll_x, scroll_y)
            current_scene = scene.name
            objs = scene.objs
            hud = scene.hud
    
    if current_scene == "blya":
        if objs[28].triggered and objs[28].active:
            scene = scene_suka
            scroll_x += scene.x - player.rect.x - 25
            scroll_y -= 900
            player.reset(scene.x, player.rect.y - 900 + 86, scene.objs, False, scroll_x, scroll_y)
            current_scene = scene.name
            objs = scene.objs
            hud = scene.hud
    
    pressed = pygame.key.get_pressed()
    
    if (pressed[pygame.K_w] or pressed[pygame.K_SPACE]):
        fbj += 1
        if player.grounded:
            if fbj < 10:
                player.vel = (player.vel[0], player.jump_power - (player.slam_storage / 5))
                player.slam_storage = 0
                player.sounds[0].play()
    else:
        fbj = 0

    #Горизонталь
    if pressed[pygame.K_a] and player.vel[0] >= -5 and not player.slaming: player.vel = (-5 - 0.5, player.vel[1])
    if pressed[pygame.K_d] and player.vel[0] <= 5 and not player.slaming: player.vel = (5 + 0.5, player.vel[1])
    if (pressed[pygame.K_d] or pressed[pygame.K_a]) and player.grounded and abs(player.vel[0]) > 3: player.sounds[3].set_volume(0.3)
    else: player.sounds[3].set_volume(0)
    #Стрелочки
    if pressed[pygame.K_UP]: scroll_y -= 30
    if pressed[pygame.K_DOWN]: scroll_y += 30
    if pressed[pygame.K_LEFT]: scroll_x -= 30
    if pressed[pygame.K_RIGHT]: scroll_x += 30
    #Ноуклип
    if player.noclip:
        if pressed[pygame.K_w]: player.rect.move_ip(0, -20)
        if pressed[pygame.K_s]: player.rect.move_ip(0, 20)
        if pressed[pygame.K_a]: player.rect.move_ip(-20, 0)
        if pressed[pygame.K_d]: player.rect.move_ip(20, 0)
    #Смещение камеры
    dealta_time = clock.tick(60)
    scroll += 1
    scroll_x += dealta_time/100
    scroll_y += dealta_time/100
    ########### Отображение спрайтов ##########
    screen.fill((50, 50, 50))
    for i in range(len(objs)):
        objs[i].draw(screen, scroll_x, scroll_y)
        objs[i].update()

    player.draw(screen, scroll_x, scroll_y)
    player.update(scroll_x, scroll_y)

    if hud:
        for i in range(len(hud)):
            hud[i].draw(screen, scroll_x, scroll_y)
            text = f"{clock.get_fps():2.0f}"
            screen.blit(pygame.font.Font("movement/fonts/ultrakall.ttf", 24).render(text, False, (255, 255, 255)),(0,0))

    if editor:
        if new_obj:
            if new_obj.image.get_size()[0] > 8 and new_obj.image.get_size()[1] > 8:
                inner_box = pygame.Surface((new_obj.image.get_size()[0] - 8, new_obj.image.get_size()[1] - 8)).convert_alpha()
                inner_box.fill((0, 0, 0, 100))
                screen.blit(inner_box, (new_obj.rect.x - scroll_x + 875 + 4, new_obj.rect.y - scroll_y + 375 + 4))
                text_x = pygame.font.Font("movement/fonts/ultrakall.ttf", 24).render(str(new_obj.image.get_size()[0]), False, (255, 255, 255))
                text_y = pygame.font.Font("movement/fonts/ultrakall.ttf", 24).render(str(new_obj.image.get_size()[1]), False, (255, 255, 255))
                screen.blit(text_x, (new_obj.rect.x - scroll_x + 875 + (new_obj.image.get_size()[0] / 2) - (text_x.get_rect().size[0] / 2), new_obj.rect.y - scroll_y + 375 + new_obj.image.get_size()[1] + 12))
                screen.blit(pygame.transform.rotate(text_y, 90), (new_obj.rect.x - scroll_x + 875 - 24, new_obj.rect.y - scroll_y + 375 + (new_obj.image.get_size()[1] / 2)  - (text_x.get_rect().size[0] / 2)))
                pos_text = pygame.font.Font("movement/fonts/ultrakall.ttf", 20).render(str((new_obj.rect.x + new_obj.rect.size[0] / 2, new_obj.rect.y + new_obj.rect.size[1] / 2)), False, (255, 255, 255))
                screen.blit(pos_text, (new_obj.rect.x - scroll_x + 875 + new_obj.rect.size[0] / 2 - pos_text.get_size()[0] / 2, new_obj.rect.y - scroll_y + 375 + new_obj.rect.size[1] / 2 - pos_text.get_size()[1] / 2))
        cursor_img_scaled = pygame.transform.rotate(cursor_img, scroll)
        screen.blit(cursor_img_scaled, (cur_pos[0] - scroll_x + 875 - (cursor_img_scaled.get_size()[0] / 2), cur_pos[1] - scroll_y + 375 - (cursor_img_scaled.get_size()[1] / 2)))
        step_text = pygame.font.Font("movement/fonts/ultrakall.ttf", 20).render(str(step), False, (255, 255, 255))
        screen.blit(step_text, (cur_pos[0] - scroll_x + 875 - (cursor_img_scaled.get_size()[0] / 2) + 20, cur_pos[1] - scroll_y + 375 - (cursor_img_scaled.get_size()[1] / 2)))

    if player.rect.x - scroll_x != 0:
        scroll_x += (player.rect.x - scroll_x)/10
    if player.rect.y - scroll_y != 0:
        scroll_y += (player.rect.y - scroll_y)/10
    
    pygame.display.flip()
