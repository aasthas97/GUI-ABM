import pygame
import numpy as np
from pygame import draw
import button

# initialize game
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, X, Y, scale = None, speed = 10):
        """Direction: Direction in which player is facing. 1: right, -1: left"""
        pygame.sprite.Sprite.__init__(self)
        self.X = X
        self.Y = Y
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.playerIcon = pygame.image.load('./images/player.png')
        self.rect = self.playerIcon.get_rect()
        self.rect.center = (playerX, playerY)

    def move(self, left, right, up, down):
        dx = 0
        dy = 0
        if left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if up:
            dy = -self.speed
            self.flip = False
            self.direction = 1
        if down:
            dy = self.speed
            self.flip = False
            self.direction = 1

        # update rectangle position
        self.rect.x += dx
        self.rect.x = 0 if self.rect.x <0 else self.rect.x
        self.rect.x = 650 if self.rect.x >650 else self.rect.x

        self.rect.y += dy
        self.rect.y = 0 if self.rect.y <0 else self.rect.y
        self.rect.y = 638 if self.rect.y >638 else self.rect.y


    def draw(self):
        screen.blit(pygame.transform.flip(self.playerIcon, self.flip, False), self.rect)


# functions
def addElement(icon, x, y):
    element_rect = icon.get_rect()
    element_rect.center = (x, y)
    screen.blit(icon, (x, y))

def drawGrid(grid_size, window_size=700):
    blockSize = window_size//grid_size #Set the size of the grid block
    for x in range(window_size):
        for y in range(window_size):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

# initialize window
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Reach the hospital')
icon = pygame.image.load("./images/face.jpg")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
FPS = 60
start_game = False

# initialize player
playerX = 0
playerY = 32
player = Player(playerX, playerY)
move_left = False
move_right = False
move_up = False
move_down = False

# other elements
icecream = pygame.image.load('./images/ice-cream-cart.png')
icecreamX = np.random.randint(100, 650)
icecreamY = np.random.randint(100, 650)
dog = pygame.image.load('./images/dog.png')
dogX = np.random.randint(100, 650)
dogY = np.random.randint(100, 650)
## fix below
if dogX == icecreamX or dogY == icecreamY:
    dogX = np.random.randint(100, 650)
    dogY = np.random.randint(100, 650)

start_img = pygame.image.load('./images/start.png')
exit_img = pygame.image.load('./images/exit.png')
start_button = button.Button(270, 200, start_img, 0.5)
exit_button = button.Button(270, 500, exit_img, 0.5)

# initialize goal
goal = pygame.image.load('./images/goal.png')
goalX = width-66
goalY = height-66
def reachedGoal(player_pos_x, player_pos_y):
    if goalX - player_pos_x < 40 and goalY - player_pos_y < 40:
        return True
    return False

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))

    if not start_game: # game has not started and player is in main menu
        start_font = pygame.font.Font('freesansbold.ttf', 28)
        start_text = start_font.render('Click Start to begin', True, (0, 0, 0))
        screen.blit(start_text, (230, 100))
        if start_button.draw(screen):
            start_game = True
        if exit_button.draw(screen):
            running = False
    
    else:
        player.draw()
        # drawGrid(10)
        addElement(icecream, icecreamX, icecreamY)
        addElement(dog, dogX, dogY)
        addElement(goal, goalX, goalY)
        player.move(move_left, move_right, move_up, move_down)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit button pressed
            running = False

        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_ESCAPE: # quit game
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False                

    if reachedGoal(player.rect.x, player.rect.y):
        over_font = pygame.font.Font('freesansbold.ttf', 28)
        game_over_text = over_font.render('Game over!', True, (0, 0, 0))
        screen.blit(game_over_text, (300, 150))

    clock.tick(FPS)
    pygame.display.update()
