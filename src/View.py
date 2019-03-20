'''
The following class is responsible for the visual representation of the 
board on the screen that the user will interact with the game from
Last updated in March 17 2019
'''
import pygame
import os
from random import randint
from PauseMenu import *
from Button import *
from BoardModel import *

class view:
    
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    ICONSIZE = 80
    BACKGROUND_COLOUR_1 = (49, 142, 105)
    BACKGROUND_COLOUR_2 = (48, 115, 221)
    board_model = None
    
    def __init__(self):
        '''
        (View) -> None
        Creates a visual representation of the
        KnightFall game that was started
        '''
        self.load_board()
        self.draw_gameboard()
        
        
    def draw_gameboard(self):
        '''
        (View) -> None
        sets up the visual representation of the 
        game board the user will play on
        '''
        pygame.init()
        
        screen = pygame.display.set_mode([self.WINDOW_WIDTH, self.WINDOW_HEIGHT])
        screen.fill(self.BACKGROUND_COLOUR_1)
        
        font = pygame.font.Font(None, 50)
        
        # creating a pause button
        pause_button = Button('Pause', self.path_to_image('imgs\\gui-play\\btn-pause.png'), screen, [10,10], None)
        pause_button.display_button()
        
        # create score title and area for the score to go
        score_title = Button('Score', self.path_to_image('imgs\\gui-play\\btn-score.png'), screen, [10,450], None)
        score_title.display_button()
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 530, 310, 70))
        pygame.draw.rect(screen, self.BACKGROUND_COLOUR_1, pygame.Rect(55, 535, 300, 60))        
        
        # create timer title and area for the timer to go
        time_title = Button('Time Remaining', self.path_to_image('imgs\\gui-play\\btn-timer.png'), screen, [10,650], None)
        time_title.display_button()
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 730, 310, 70))
        pygame.draw.rect(screen, self.BACKGROUND_COLOUR_1, pygame.Rect(55, 735, 300, 60))
        
        #load image
        KNIGHICONS = []
        for i in range(1,10):
            knightimg = pygame.image.load(self.path_to_image('imgs\\Medieval_%d.png' % i)).convert_alpha()
            if knightimg.get_size() != (self.ICONSIZE, self.ICONSIZE):
                knightimg = pygame.transform.smoothscale(knightimg, (self.ICONSIZE, self.ICONSIZE))
            KNIGHICONS.append(knightimg)
            
        # making the part of the board containing the icons a different colour
        pygame.draw.rect(screen, self.BACKGROUND_COLOUR_2, pygame.Rect(550, 0, self.WINDOW_WIDTH - 500, self.WINDOW_HEIGHT))
        
        #this displays the items in BoardModel board_model on the screen
        for col in range(7):
            for row in range(7):
                screen.blit(KNIGHICONS[self.board_model.board[row][col]], (self.WINDOW_WIDTH - 635 + 90 * col, self.WINDOW_HEIGHT - 720 + 90 * row)) 
                
        # keeps the board open until the user closes it
        closed = False
        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closed = True
            pygame.display.flip()
            
        pygame.quit()
        
    def path_to_image(self, image_location):
        '''
        (View, str) -> str
        Creates and returns the file path to the location
        designated by image_location with the starting
        directory being KnightFall
        '''        
        return os.path.join(os.path.abspath('')[:-4], image_location)
    
    def load_board(self):
        '''
        (View) -> None
        Sets the current instance of BoardModel that
        will be used in this instance of the view
        in board_model
        '''
        self.board_model = BoardModel()