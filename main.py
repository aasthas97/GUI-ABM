import pygame

def drawGrid(grid_size, window_size):
    blockSize = window_size//grid_size #Set the size of the grid block
    for x in range(window_size):
        for y in range(window_size):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)


# initialize game
pygame.init()
grid_size = 4

# initialize window
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Reach the hospital')
icon = pygame.image.load("face.jpg")
pygame.display.set_icon(icon)

# initialize player
playerIcon = pygame.image.load('player.png')
playerX = 0
playerY = 0
def addPlayer(x, y):
    screen.blit(playerIcon, (x, y))

# initialize goal
goalIcon = pygame.image.load('goal.png')
goalX = 400-66
goalY = 400-66
def addGoal(x, y):
    screen.blit(goalIcon, (x, y))

# detect goal reach
def reachedGoal(player_pos_x, player_pos_y):
    if goalX - player_pos_x < 40 and goalY - player_pos_y < 40:
        return True
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit button pressed
            running = False

        if event.type == pygame.KEYDOWN: # a key has been pressed
            if event.key == pygame.K_LEFT:
                playerX -= 50
            if event.key == pygame.K_RIGHT:
                playerX += 50
            if event.key == pygame.K_UP:
                playerY -= 50
            if event.key == pygame.K_DOWN:
                playerY += 50

    screen.fill((255, 255, 255))

    # Window boundaries
    playerX = 0 if playerX < 0 else playerX
    playerX = width-64 if playerX > width-64 else playerX # subtracting 64 because the player icon occupies 64 pixels

    playerY = 0 if playerY < 0 else playerY
    playerY = height-64 if playerY > height-64 else playerY

    # check if player has reached goal
    if reachedGoal(playerX, playerY):
        over_font = pygame.font.Font('freesansbold.ttf', 28)
        game_over_text = over_font.render('Game over!', True, (0, 0, 0))
        screen.blit(game_over_text, (120, 150))
        ### Uncomment to exit the window after game ends
        # print('Game over.')
        # break

    # render
    ### Uncomment the following to add grid
    # drawGrid(grid_size, height)
    addPlayer(playerX, playerY)
    addGoal(goalX, goalY)
    pygame.display.update()
