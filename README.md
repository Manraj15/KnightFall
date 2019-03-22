# KnightFall

![menu-image](imgs/Menu_Screenshot.png?raw=true)

## Introduction

KnightFall is an implementation of Bejewelled, a game originally made by PopCap in 2001. KnightFall is made using ```Python``` and ```PyGame```.

## Installation
To run KnightFall, you must download either Python 3.6 or Python 3.7. You can do this from either the [Python.org website](https://www.python.org/downloads/) or, if you have Homebrew installed, you can run the following commands (OSX  users only):

    $ brew install python3
    
Next, you must install PyGame. This can be done using pip:

    $ python3 -m pip install -U pygame --user
    
Where the ```user``` flag installs ```PyGame``` in the home directory rather than globally.

Now, download or clone the KnightFall repo. Then, change directory to KnightFall. Now, run the following command in temrinal:

    $ python3 KnightFall.py

## Player Manual
The objective of KnightFall is to align as many objects as possible either vertically or horizontally. This is done by clicking on an item, and then clicking on an adjacent with which you will like to swap the previously clicked item with. Any row(s) of similar items of length greather than or equal to 3 will then be collapsed and counted as points. Newly generated items will then take the place of the collapsed items. You will gain 10 points for each item that is collapsed. For example, if you are able to match a row of 4 of the same adjacent items, you will recieve 40 points.

Each game in KnightFall is 2 minutes long. Once the time runs out, your score will be recorded. Moreover, you will be notified if your current score is the new high score.

## Directory Structure

```src```: Contains all the source files for KnightFall

```imgs```: Contains the images used as icons in the game board

## Code Structure
KnightFall's source code contains 3 major classes: ```BoardModel```, ```Items```, and ```View```

### BoardModel
The ```BoardModel``` class is in the BoardModel.py file. It is used to represent the current state of the
board game and update it according to the moves a user makes. The current implementation of
BoardModel.py has three attributes:

* ```board```: A two-dimensional array in which each element of the array contains an Item on the
  board
  
* ```num_points```: The current number of points the user has scored

* ```num_possible_moves```: the number of possible moves a user can make

The ```BoardModel``` class currently has five methods a client can use:

* ```__init__()```: This method is automatically called when a BoardModel is instantiated. Upon
instantiating, ```__init__``` will simply call the make_board() method
* ```make_board()```: The make_board method is responsible for generating the current state of
the board. It does so by using an outer and inner loop, each of which runs seven times to
generate a total of 49 positions. Each of these positions is filled with a randomly generated
number from 1 to 4. Each of these numbers correspond to a specific Item
* ```update_num_points(num_points)```: The ```update_num_points``` method is used to update the
number of points the User currently has. It takes one Integer argument called ```num_points```,
which is the number of points to be added to the Users current score
* ```get_num_points()```: The ```get_num_points``` method is used to get the number of points a
User currently has
* ```get_board()```: The get_board method is used to get the current state of the board game.
It simply returns the board attribute

### Items
The ```Item``` class can be found in the Items.py file. The ```Item``` class is not meant to be instantiated
by itself. Instead, it should only be used as a parent to classes representing a specific type of ```Item```.
By doing so, it becomes much easier to make different kind of items, such as swords, shields, or
crowns.The ```Item``` class currently has 4 attributes:

* ```img_path```: The file path to the image icon of the item
* ```points```: The number of points this item is worth
* ```xcoord```: The x coordinate of the item on the gameboard
* ```ycoord```: The y coordinate of the item on the gameboard

The Item class currently supports 3 methods:

* ```__init__(img_path, points, xcoord, ycoord)```: This method is automatically called when an
object of type Item is instantiated. It accepts the arguments (from left to right): the image
path of the file, the number of points it is worth, its x coordinate, and its y coordinate.
* ```get_path()```: returns the img_path of the Item
* ```get_points()```: returns the amount of points the Item is worth

### ViewController

The ```ViewController``` class can be found in ViewController.py. It is responsible for displaying the game board as well as the main menu and all other user facing parts of the game. Currently, it contains 5 methods:

* ```__init__()```: called upon instantiation of the game
* ```_set_bkg```: Sets the background image of the Menu
* ```_display_elements```: Displays all the items on the board
* ```_handle_btn_events```: Handles all clicks on buttons and other interfaces on the view
* ```display_GUI```: Displays the GUI of the game

Classes that inherit from ViewController: 

* TutorialMenu : This menu contains the basic instructions to play the game KnightFall.

* LBMenu : LBMenu (Leaderboards Menu) contains a list of Leaderboard instances. Since KnightFall has two modes, 
classic and survival, the original list contains two Leaderboard objects. 
Note that the Leaderboard class is for keeping track of the top scores information while LBMenu is for displaying them. 

* CreditsMenu : This menu displays a list of main contributors of the game KnightFall.

#### MainMenu

The ```MainMenu``` class inherits from ```ViewController```. The purpose of this class is to initialize the main menu buttons and handle its functions. The attributes are other menus that are accessible through the main menu. The current four attributes are:

* ```mode_menu```: an instance of ```ModeMenu```
* ```lb```: an instance of ```LBMenu``` leaderboard menu
* ```tut```: an instance of ```TutorialMenu```
* ```credits```: an instance of ```CreditsMenu```

The methods are: 

* ```_display_elements()```: Shows buttons on main page (start, tutorial, leaderboard, credits and quit)
* ```_handle_btn_events()```: Selects the appropriate menu to display or exits the game

#### ModeMenu

The ```ModeMenu``` class and all its attributes inherits from ```ViewController```. It displays the options of game modes or returns to the main menu. The buttons on the mode selection page are: survival, classic and back. The methods are: 

* ```_display_elements()```: Displays its buttons (Classic, Survival and Back)
* ```_handle_btn_events()```: Selects the view of the game mode or returns back to main menu

#### PauseMenu

The ```PauseMenu``` class inherits from ```ViewController```. Its purpose is to display the pause menu and initializes the buttons.

* ```_display_elements()```: Displays its buttons (Restart, Resume, Menu, Quit)
* ```_handle_btn_events()```: Selects the appropriate visual interface to display

#### Leaderboard
The Leaderboard class is meant to keep track of the top 5 high scores earned in a game mode in KnightFall. 
Typically, there are two Leaderboards created since there are two game modes: classic and survival.
	
When the game session is over (time is up), the Leaderboard will check if the score earned by the user 
qualifies to be in the top 5 Leaderboard. If yes, this new score will be added. Depending on how many 
scores are currently saved on the Leaderboard for a game mode, Leaderboard can delete lower scores to 
make room for the new high score.

Basic Leaderboard methods:
* ```add_score()``` : add a new_score to the Leaderboard in the correct place if new_score makes the top 5. 
* ```pop_lowest_score()``` : Pop the lowest score on the Leaderboard iff high_scores is not empty.
* ```get_high_scores()``` : return the Leaderboard's high_scores list.
* ```save_leader_rank_in_txt()``` : write the leaderboard's info into a txt file

#### Button
The Button class creates a visual button from an image file.
* ```is_hover()``` : checks if the cursor is hovering over Button
* ```is_clicked()``` : checks if the button is clicked
* ```set_action()``` : set the action performed by button if activated
* ```call_action()``` : returns the button's action
* ```display_button()``` : display the button on the screen

## Extending the Code
Adding new items of your choice is easy with the modular and extendable design of KnightFall's source code. All item's shpuld inherit from the ```Item``` class, which provides basic functionality for a given item. For example, let's say you wanted to add a ```helmet``` item. It can be done int he following way:


    class Helmet(Items):
        def __init__(img_path, points, xCoord, yCoord):
            super().__init__(img_path, points, xCoord, yCoord)
        # Now have access to methods such as get_path and get_points. Now, add 
        # new method called change_helmet
        def change_helmet(new_path):
            self.path = new_path
 
New game modes can be created by building on the code for the base modes classic and survival. The structure is up to the person extending the game. Menus must be modified (add the new mode to the mode menu and update button linking) and a leaderboard for the new mode must be created.

The Button class allows others to create buttons that function using the set_action and call_action methods. A function or value can be defined outside of a class and set to the button's action so that call_action returns this function or value.
 
 ## Licence
 
 This game is made by [Jheyzelle](https://github.com/Jheyzelle), [YoshHau](https://github.com/YoshHau), [Manraj15](https://github.com/Manraj15), [EvanGi](https://github.com/EvanGi), and [davidysding](https://github.com/davidysding) under the [MIT Licence](https://mit-license.org/). 
 
 All artwork is taken from [Wallpaperplay](https://wallpaperplay.com/board/medieval-desktop-wallpapers). Original images can be found here:
 
 * [background](https://wallpaperplay.com/walls/full/e/a/e/113798.jpg#.XJQHtXftdvA.link)
 * [theme](https://wallpaperplay.com/walls/full/3/3/e/113796.jpg#.XJQHtSUu6kc.link)
