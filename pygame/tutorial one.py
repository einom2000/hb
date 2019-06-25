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


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True

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


def redraw_game_window():
    wn.blit(bg, (0, 0))
    man.draw(wn)
    for bullet in bullets:
        bullet.draw(wn)
    pygame.display.update()


# main loop
man = Player(300, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 0 < bullet.x < 500 :
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left :
            facing  = -1
        else:
            facing = 1

        if len(bullets) < 5:
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

