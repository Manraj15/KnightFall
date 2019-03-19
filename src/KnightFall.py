from Initializer import *

class KnightFall():
    '''
    KnightFall is a matching game based on Bejeweled.
    '''

    def __init__(self):
        '''
        Run KnightFall.
        '''
        self.main = MAIN
        self.main.display_GUI()

KnightFall()

pygame.quit()
quit()
