from ViewController import *

class PauseMenu(ViewController):
    '''
    The PauseMenu options are resume, restart, menu, and quit.
    '''

    def __init__(self, bkg_img, view, btn_dict):
        '''
        Create the pause menu for the game KnightFall.
        '''
        ViewController.__init__(self, bkg_img, view, btn_dict)

    def _display_elements(self):

        self.btn_dict.get("title").display_button()
        self.btn_dict.get("logo").display_button()
        
        self.btn_dict.get("resume").display_button()
        self.btn_dict.get("restart").display_button()
        self.btn_dict.get("menu").display_button()
        self.btn_dict.get("quit").display_button()

    def _handle_btn_events(self, cursor, event):

        if self.btn_dict.get("resume").is_clicked(cursor, event):
            return 0
        elif self.btn_dict.get("restart").is_clicked(cursor, event):
            return "restart"
        elif self.btn_dict.get("menu").is_clicked(cursor, event):
            return "menu"
        elif self.btn_dict.get("quit").is_clicked(cursor, event):
            return 1
