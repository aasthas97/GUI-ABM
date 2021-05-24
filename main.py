import pygame
import numpy as np
from pygame import draw
import button

"""Features: Start menu present, grid background absent"""

# initialize game
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, X, Y, scale = None, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.X = X
        self.Y = Y
        self.speed = speed
        self.flip = False
        self.playerIcon = pygame.image.load('./images/player.png')
        self.rect = self.playerIcon.get_rect()
        self.rect.center = (playerX, playerY)
        self.steal = 0

    def move(self, left, right, up, down):
        dx = 0
        dy = 0
        if left:
            dx = -self.speed
            self.flip = True
        if right:
            dx = self.speed
            self.flip = False
        if up:
            dy = -self.speed
            self.flip = False
        if down:
            dy = self.speed
            self.flip = False

        # update rectangle position
        self.rect.x += dx
        self.rect.x = 0 if self.rect.x <0 else self.rect.x
        self.rect.x = 650 if self.rect.x >650 else self.rect.x

        self.rect.y += dy
        self.rect.y = 0 if self.rect.y <0 else self.rect.y
        self.rect.y = 538 if self.rect.y >538 else self.rect.y

    def draw(self):
        screen.blit(pygame.transform.flip(self.playerIcon, self.flip, False), self.rect)

# element class for graphics display
class Graphics:
    def __init__(self,icon_path):
        self.icon = pygame.image.load(icon_path)
    
    def draw(self, x, y):
        element_rect = self.icon.get_rect()
        element_rect.center = (x, y)
        screen.blit(self.icon, (x, y))
        

# class for on-screen text display        
class Text:
    def __init__(self, text):
        self.text = text
        
    def write(self, loc, color = (0, 0, 255)):
        font = pygame.font.Font('freesansbold.ttf', 16)
        screen.blit(font.render(self.text, True, color), loc)
        

# FUNCTIONS

def addGameRect(screen, width, height):
    """Draw rectangle around the gaming part of the window"""
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, width, height),  2)
    
def reachedDanger(player_pos_x, player_pos_y):
    """Check if player has reached danger"""
    if dangerX - player_pos_x < 40 and dangerY - player_pos_y < 40:
        return True
    return False  

def reachedGoal(player_pos_x, player_pos_y):
    if goalX - player_pos_x < 40 and goalY - player_pos_y < 40:
        return True
    return False

# INITIALIZE VARIABLES
prob_risk_avoidance = np.random.random()
prob_profit_seeking = np.random.random()
learning_rate = np.random.random()
print('Prob_risk_avoidance: %f\nprob_profit_seeking: %f\nlearning_rate: %f' % (prob_risk_avoidance, prob_profit_seeking, learning_rate))


risk_num= np.random.random() # risk value
risk_string = 'Risk: ' + format(risk_num, '.2f')
risk = Text(risk_string) # define class instance to be displayed on screen

# cost
cost_num = np.random.random()
cost_string = 'Cost: ' + format(cost_num, '.2f')
cost = Text(cost_string)

#reward
reward_num = np.random.random()
reward_string = 'Reward: ' + format(reward_num, '.2f')
reward = Text(reward_string)

print('%s\n%s\n%s' % (risk_string, cost_string, reward_string))

R = prob_risk_avoidance * risk_num
P = prob_profit_seeking * (reward_num-cost_num)
net = P-R 
rand = np.random.random()

print('R: %f\nP: %f\nNet: %f\nrand: %f' % (R, P, net, rand))


# START SCREEN
start_img = pygame.image.load('./images/start.png')
exit_img = pygame.image.load('./images/exit.png')
start_button = button.Button(270, 200, start_img, 0.5)
exit_button = button.Button(270, 500, exit_img, 0.5)

# CREATE PLAYER
playerX = 0
playerY = 35
player = Player(playerX, playerY)
move_left = False
move_right = False
move_up = False
move_down = False

# CREATE ELEMENTS
icecream = Graphics('./images/ice-cream-cart.png')
icecreamX = 185
icecreamY = 100

dog = Graphics('./images/dog.png')
dogX = 360
dogY = 280

danger = Graphics('./images/danger.png')
dangerX = 185
dangerY = 400

# CREATE GOAL
size = width, height = 900, 600 # window details
goalX = width-266
goalY = height-66
goal = Graphics('./images/goal.png')

# initialize game
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Reach the hospital')
clock = pygame.time.Clock()
FPS = 60

# Game loop
running = True
start_game = False
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
        addGameRect(screen, width-200, height)
        icecream.draw(icecreamX, icecreamY)
        dog.draw(dogX, dogY)
        goal.draw(goalX, goalY)
        danger.draw(dangerX, dangerY)

        # add risk cost reward details
        danger.draw(750, 10) # draw danger icon outside game window
        risk.write(loc = (750, 70), color = (255, 0, 0))
        cost.write(loc = (750, 85), color = (255, 0, 0))
        reward.write(loc = (750, 100), color = (255, 0, 0))

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
        
    if reachedDanger(player.rect.x, player.rect.y):
        if rand < net:
            print('Stealing')
            string = format(net, '.2f') + ' ' + format(rand, '.2f') + ' ' + str(player.steal)
            player.steal = 1
        else:
            string = 'Skip'
            
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render(string, True, (0, 0, 0))
        screen.blit(text, (300, 150))        

    clock.tick(FPS)
    pygame.display.update()
