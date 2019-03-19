'''
The following class is responsible for the visual representation of the 
board on the screen that the user will interact with the game from
Last updated in March 17 2019
'''
import pygame
import os
from random import randint

class view:
    
    window_width = 1000
    window_height = 800
    ICONSIZE = 80
    def __init__(self):
        '''
        Creates a visual representation of the 
        KnightFall game that was started
        '''
        self.draw_gameboard()
        
    def draw_gameboard(self):
        '''
        sets up the visual representation of the 
        game board the user will play on
        '''
        pygame.init()
        
        screen = pygame.display.set_mode([self.window_width, self.window_height])
        screen.fill((49, 142, 105))
        
        font = pygame.font.Font(None, 50)
        
        # creating a pause icon
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 35, 140, 60))
        pygame.draw.rect(screen, (49, 142, 105), pygame.Rect(55, 40, 130, 50))
        pause_title = font.render("Pause", 1, (255, 255, 255))
        screen.blit(pause_title, (60, 50))
        
        score_title = font.render("Score", 1, (255, 255, 255))
        screen.blit(score_title, (50, 550))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 590, 200, 50))
        pygame.draw.rect(screen, (49, 142, 105), pygame.Rect(55, 595, 190, 40))
        
        time_title = font.render("Time Left", 1, (255, 255, 255))
        screen.blit(time_title, (50, 650))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 690, 200, 50))
        pygame.draw.rect(screen, (49, 142, 105), pygame.Rect(55, 695, 190, 40))
        #load image
        KNIGHICONS = []
        for i in range(1,10):
            knightimg = pygame.image.load(os.path.join(os.path.abspath('')[:-4], 'imgs\\Medieval_%d.png' % i)).convert_alpha()
            if knightimg.get_size() != (self.ICONSIZE, self.ICONSIZE):
                knightimg = pygame.transform.smoothscale(knightimg, (self.ICONSIZE, self.ICONSIZE))
            KNIGHICONS.append(knightimg)
        # making the part of the board containing the icons a different colour
        pygame.draw.rect(screen, (48, 115, 221), pygame.Rect(300, 0, 700, 800))
        
        #this currently just randomly the icons on the screen, however it should get them from an instance of BoardModel
        for col in range(7):
            for row in range(7):
                screen.blit(KNIGHICONS[randint(0, 8)], (365 + 90 * col, 80 + 90 * row)) 
        # keeps the board open until the user closes it
        closed = False
        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closed = True
            pygame.display.flip()
            
        pygame.quit()