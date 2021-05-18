import pygame

# initialize game
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, X, Y, scale = None):
        pygame.sprite.Sprite.__init__(self)
        self.X = X
        self.Y = Y
        self.playerIcon = pygame.image.load('player.png')
        self.rect = self.playerIcon.get_rect()
        self.rect.center = (playerX, playerY)

    def draw(self):
        screen.blit(self.playerIcon, self.rect)



# initialize window
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Reach the hospital')
icon = pygame.image.load("face.jpg")
pygame.display.set_icon(icon)

# initialize player
playerX = 16
playerY = 32
player = Player(playerX, playerY)

# initialize goal
goalIcon = pygame.image.load('goal.png')
goalX = width-66
goalY = height-66
def addGoal(x, y):
    screen.blit(goalIcon, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit button pressed
            running = False

        # keyboard presses
        if event.type == pygame.KEYDOWN:
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
    playerX = 16 if playerX < 16 else playerX
    playerX = width-16 if playerX > width-16 else playerX # subtracting 64 because the player icon occupies 64 pixels

    playerY = 32 if playerY < 32 else playerY
    playerY = height-32 if playerY > height-32 else playerY

    player.draw()
    addGoal(goalX, goalY)
    pygame.display.update()
