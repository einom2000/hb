import pygame

pygame.init()

wn = pygame.display.set_mode((500, 480))

pygame.display.set_caption('吃鸭游戏')

bg = pygame.image.load('pic\\bg.jpg')

music = pygame.mixer.music.load('pic\\music.mp3')

run = True
pygame.mixer.music.play(-1)
while run:
    wn.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
