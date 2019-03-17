'''
The MainMenu for the game KnightFall.
Last updated on March 17 2019
'''

import pygame
from pygame import *
import time
from Button import Button
pygame.init()

class MainMenu:
    
    def __init__(self, view):
        '''
        Create the KnightFall's MainMenu to display in view.
        '''
        self.name = "KnightFall"
        self.view = view

        # Call helpers to prepare the visual elements for MainMenu
        self._set_bkg("../imgs/bkg-main-720.png")
        self._create_buttons()

    def _set_bkg(self, image_file):
        '''
        Load and prepare the background image for the KnightFall MainMenu.
        '''
        self.bkg = pygame.image.load(image_file)
        # scale bkg image to window size
        width, height = pygame.display.get_surface().get_size()
        self.bkg = pygame.transform.scale(self.bkg, (width, height))
        
        self.rect = self.bkg.get_rect()
        self.rect.left, self.rect.top = [0,0]

    def _create_buttons(self):
        '''
        Create the MainMenu buttons using the Button class.
        '''
        # positioning relative to 720p window
        self.btn_start = Button("Start", "../imgs/btn-main/btn-start.png", gD, [387,310])
        self.btn_tut = Button("Tutorial", "../imgs/btn-main/btn-tutorial.png", gD, [387,392])
        self.btn_lb = Button("Leaderboards", "../imgs/btn-main/btn-leaderboards.png", gD, [387,473])
        self.btn_creds = Button("Credits", "../imgs/btn-main/btn-credits.png", gD, [387,555])
        self.btn_quit = Button("Quit", "../imgs/btn-main/btn-quit.png", gD, [631,555])
        
    def display_MainMenu(self, clock = None):
        '''
        Display MainMenu on the view screen and handle key events.
        '''
        # MainMenu takes an existing clock or uses its own
        self.clock = pygame.time.Clock() if clock == None else clock

        show_menu = True
        while show_menu:

            # Render background
            self.view.fill([255, 255, 255])
            self.view.blit(self.bkg, self.rect)

            # Render Buttons
            self.btn_start.display_button()
            self.btn_tut.display_button()
            self.btn_lb.display_button()
            self.btn_creds.display_button()
            self.btn_quit.display_button()

            # Track cursor position and click action
            cursor = pygame.mouse.get_pos()
            click_action = pygame.mouse.get_pressed()
            
            # Event handling...
            q = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    q = True
                    print("Thanks for playing!")
                    pygame.quit()
                    quit()
                    break
            if q: break # Break while loop if quit or pygame.error is raised

            # TODO: Implement start, tutorial, leaderboards, credits menus
            if self.btn_start.get_btnrect().collidepoint(cursor):
                if click_action[0] == 1:
                    print("Start")
                    
            if self.btn_tut.get_btnrect().collidepoint(cursor):
                if click_action[0] == 1:
                    print("Tutorial")
                    
            if self.btn_lb.get_btnrect().collidepoint(cursor):
                if click_action[0] == 1:
                    print("Leaderboards")

            if self.btn_creds.get_btnrect().collidepoint(cursor):
                if click_action[0] == 1:
                    print("Credits")

            if self.btn_quit.get_btnrect().collidepoint(cursor):
                if click_action[0] == 1:
                    print("Good Bye!")
                    show_menu = False
                    pygame.quit()
                    quit()
                    break
                    
            pygame.display.update()
            self.clock.tick(15)

# TODO: Implement into view
# Use 720p res for the window size to match background image size
# Remove below once implemented into view
# =================================================================
window_size = (1280, 720)
gD = pygame.display.set_mode(window_size)

pygame.display.set_caption("KnightFall")
main = MainMenu(gD)
main.display_MainMenu()
