import pygame
import random

pygame.init()

wn = pygame.display.set_mode((500, 480))

pygame.display.set_caption('吃鸭游戏')
clock = pygame.time.Clock()

walk_right = [pygame.image.load('pic\\R1.png'),
              pygame.image.load('pic\\R2.png'),
              pygame.image.load('pic\\R3.png'),
              pygame.image.load('pic\\R4.png'),
              pygame.image.load('pic\\R5.png'),
              pygame.image.load('pic\\R6.png'),
              pygame.image.load('pic\\R7.png'),
              pygame.image.load('pic\\R8.png'),
              pygame.image.load('pic\\R9.png')]

walk_left = [pygame.image.load('pic\\L1.png'),
             pygame.image.load('pic\\L2.png'),
             pygame.image.load('pic\\L3.png'),
             pygame.image.load('pic\\L4.png'),
             pygame.image.load('pic\\L5.png'),
             pygame.image.load('pic\\L6.png'),
             pygame.image.load('pic\\L7.png'),
             pygame.image.load('pic\\L8.png'),
             pygame.image.load('pic\\L9.png')]

bg = pygame.image.load('pic\\bg.jpg')
char = pygame.image.load('pic\\standing.png')

class Enemy(object):
    walk_right = [pygame.image.load('pic\\R1E.png'),
                  pygame.image.load('pic\\R2E.png'),
                  pygame.image.load('pic\\R3E.png'),
                  pygame.image.load('pic\\R4E.png'),
                  pygame.image.load('pic\\R5E.png'),
                  pygame.image.load('pic\\R6E.png'),
                  pygame.image.load('pic\\R7E.png'),
                  pygame.image.load('pic\\R8E.png'),
                  pygame.image.load('pic\\R9E.png'),
                  pygame.image.load('pic\\R10E.png'),
                  pygame.image.load('pic\\R11E.png')]

    walk_left = [pygame.image.load('pic\\L1E.png'),
                 pygame.image.load('pic\\L2E.png'),
                 pygame.image.load('pic\\L3E.png'),
                 pygame.image.load('pic\\L4E.png'),
                 pygame.image.load('pic\\L5E.png'),
                 pygame.image.load('pic\\L6E.png'),
                 pygame.image.load('pic\\L7E.png'),
                 pygame.image.load('pic\\L8E.png'),
                 pygame.image.load('pic\\L9E.png'),
                 pygame.image.load('pic\\L10E.png'),
                 pygame.image.load('pic\\L11E.png')]

    def __init__(self, x, y, width, height, start, end, health, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.start = start
        self.path = [self.start, self.end]
        self.walk_count = 0
        self.vel = vel
        self.hit_box = (self.x + 15 - self.vel, self.y + 1,
                        34, 57)
        self.health = health
        self.max_health = health
        self.visible = True

    def draw(self, wn):
        if self.visible:
            self.move()
            if self.walk_count +1 >= 33:
                self.walk_count = 0
            else:
                self.walk_count += 1

            if self.vel > 0:
                wn.blit(self.walk_right[self.walk_count // 3],
                        (self.x, self.y))
            else:
                wn.blit(self.walk_left[self.walk_count // 3],
                        (self.x, self.y))
            self.hit_box = (self.x + 15 - self.vel, self.y + 1,
                            34, 57)
            # pygame.draw.rect(wn, (255, 0, 0), self.hit_box, 2)

            pygame.draw.rect(wn, (255, 0, 0),
                  (self.hit_box[0], self.hit_box[1] -20, 50, 10), 1)

            pygame.draw.rect(wn, (0, 255, 0),
                  (self.hit_box[0], self.hit_box[1] - 20,
                   50 - ((50 / self.max_health) * (self.max_health - self.health)), 10))

    def move(self):
        if self.x + self.vel < self.path[1]:
            self.x += self.vel
        else:
            self.vel *= -1
            self.walk_count = 0
        if self.x + self.vel > self.path[0]:
            self.x += self.vel
        else:
            self.vel *= -1
            self.walk_count = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
            self.y = -900
        pass


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.is_jump = False
        self.jump_count = 10
        self.walk_count = 0
        self.left = True
        self.right = False
        self.standing = True
        self.hit_box = (self.x + 17, self.y +11, 29, 52)

    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                wn.blit(walk_left[self.walk_count // 3],
                        (self.x, self.y))
                self.walk_count += 1
            if self.right:
                wn.blit(walk_right[self.walk_count // 3],
                        (self.x, self.y))
                self.walk_count += 1
        else:
            if self.left:
                wn.blit(walk_left[0], (self.x, self.y))
            else:
                wn.blit(walk_right[0], (self.x, self.y))
        self.hit_box = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(wn, (0, 0, 0), self.hit_box, 2)

    def hit(self):
        if self.x >= 200:
            self.x = 60
        else:
            self.x = 300

        self.y = 410
        self.walk_count =0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        wn.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class Projecttile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, wn):
        pygame.draw.circle(wn, self.color,
                           (self.x, self.y), self.radius)


def redraw_game_window():
    wn.blit(bg, (0, 0))
    text = font.render('Score' + str(score), 1,  (0, 0, 0))
    wn.blit(text, (20, 10))
    man1.draw(wn)
    for goblin in goblins:
        goblin.draw(wn)
    for bullet in bullets:
        bullet.draw(wn)
    pygame.display.update()


def create_goblins(num):
    global goblins
    for _ in range(num):
        g_health = random.randint(10, 20)
        g_vel = random.randint(1, 3) * (random.randint(1, 2) * 2 -3)
        g = Enemy(random.randint(100, 400), 410, 64, 64, 4, 450, g_health, g_vel)
        goblins.append(g)


font = pygame.font.SysFont('comicsans', 30, True)
score = 0
bullet_sound = pygame.mixer.Sound('pic\\bullet.wav')
music = pygame.mixer.music.load('pic\\music.mp3')
hit_sound = pygame.mixer.Sound('pic\\bullet.wav')
run = True
bullets = []
last_shoot = -1000
pygame.mixer.music.play(-1)
man1 = Player(100, 410, 64, 64)
goblins = []
create_goblins(2)

while run:
    clock.tick(27)
    for goblin in goblins:
        if man1.hit_box[1] < goblin.hit_box[1] + goblin.hit_box[3] and \
             man1.hit_box[1] + man1.hit_box[3] > goblin.hit_box[1]:
            if man1.hit_box[0] + man1.hit_box[2] > goblin.hit_box[0] and \
                 man1.hit_box[0] < goblin.hit_box[0] + goblin.hit_box[2]:
                man1.hit()
                score -= 5
        if goblin.y == -900:
            goblins.pop(goblins.index(goblin))
            create_goblins(random.randint(0, 3))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        for goblin in goblins:
            if goblin.hit_box[1] < bullet.y + bullet.radius < \
                    goblin.hit_box[1] + goblin.hit_box[3] and \
                    goblin.hit_box[0] < bullet.x + bullet.radius < \
                    goblin.hit_box[0] + goblin.hit_box[2]:
                goblin.hit()
                hit_sound.play()
                bullets.pop(bullets.index(bullet))
                score += 20

        if 0 < bullet.x < 500:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()  # keys is a dictionary {}

    if keys[pygame.K_SPACE] and \
        pygame.time.get_ticks() - last_shoot >= 300:
        last_shoot = pygame.time.get_ticks()
        if man1.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullet_sound.play()
            bullets.append(Projecttile(round(man1.x + man1.width // 2),
                                       round(man1.y + man1.height // 2),
                                       6, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and man1.x > man1.vel:
        man1.x -= man1.vel
        man1.left = True
        man1.right = False
        man1.standing = False

    elif keys[pygame.K_RIGHT] and man1.x < 500 - man1.width\
                                - man1.vel:
        man1.x += man1.vel
        man1.left = False
        man1.right = True
        man1.standing = False
    else:
        man1.standing = True
        man1.walk_count = 0

    if not man1.is_jump:
        if keys[pygame.K_UP]:
            man1.is_jump = True
            man1.standing = True
    else:
        if man1.jump_count >= -10:
            direction = 1
            if man1.jump_count < 0:
                direction = -1
            man1.y -= (man1.jump_count ** 2) * 0.5 * \
                      direction
            man1.jump_count -= 1
        else:
            man1.is_jump = False
            man1.jump_count = 10
            if man1.y > 410:
                man1.y = 410
    redraw_game_window()
