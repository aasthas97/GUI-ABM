import pygame

def drawGrid(grid_size, window_size):
    blockSize = window_size//grid_size #Set the size of the grid block
    for x in range(window_size):
        for y in range(window_size):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1) 


# initialize game
pygame.init()
grid_size = 6

# initialize window
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Grid game')
icon = pygame.image.load("face.jpg")
pygame.display.set_icon(icon)

# initialize player
playerIcon = pygame.image.load('player.png')
playerX = 0
playerY = 0
def addPlayer(x, y):
    screen.blit(playerIcon, (x, y))

# Game loop
running = True
i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit button pressed
            running = False
    
    screen.fill((255, 255, 255))
    drawGrid(grid_size, height)

    addPlayer(playerX, playerY)
    pygame.display.update()
   
