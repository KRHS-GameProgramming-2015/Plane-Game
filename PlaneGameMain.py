import sys, pygame, math, random
from Thing import *
from Block import *
from Button import *
from Booster import *
from Coin import *
from Spike import *
from Player import *
from Level import *
pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 700
size = width, height
 
bgColor = r,g,b = 135, 206, 235

screen = pygame.display.set_mode(size)

blocks = pygame.sprite.Group()
buttons = pygame.sprite.Group()
gamePeices = pygame.sprite.Group()
boosters = pygame.sprite.Group()
coins = pygame.sprite.Group()
spikes = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Block.containers = (blocks, all)
Player.containers = (players, all)
#Wall.containers = (boundries, all)
#PlayerBall.containers = (players, all)

level = Level("Levels/Level1.layout")

player = level.player
print player.rect.center, player.rect

startup = True

while True:
    while startup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        if player.rect.left <  500:
            player.speed = [3,0]
            player.staticMove() 
            
        elif player.rect.left >= 500 and player.rect.left < 650:
            player.staticTilt(-45)
            player.speed = [3,3]
            player.staticMove()
            
        elif player.rect.left >= 650 and player.rect.left < 700:
            player.staticTilt(0)
            player.speed = [3,0]
            player.staticMove()
            
        elif player.rect.left >= 700 and player.rect.left < 950:
            player.staticTilt(45)
            player.speed = [3,-3]
            player.staticMove()
        
        
        all.update(size)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

    while not startup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            #elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_UP:
                    #player.go("up")
                #elif event.key == pygame.K_DOWN:
                    #player.go("down")
                #elif event.key == pygame.K_LEFT:
                    #player.go("left")
                #elif event.key == pygame.K_RIGHT:
                    #player.go("right")
            #elif event.type == pygame.KEYUP:
                #if event.key == pygame.K_UP:
                    #player.go("stop up")
                #elif event.key == pygame.K_DOWN:
                    #player.go("stop down")
                #elif event.key == pygame.K_LEFT:
                    #player.go("stop left")
                #elif event.key == pygame.K_RIGHT:
                    #player.go("stop right")
        
        all.update(size)
        
        #playersHitBalls = pygame.sprite.groupcollide(players, balls, False, True)
        #playersHitBoundries = pygame.sprite.groupcollide(players, boundries, False, False)
        #ballsHitBoundries = pygame.sprite.groupcollide(balls, boundries, False, False)
        #ballsHitBalls = pygame.sprite.groupcollide(balls, balls, False, False)
        
        #for p in playersHitBoundries:
            #for boundry in playersHitBoundries[p]:
                #p.collideBoundry(boundry)
        
        #for ball in ballsHitBoundries:
            #for boundry in ballsHitBoundries[ball]:
                #ball.collideBoundry(boundry)
        
        #for ball1 in ballsHitBalls:
            #for ball2 in ballsHitBalls[ball1]:
                #ball1.collideBall(ball2)
        
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
