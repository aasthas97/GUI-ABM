import pygame

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
        self.playerIcon = pygame.image.load('player.png')
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



# initialize window
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Reach the hospital')
icon = pygame.image.load("face.jpg")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
FPS = 60

# initialize player
playerX = 0
playerY = 32
player = Player(playerX, playerY)
move_left = False
move_right = False
move_up = False
move_down = False

# Game loop
running = True
while running:
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

    clock.tick(FPS)
    screen.fill((255, 255, 255))
    player.draw()
    player.move(move_left, move_right, move_up, move_down)
    pygame.display.update()
