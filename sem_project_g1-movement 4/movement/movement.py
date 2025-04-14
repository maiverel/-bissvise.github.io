import pygame

#Класс игрока
class Player(pygame.sprite.Sprite):
    #Назначаем начальные переменные
    def __init__(self, col, x, y, colliders):
        #Цвет, позиция X и Y, коллизия?
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('movement/sprites/idle.png').convert_alpha()

        self.images_walk = []
        self.images = []
        self.images_walk.append(pygame.image.load('movement/sprites/walk1.png').convert_alpha())
        self.images_walk.append(pygame.image.load('movement/sprites/walk2.png').convert_alpha())
        self.images_walk.append(pygame.image.load('movement/sprites/walk3.png').convert_alpha())
        self.images_walk.append(pygame.image.load('movement/sprites/walk4.png').convert_alpha())
        self.images_walk.append(pygame.image.load('movement/sprites/walk5.png').convert_alpha())
        self.images_walk.append(pygame.image.load('movement/sprites/walk6.png').convert_alpha())
        self.images.append(pygame.image.load('movement/sprites/idle.png').convert_alpha())
        self.rect = pygame.Rect(x, y, 50, 172)
        self.rect.center = (x, y)
        self.vel = (0, 0)
        self.grounded = False
        self.colliders = colliders
        self.scroll_x = 0
        self.scroll_y = 0
        self.frame = 0
        self.slaming = False
        self.jump_power = -8
        self.slam_storage = 0
        self.fbs = 0
        self.jumps = 3
        self.noclip = False
        self.sounds = []
        self.sounds.append(pygame.mixer.Sound("movement/sounds/jump.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/dash.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/land.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/footsteps.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/stamina1.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/stamina2.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/stamina3.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/falling.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/message.wav"))
        self.sounds.append(pygame.mixer.Sound("movement/sounds/undone.wav"))
        self.sounds[0].set_volume(0.5)
        self.sounds[1].set_volume(0.5)
        self.sounds[2].set_volume(0.3)
        self.sounds[7].set_volume(0.0)
        self.sounds[4].set_volume(0.3)
        self.sounds[5].set_volume(0.3)
        self.sounds[6].set_volume(0.3)
        self.sounds[7].set_volume(0.0)
        self.sounds[8].set_volume(0.5)
        self.sounds[3].play(-1)
        self.sounds[7].play(-1)
    #Функция выполняется каждый тик
    def update(self, scroll_x, scroll_y):
        #Переменные и гравитация
        if not self.noclip:
            self.frame += 1
            self.vel = (self.vel[0], self.vel[1] + 1/6)
            self.grounded = False
            self.scroll_x = scroll_x
            self.scroll_y = scroll_y

            sps = 8
            if self.vel[0] < -1 or self.vel[0] > 1:
                for i in range(len(self.images_walk)):
                    if i * (60 / sps)  < (self.frame % (60 * (len(self.images_walk)) / sps)) < (i + 1) * (60 / sps):
                        self.image = pygame.transform.flip(self.images_walk[i % len(self.images_walk)], self.vel[0] < -1, False)
            else:
                    self.image = self.images[0]
                    self.frame = 0

            #Коллизия и попытка движения
            self.rect.move_ip(self.vel[0], 0)
            if self.vel[0] != 0:
                for i in range(len(self.colliders)):
                    if self.rect.colliderect(self.colliders[i]) and self.colliders[i].collision and not self.colliders[i].has_trigger and not self.colliders[i].isDoor:
                        while self.rect.colliderect(self.colliders[i]) and self.colliders[i].collision == True:
                            if self.vel[0] != 0: self.rect.move_ip((self.vel[0] / abs(self.vel[0]))* -1, 0)
                        self.vel = (0, self.vel[1])

                    elif self.colliders[i].has_trigger and self.rect.colliderect(self.colliders[i].trigger_rect):
                        self.colliders[i].triggered = True

                    elif self.colliders[i].has_trigger and not self.rect.colliderect(self.colliders[i].trigger_rect):
                        self.colliders[i].triggered = False

                    elif self.rect.colliderect(self.colliders[i]) and self.colliders[i].collision and not self.colliders[i].has_trigger and self.colliders[i].isDoor:
                        if self.rect.colliderect(self.colliders[i].rect_open) and self.colliders[i].opened:
                            while self.rect.colliderect(self.colliders[i].rect_open):
                                if self.vel[0] != 0: self.rect.move_ip((self.vel[0] / abs(self.vel[0]))* -1, 0)
                            self.vel = (0, self.vel[1])
                        elif self.rect.colliderect(self.colliders[i].rect_close) and not self.colliders[i].opened:
                            while self.rect.colliderect(self.colliders[i].rect_close):
                                if self.vel[0] != 0: self.rect.move_ip((self.vel[0] / abs(self.vel[0]))* -1, 0)
                            self.vel = (0, self.vel[1])
                

            #Ещё одна попытка
            if self.vel[1] != 0:
                self.rect.move_ip(0, self.vel[1] + (1 * self.vel[1]) / abs(self.vel[1]))
                for i in range(len(self.colliders)):
                    if self.rect.colliderect(self.colliders[i]) and self.colliders[i].collision and not self.colliders[i].has_trigger:
                        if self.vel[1] != 0: self.rect.move_ip(0, (self.vel[1] + (1 * self.vel[1]) / abs(self.vel[1])) * -1)
                        if self.vel[1] > 0:
                            self.grounded = True
                            self.slaming = False
                            self.sounds[7].set_volume(0.0)
                            if self.vel[1] > 10: self.sounds[2].play()
                        self.vel = (self.vel[0], 0)

                    elif self.colliders[i].has_trigger and self.rect.colliderect(self.colliders[i].trigger_rect):
                        self.colliders[i].triggered = True

                    elif self.colliders[i].has_trigger and not self.rect.colliderect(self.colliders[i].trigger_rect):
                        self.colliders[i].triggered = False
            
            #Трение о поверхности и о воздух
            if self.grounded: self.vel = (self.vel[0] / 1.2, self.vel[1])
            else: self.vel = (self.vel[0] / 1.002, self.vel[1])

            if self.slaming:
                self.slam_storage += 1
                if self.sounds[7].get_volume() < 0.3 and self.slam_storage > 15:
                    self.sounds[7].set_volume(self.sounds[7].get_volume() + (1 / 100))
            
            if self.jumps < 3:
                self.jumps += 0.01

            if self.grounded:
                if self.fbs >= 20:
                    self.slam_storage = 0
                    self.jump_power = -8
                self.fbs += 1
            else: self.fbs = 0

            self.jumps = round(self.jumps, 2)

            if self.jumps == 1:self.sounds[4].play()
            if self.jumps == 2:self.sounds[5].play()
            if self.jumps == 2.99:self.sounds[6].play()

            #Округляем велосити до 2 знаков в меньшую
            self.vel = ((int(self.vel[0] * 100)) / 100, (int(self.vel[1] * 100)) / 100)
    
    def reset(self, x, y, col, resVel, scroll_x, scroll_y):
        self.scroll_x = scroll_x
        self.scroll_y = scroll_y
        if resVel:
            self.vel = (0,0)
        self.jumps = 3
        self.rect.x = x - 25
        self.rect.y = y - 86
        self.colliders = col
        self.slaming = False
        self.jump_power = -8
        self.slam_storage = 0
        self.fbs = 0

    #На экран выводим
    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (self.rect.x - scroll_x + 875, self.rect.y - scroll_y + 375))

#Класс спрайта или просто объекта
class Sprite(pygame.sprite.Sprite):
    #Переменные
    def __init__(self, col, x, y, size_x, size_y, collision, anchored=True):
        #Цвет, позиция X и Y, размер X и Y, коллизия?, прикреплён?(взаимодействие объектов между собой недоделано)
        pygame.sprite.Sprite.__init__(self)
        if isinstance(col, str):
            self.image = pygame.Surface((size_x, size_y))
            self.image.fill(col)
        else:
            self.image = col
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel = (0, 0)
        self.col = col
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.anchored = anchored
        self.collision = collision
        self.isDoor = False
        self.has_trigger = False
    #Функция каждый тик вызывается
    def update(self):
        #Простая гравитация без коллизии (пока что)
        if not self.anchored: self.rect.move_ip(self.vel[0], self.vel[1])  
        if not self.anchored: self.vel = (self.vel[0], self.vel[1] + 1/6)
    #На экран вывод
    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (self.rect.x - scroll_x + 875, self.rect.y - scroll_y + 375))

#Класс Двери
class Door(pygame.sprite.Sprite):
    #Переменные
    def __init__(self, col, x, y , x_end, y_end, size_x, size_y):
        #Цвет, позиция X и Y, размер X и Y, коллизия?, прикреплён?(взаимодействие объектов между собой недоделано)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size_x, size_y))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.collision = True
        self.x_end = x_end
        self.y_end = y_end
        self.x_start = x
        self.y_start = y
        self.x_goal = self.x_start
        self.y_goal = self.y_start
        self.opened = False
        self.isDoor = True
        self.has_trigger = False
        self.sound = pygame.mixer.Sound("movement/sounds/door.wav")
        self.sound.set_volume(0.3)

        self.image_open = pygame.Surface((size_x, size_y))
        self.image_close = pygame.Surface((size_x, size_y))
        self.image_open = self.image_open.convert_alpha()
        self.image_close = self.image_close.convert_alpha()
        self.image_open.fill((0, 255, 0, 100))
        self.image_close.fill((255, 0, 0, 100))
        self.rect_open = self.image_open.get_rect()
        self.rect_close = self.image_close.get_rect()
        self.rect_open.center = (x_end, y_end)
        self.rect_close.center = (x, y)
    #Функция каждый тик вызывается
    def update(self):
        #Перемещение двери
        self.x = (self.x_goal + self.x * 4) / 5
        self.y = (self.y_goal + self.y * 4) / 5
        self.rect.center = (self.x, self.y)
    #Открытие или закрытие
    def switch(self):
        if not self.opened:
            self.x_goal = self.x_end
            self.y_goal = self.y_end
            self.opened = True
        else:
            self.x_goal = self.x_start
            self.y_goal = self.y_start
            self.opened = False

    def open(self):
        if not self.opened:
            self.x_goal = self.x_end
            self.y_goal = self.y_end
            self.opened = True
            self.sound.play()
        
    def close(self):
        if self.opened:
            self.x_goal = self.x_start
            self.y_goal = self.y_start
            self.opened = False

    #Экран картинка
    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (self.rect.x - scroll_x + 875, self.rect.y - scroll_y + 375))

#Класс рычага
class Lever(pygame.sprite.Sprite):
    def __init__(self, col, x, y, size_x, size_y, x_trigger, y_trigger, x_trigger_size, y_trigger_size, show_trigger = False):
        #Рычаг
        pygame.sprite.Sprite.__init__(self)
        if isinstance(col, str):
            self.image = pygame.Surface((size_x, size_y))
            self.image.fill(col)
        else:
            self.image = col
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.collision = False
        
        #Триггер
        self.trigger_image = pygame.Surface((x_trigger_size, y_trigger_size))
        self.button_image = pygame.image.load("movement/sprites/button_f.png")
        self.trigger_image = self.trigger_image.convert_alpha()
        self.trigger_image.fill((0, 255, 0, 100 * int(show_trigger)))
        self.trigger_rect = self.trigger_image.get_rect()
        self.trigger_rect.center = (x_trigger, y_trigger)
        self.x_trigger = x_trigger
        self.y_trigger = y_trigger
        self.has_trigger = True
        self.triggered = False
        self.locked = False
    #На экран
    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.trigger_image, (self.trigger_rect.x - scroll_x + 875, self.trigger_rect.y - scroll_y + 375))
        screen.blit(self.image, (self.rect.x - scroll_x + 875, self.rect.y - scroll_y + 375))
        if self.triggered and not self.locked:
            screen.blit(self.button_image, (self.rect.x - scroll_x + 875 + self.rect.size[0] / 2 - 15, self.rect.y - scroll_y + 375 + self.rect.size[1] / 2 - 15))
    #каждый тик
    def update(self):
        if self.triggered:
            self.triggered = False
    
class Scene():
    def __init__(self, name, objs, x=0, y=0, hud=False):
        self.name = name
        self.objs = objs
        self.x = x
        self.y = y
        self.hud = hud

class Trigger(pygame.sprite.Sprite):
    def __init__(self, x, y, size_x, size_y, visible):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size_x, size_y)).convert_alpha()
        self.image.fill((0, 255, 0, 100 * int(visible)))
        self.trigger_rect = self.image.get_rect()
        self.trigger_rect.center = (x, y)
        self.rect = self.trigger_rect
        self.collision = False
        self.has_trigger = True
        self.isDoor = False
        self.triggered  = False
        self.active = True
    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (self.trigger_rect.x - scroll_x + 875, self.trigger_rect.y - scroll_y + 375))

class Message():
    def __init__(self, message, x, y, active, locked=True):
        self.text = []
        for i in range(len(message)):
            self.text.append(pygame.font.Font("movement/fonts/ultrakall.ttf", 36).render(message[i], False, (255, 255, 255)))
        self.message = message
        self.box_rect = self.text[0].get_rect()
        for i in range(len(message)-1):
            self.box_rect.size = (self.box_rect.size[0], self.box_rect.size[1] + self.text[i+1].get_rect().size[1])
        self.box = pygame.Surface((self.box_rect.size[0] + 100, self.box_rect.size[1] + 100)).convert_alpha()
        self.box.fill((0, 0, 0, 100))
        self.x = x
        self.y = y
        self.active = active
        self.locked = locked
    def draw(self, screen, scroll_x, scroll_y):
        if self.active:
            if self.locked:
                screen.blit(self.box, (self.x - 50 - self.text[0].get_rect().size[0] / 2, self.y - 50 - self.text[0].get_rect().size[1] / 2 - (len(self.message)- 1) * 13))
                for i in range(len(self.message)):
                    screen.blit(self.text[i], (self.x - self.text[i].get_rect().size[0] / 2, self.y - self.text[i].get_rect().size[1] / 2 + (36 * i) - (len(self.message)- 1) * 13))
            if not self.locked:
                screen.blit(self.box, (self.x - 50 - self.text[0].get_rect().size[0] / 2  - scroll_x + 875, self.y - 50 - self.text[0].get_rect().size[1] / 2 - (len(self.message)- 1 ) * 13 - scroll_y + 375))
                for i in range(len(self.message)):
                    screen.blit(self.text[i], (self.x - self.text[i].get_rect().size[0] / 2  - scroll_x + 875, self.y - self.text[i].get_rect().size[1] / 2 + (36 * i) - (len(self.message)- 1) * 13 - scroll_y + 375))
    def change(self, message):
        self.text = []
        for i in range(len(message)):
            self.text.append(pygame.font.Font("movement/fonts/ultrakall.ttf", 36).render(message[i], False, (255, 255, 255)))
        self.message = message
        self.box_rect = self.text[0].get_rect()
        for i in range(len(message)-1):
            self.box_rect.size = (self.box_rect.size[0], self.box_rect.size[1] + self.text[i+1].get_rect().size[1])
        self.box = pygame.Surface((self.box_rect.size[0] + 100, self.box_rect.size[1] + 100)).convert_alpha()
        self.box.fill((0, 0, 0, 100))

class lockHud():
    def __init__(self, x, y, text, answer):
        self.x = x
        self.y = y
        self.text = text
        self.answer = answer
        self.input = ""
        self.sounds = [
            pygame.mixer.Sound("movement/sounds/error.wav")
        ]
        self.sounds[0].set_volume(0.5)
        self.input_text = pygame.font.Font("movement/fonts/ultrakall.ttf", 36).render(self.input, False, (255, 255, 255))
        self.active = False
        self.text_render = pygame.font.Font("movement/fonts/ultrakall.ttf", 36).render(self.text, False, (255, 255, 255))
        self.image = pygame.Surface((230, 136)).convert_alpha()
        self.image.fill((0, 0, 0, 100))
        self.box_image = pygame.Surface((200, 40)).convert_alpha()
        self.box_image.fill((100, 100, 100, 255))
        self.box = self.image.get_rect()
        self.box.center = (x, y)
        self.text_box = self.box_image.get_rect()
        self.text_box.center = (x, y)
    def draw(self, screen, scroll_x, scroll_y):
        if self.active:
            screen.blit(self.image, (self.box.x - scroll_x + 875, self.box.y - scroll_y + 375))
            screen.blit(self.text_render, (self.box.x - scroll_x + 875 + 115  - self.text_render.get_rect().size[0] / 2, self.box.y - scroll_y + 375 + 68 - self.text_render.get_rect().size[1] / 2 - 36))
            screen.blit(self.box_image, (self.text_box.x - scroll_x + 875, self.text_box.y - scroll_y + 375 + 20))
            self.input_text = pygame.font.Font("movement/fonts/ultrakall.ttf", 36).render(self.input, False, (255, 255, 255))
            screen.blit(self.input_text, (self.box.x - scroll_x + 875 + 115  - self.input_text.get_rect().size[0] / 2, self.box.y - scroll_y + 375 + 68 - self.input_text.get_rect().size[1] / 2 + 20))
    def add(self, input):
        if len(self.input) < 8:
            self.input += input
    def errase(self):
        self.input = ''.join(list(self.input)[0:-1])