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
char_x = 200
char_y = 410
char_vel = 1
walk_count = -1
jump_count = 10
is_jump = False

music = pygame.mixer.music.load('pic\\music.mp3')

run = True
pygame.mixer.music.play(-1)
wn.blit(char, (char_x, char_y))

while run:
    clock.tick(27)
    wn.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # keys is a dictionary {}

    if keys[pygame.K_LEFT] and char_x > char_vel:
        char_x -= char_vel
        wn.blit(walk_left[walk_count // 3], (char_x, char_y))
        walk_count += 1
    elif keys[pygame.K_RIGHT] and char_x < 500 - 64 - char_vel:
        char_x += char_vel
        wn.blit(walk_right[walk_count // 3], (char_x, char_y))
        walk_count += 1
    elif keys[pygame.K_UP] and not is_jump:
        is_jump = True
    else:
        wn.blit(char, (char_x, char_y))

    if is_jump:
        if jump_count >= -10:
            direction = 1
            if jump_count < 0:
                direction = -1
            char_y -= (jump_count ** 2) * 0.5 * direction
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    if walk_count >= 26:
        walk_count = 0

    pygame.display.update()
