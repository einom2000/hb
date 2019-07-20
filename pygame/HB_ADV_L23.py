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


def redraw_game_window():
    wn.blit(bg, (0, 0))
    text = font.render('Score' + str(score), 1,  (0, 0, 0))
    wn.blit(text, (20, 10))
    man1.draw(wn)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
score = 0

music = pygame.mixer.music.load('pic\\music.mp3')
run = True
pygame.mixer.music.play(-1)
man1 = Player(200, 410, 64, 64)


while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # keys is a dictionary {}

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
