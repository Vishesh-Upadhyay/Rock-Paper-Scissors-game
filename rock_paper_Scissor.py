import pygame
pygame.init()   # Initialize pyame 

screen = pygame.display.set_mode((800,600))  #set the screen
pygame.display.set_caption("LETS ROCK PAPER and SCISSOR")
icon = pygame.image.load('rock_paper_scissors.png')
pygame.display.set_icon(icon)
running = True                  #game loop
while running:                  # keep the window stable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False