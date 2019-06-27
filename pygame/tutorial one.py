import pygame
pygame.init()

wn = pygame.display.set_mode((500, 480))

pygame.display.set_caption('First Game')

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
clock = pygame.time.Clock()

score = 0

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.is_jump = False
        self.jump_count = 10
        self.left = True
        self.right = False
        self.walk_count = 0
        self.standing = True
        self.hit_box = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, wn):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                wn.blit(walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                wn.blit(walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            if self.right:
                wn.blit(walk_right[0], (self.x, self.y))
            else:
                wn.blit(walk_left[0], (self.x, self.y))
        self.hit_box = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(wn, (0, 0, 0), self.hit_box, 2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walk_count = 0
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
        pygame.draw.circle(wn, self.color, (self.x, self.y), self.radius)


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
        self.hit_box = (self.x + 15 - self.vel, self.y + 1, 34, 57)
        self.health = 10
        self.visible = True

    def draw(self, wn):
        if self.visible:
            self.move()
            if self.walk_count + 1 >= 33:
                self.walk_count = 0
            else:
                self.walk_count += 1

            if self.vel > 0:
                wn.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
            else:
                wn.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))

            pygame.draw.rect(wn, (255, 0, 0), (self.hit_box[0], self.hit_box[1] - 20, 50, 10), 1)
            pygame.draw.rect(wn, (0, 255, 0), (self.hit_box[0], self.hit_box[1] - 20,
                                               50 - ((50 / 10) * (10 - self.health)), 10))
            self.hit_box = (self.x + 15 - self.vel, self.y + 1, 34, 57)
            # pygame.draw.rect(wn, (255, 0, 0), self.hit_box, 2)

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


def redraw_game_window():
    wn.blit(bg, (0, 0))
    text = font.render('Score:' + str(score), 1, (0, 0, 0))
    wn.blit(text, (20, 10))
    man.draw(wn)
    goblin.draw(wn)
    for bullet in bullets:
        bullet.draw(wn)
    pygame.display.update()


# main loop
font = pygame.font.SysFont('comicsans', 30, True)
bullet_sound = pygame.mixer.Sound('pic\\bullet.wav')
hit_sound = pygame.mixer.Sound('pic\\hit.wav')
music = pygame.mixer.music.load('pic\\music.mp3')
pygame.mixer.music.play(-1)
man = Player(200, 410, 64, 64)
goblin = Enemy(64, 410, 64, 64, 450)
bullets = []
run = True
last_shoot_time = -1000
while run:
    clock.tick(27)

    if man.hit_box[1] < goblin.hit_box[1] + goblin.hit_box[3] and man.hit_box[1] + man.hit_box[3] > goblin.hit_box[1]:
        if man.hit_box[0] + man.hit_box[2] > goblin.hit_box[0] and man.hit_box[0] <  goblin.hit_box[0] + goblin.hit_box[2]:
            man.hit()
            score -= 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if goblin.hit_box[1] < bullet.y  + bullet.radius < goblin.hit_box[1] + goblin.hit_box[3] and \
                    goblin.hit_box[0] < bullet.x + bullet.radius < goblin.hit_box[0] + goblin.hit_box[2]:
            goblin.hit()
            hit_sound.play()
            bullets.pop(bullets.index(bullet))
            score += 10
        if 0 < bullet.x < 500:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and pygame.time.get_ticks() - last_shoot_time >= 300:
        last_shoot_time = pygame.time.get_ticks()
        if man.left :
            facing  = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullet_sound.play()
            bullets.append(Projecttile(round(man.x + man.width // 2), round(man.y + man.height // 2)
                                       , 6, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walk_count = 0

    if not man.is_jump:
        if keys[pygame.K_UP]:
            man.is_jump = True
            man.standing = True
    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2) * 0.5 * neg
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 10
    redraw_game_window()

pygame.quit()


