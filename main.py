import pygame
import numpy as np
from pygame import draw
from pygame_widgets import Slider
# import ipywidgets as widgets

# CLASSES
class Player(pygame.sprite.Sprite):
    def __init__(self, X, Y, scale = None, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.X = X
        self.Y = Y
        self.speed = speed
        self.flip = False
        self.playerIcon = pygame.image.load('./images/player.png')
        self.rect = self.playerIcon.get_rect()
        self.rect.center = (playerX+32, playerY+32)
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
        self.rect.y += dy
        
        # define x-axis boundaries
        self.rect.x = 0 if self.rect.x <0 else self.rect.x
        self.rect.x = 1040 if self.rect.x >1040 else self.rect.x

        
        # define y-axis boundaries
        self.rect.y = 0 if self.rect.y <0 else self.rect.y
        self.rect.y = 436 if self.rect.y >436 else self.rect.y
        
    def collide(self, item):
        collision_tolerance = 10
        if abs(self.rect.bottom - item.rect.top) <= collision_tolerance: # top collision
            self.rect.y -= self.speed
        if abs(self.rect.top - item.rect.bottom) <= collision_tolerance: # bottom collision
            self.rect.y += self.speed
        if abs(self.rect.left - item.rect.right) <= collision_tolerance: # right collision
            self.rect.x += self.speed
        if abs(self.rect.right - item.rect.left) <= collision_tolerance: # left collision
            self.rect.x -= self.speed

    def draw(self):
        screen.blit(pygame.transform.flip(self.playerIcon, self.flip, False), self.rect)

class Graphics:
    """Graphics to be displayed in game window"""
    def __init__(self,icon_path):
        self.icon = pygame.image.load(icon_path)
        self.rect = self.icon.get_rect()
    
    def draw(self, x, y, scale = 0):
        if scale != 0:
            self.icon = pygame.transform.scale(self.icon, scale)
        self.rect.center = (x+32, y+32)
        screen.blit(self.icon, (x, y))

    def drawRect(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect,  2)

class Text:
    """Text to be displayed in game window"""
    def __init__(self, text):
        self.text = text
        
    def write(self, loc, color = (0, 0, 255), font_size = 16):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        screen.blit(font.render(self.text, True, color), loc)        


# FUNCTIONS
def addGameRect(screen, width, height):
    """Draw rectangle around the gaming part of the window"""
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, width, height),  2)
    
def isCollide(item1, item2):
    r1 = item1.rect
    r2 = item2.rect
    return r1.colliderect(r2)


# AGENT VALUES
prob_risk_avoidance = np.random.random()
prob_profit_seeking = np.random.random()
learning_rate = np.random.random()

print(prob_risk_avoidance, prob_profit_seeking, learning_rate)
probabilities = [Text('Risk avoidance: %.2f' % prob_risk_avoidance), Text('Profit-seeking: %.2f' % prob_profit_seeking), Text('Learning Rate: %.2f' % learning_rate)]

risk= np.random.random() # risk value
cost = np.random.random()
reward = np.random.random()

print('Risk: %f\nCost: %f\nReward: %f' % (risk, cost, reward))
rrc = [Text('Risk: %.2f' % risk), Text('Cost: %.2f' % cost), Text('Reward: %.2f' % reward)]

# PLAYER
playerX = 0
playerY = 0
player = Player(playerX, playerY)
move_left = False
move_right = False
move_up = False
move_down = False


# ELEMENTS
icecream = Graphics('./images/ice-cream-cart.png')
icecreamX = 785
icecreamY = 100

dog = Graphics('./images/dog.png')
dogX = 560
dogY = 280

danger = Graphics('./images/danger.png')
dangerX = 185
dangerY = 400
danger2 = Graphics('./images/danger.png')

size = width, height = 1300, 500 # window size
goalX = width-270
goalY = height-68
goal = Graphics('./images/goal.png')

# initialize game
pygame.init()

# initialize window
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Reach the hospital')
# bg = pygame.image.load("./images/grid-bg.png")
clock = pygame.time.Clock()
FPS = 30

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
#     screen.blit(bg, (0, 0))
    player.draw()
    addGameRect(screen, width-200, height)
    icecream.draw(icecreamX, icecreamY)
    dog.draw(dogX, dogY)
    goal.draw(goalX, goalY)
    danger.draw(dangerX, dangerY) 
    danger.drawRect()   
    danger2.draw(1110, 85, scale = (50, 50)) # draw danger icon outside game window

    
    # DISPLAY TEXT OUTSIDE GAME WINDOW
    legend = Text('LEGEND')
    legend.write(loc = (1135, 20), color = (0, 0, 0), font_size=24)
    for i in range(len(probabilities)):
        prob = probabilities[i]
        prob.write(loc = (1120, 170+i*20), color = (0, 0, 200))
    
    for j in range(len(rrc)):
        value = rrc[j]
        value.write(loc = (1170, 80+j*20), color = (0, 0, 200))
    
    # MOVE PLAYER
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

    # CHECK FOR COLLISIONS
    if isCollide(player, goal):
        player.collide(goal)
        over_font = pygame.font.Font('freesansbold.ttf', 28)
        game_over_text = over_font.render('Game over!', True, (0, 0, 0))
        screen.blit(game_over_text, (300, 150))

    if isCollide(player, dog):
        player.collide(dog)
        
    if isCollide(player, icecream):
        player.collide(icecream)
        
    if isCollide(player, danger):
        player.collide(danger)
        R = prob_risk_avoidance * risk
        P = prob_profit_seeking * (reward-cost)
        net = P-R # USE ABSOLUTE VALUE HERE?
        rand = np.random.random()
        # rand = r1.value
        print(rand, net)
        if rand < net:
            print('R: %f\nP: %f\nNet: %f\nrand: %f' % (R, P, net, rand))
            print('Player has decided to steal')
            string = 'Net: %.2f, rand: %.2f, STEALING' % (net, rand)
            player.steal = 1
            rand2 = np.random.random()
            # rand2 = r2.value
            if rand2 < risk:
                prob_risk_avoidance -= learning_rate
                string = 'CAUGHT. Risk avoidance: %.2f, rand2: %.2f' % (prob_risk_avoidance, rand2)
                print('Player got caught')
                running = False

            else:
                print('Did not get caught')
                running = False

            
        else:
            string = 'Not stealing'
            running = False
        
            
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render(string, True, (0, 0, 180))
        screen.blit(text, (300, 150))


    clock.tick(FPS)
    pygame.display.update()