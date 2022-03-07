from itertools import permutations
import pygame

n = 8
sample = range(n)
for x in permutations(sample):                      
    if n==len(set(x[i]+i for i in sample))==len(set(x[i]-i for i in sample)):
        place = x
        print(place)
        break

def display_board(n, place):
    pygame.init()
    background = pygame.image.load("Image/chess_board.png")
    queen = pygame.image.load("Image/queen.png")
    icon = pygame.image.load("Image/queen.png")
    screen = pygame.display.set_mode((n*32, n*32))
    pygame.display.set_caption("N Queen")
    pygame.display.set_icon(icon)
    index = 0

    while True:
        screen.blit(background,(0,0))
        for i in range(n):
            screen.blit(queen,(32*i, 32*place[i]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.update()

display_board(n, place)