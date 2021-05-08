import pygame

# initialize game
pygame.init()

# initialize window
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Grid game')

# icons
icon = pygame.image.load("face.jpg")
pygame.display.set_icon(icon)

# player icon
playerIcon = pygame.image.load('player.png')

def addPlayer():
    screen.blit(playerIcon, (0, 0))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit button pressed
            running = False
    
    screen.fill((255, 255, 255))
    addPlayer()
    pygame.display.update()
   
