import pygame

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

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 3
        self.hit_box = (self.x + 15 - self.vel, self.y + 1,
                        34, 57)
        self.health = 10
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

    def hit(self):
        pass


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
    goblin.draw(wn)
    for bullet in bullets:
        bullet.draw(wn)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
score = 0
bullet_sound = pygame.mixer.Sound('pic\\bullet.wav')
music = pygame.mixer.music.load('pic\\music.mp3')
run = True
bullets = []
last_shoot = -1000
pygame.mixer.music.play(-1)
man1 = Player(200, 410, 64, 64)
goblin = Enemy(64, 410, 64, 64, 450)


while run:
    clock.tick(27)

    if man1.hit_box[1] < goblin.hit_box[1] + goblin.hit_box[3] and \
        man1.hit_box[1] + man1.hit_box[3] > goblin.hit_box[1]:
        if man1.hit_box[0] + man1.hit_box[2] > goblin.hit_box[0] and \
            man1.hit_box[0] < goblin.hit_box[0] + goblin.hit_box[2]:
            man1.hit()
            score -= 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
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
    redraw_game_window()
