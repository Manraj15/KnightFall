'''
Prepare the KnightFall game instances.
    Initialize pygame
    Load images
    Create buttons and menus
'''
import pygame
import time

from GUI import *

from MainMenu import *
from ModeMenu import *
from LBMenu import *
from TutorialMenu import *
from CreditsMenu import *
from PauseMenu import *

pygame.init()

WINDOW_SIZE = (1280, 720)
SCREEN_DISPLAY = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("KnightFall")

# Set up MainMenu
list_main = [Button("title-main", "../imgs/title/logo-main.png", SCREEN_DISPLAY, [294,97]),
             # MainMenu Buttons
             Button("start", "../imgs/gui-main/btn-start.png", SCREEN_DISPLAY, [400,310]),
             Button("tutorial", "../imgs/gui-main/btn-tutorial.png", SCREEN_DISPLAY, [400,392]),
             Button("leaderboards", "../imgs/gui-main/btn-leaderboards.png", SCREEN_DISPLAY, [400,473]),
             Button("credits", "../imgs/gui-main/btn-credits.png", SCREEN_DISPLAY, [400,555]),
             Button("quit", "../imgs/gui-main/btn-quit.png", SCREEN_DISPLAY, [644,555])
             ]

# Set up ModeMenu
list_mode = [Button("logo", "../imgs/title/logo-small.png", SCREEN_DISPLAY, [446,72]),
             Button("title", "../imgs/title/title-select-mode.png", SCREEN_DISPLAY, [446,162]),
             Button("classic", "../imgs/gui-mode/btn-classic.png", SCREEN_DISPLAY, [400,310]),
             Button("survival", "../imgs/gui-mode/btn-survival.png", SCREEN_DISPLAY, [400,392]),
             Button("back", "../imgs/gui-mode/btn-back-long.png", SCREEN_DISPLAY, [400,473])
             ]

# Set up Leaderboards
list_lb = [  Button("logo", "../imgs/title/logo-small.png", SCREEN_DISPLAY, [52,44]),
             Button("title", "../imgs/title/title-lb.png", SCREEN_DISPLAY, [518,44]),
             # LB Buttons
             Button("classic", "../imgs/gui-lb/btn-classic-switch.png", SCREEN_DISPLAY, [55,457]),
             Button("survival", "../imgs/gui-lb/btn-survival-switch.png", SCREEN_DISPLAY, [55,457]),
             Button("back", "../imgs/btn-reuse/btn-back.png", SCREEN_DISPLAY, [55,551]),
             # Leaderboard ranking
             Button("rank1", "../imgs/gui-lb/lb-rank1.png", SCREEN_DISPLAY, [519,174]),
             Button("rank2", "../imgs/gui-lb/lb-rank2.png", SCREEN_DISPLAY, [519,268]),
             Button("rank3", "../imgs/gui-lb/lb-rank3.png", SCREEN_DISPLAY, [519,361]),
             Button("rank4", "../imgs/gui-lb/lb-rank4.png", SCREEN_DISPLAY, [519,455]),
             Button("rank5", "../imgs/gui-lb/lb-rank5.png", SCREEN_DISPLAY, [519,549]),
             ]

# Set up TutorialMenu
list_tut = [ Button("logo", "../imgs/title/logo-small.png", SCREEN_DISPLAY, [446,72]),
             Button("title", "../imgs/title/title-tutorial.png", SCREEN_DISPLAY, [528,162]),
             Button("back", "../imgs/btn-reuse/btn-back-small.png", SCREEN_DISPLAY, [55,600]),
             Button("info", "../imgs/gui-tutorial/info-tutorial.png", SCREEN_DISPLAY, [307,246])
             ]

# Set up CreditsMenu
list_credits = [ Button("logo", "../imgs/title/logo-small.png", SCREEN_DISPLAY, [446,72]),
             Button("title", "../imgs/title/title-credits.png", SCREEN_DISPLAY, [528,162]),
             Button("back", "../imgs/btn-reuse/btn-back-small.png", SCREEN_DISPLAY, [50,600]),
             ]

# Set up Pause
list_pause = [ Button("logo", "../imgs/title/logo-small.png", SCREEN_DISPLAY, [446,72]),
             Button("title", "../imgs/title/title-paused.png", SCREEN_DISPLAY, [528,162]),
             # Pause Buttons
             Button("resume", "../imgs/gui-pause/btn-resume.png", SCREEN_DISPLAY, [401,310]),
             Button("restart", "../imgs/gui-pause/btn-restart.png", SCREEN_DISPLAY, [401,392]),
             Button("menu", "../imgs/gui-pause/btn-menu.png", SCREEN_DISPLAY, [401,473]),
             Button("quit", "../imgs/gui-pause/btn-quit-long.png", SCREEN_DISPLAY, [401,555]),
             ]

# Create dictionaries of menu buttons
dict_main = create_btn_dict(list_main)
dict_mode = create_btn_dict(list_mode)
dict_lb = create_btn_dict(list_lb)
dict_tut = create_btn_dict(list_tut)
dict_credits = create_btn_dict(list_credits)
dict_pause = create_btn_dict(list_pause)
# dict_play = create_btn_dict(list_play)
   
# Create leaderboards for classic (0) and survival mode (1)
lb_modes = [Leaderboard(), Leaderboard()]

MODE_MENU = ModeMenu("../imgs/bkg/bkg-original-720.png", SCREEN_DISPLAY, dict_mode)
TUTORIAL = TutorialMenu("../imgs/bkg/bkg-original-720.png", SCREEN_DISPLAY, dict_tut)
LB_MENU = LBMenu("../imgs/bkg/bkg-original-720.png", SCREEN_DISPLAY, dict_lb, lb_modes)
CREDITS = CreditsMenu("../imgs/bkg/bkg-original-720.png", SCREEN_DISPLAY, dict_credits)
PAUSE_MENU = PauseMenu("../imgs/bkg/bkg-original-720.png", SCREEN_DISPLAY, dict_pause)

MAIN = MainMenu("../imgs/bkg/bkg-original-720.png", SCREEN_DISPLAY, dict_main, LB_MENU, TUTORIAL, CREDITS, MODE_MENU)
