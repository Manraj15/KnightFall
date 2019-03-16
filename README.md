# KnightFall

## Introduction

KnightFall is an implementation of Bejewelled, a game originally made by PopCap in 2001. KnightFall is made using ```Python``` and ```PyGame```.

## Installation
To run KnightFall, you must download either Python 3.6 or Python 3.7. You can do this from either the [Python.org website](https://www.python.org/downloads/) or, if you have Homebrew installed, you can run the following commands (OSX  users only):

    $ brew install python3
    
Next, you must install PyGame. This can be done using pip:

    $ python3 -m pip install -U pygame --user
    
Where the ```user``` flag install ```PyGame``` in the home directory rather than globally.

## Player Manual
The objective of KnightFall is to align as many objects as possible either vertically or horizontally. This is done by clicking on an item, and then clicking on an adjacent with which you will like to swap the previously clicked item with. Any row(s) of similar items of length greather than or equal to 3 will then be collapsed and counted as points. Newely generated items will then take the place of the collapsed items. You will gain 10 points for each item that is collapsed. For example, if you are able to match a row of 4 of the same adjacent items, you will recieve 40 points.

Each game in KnightFall is 2 minutes long. Once the time runs out, your score will be recorded. Moreover, you will be notified if your current score is the new high score.

## Directory Structure

```src```: Contains all the source files for KnightFall
```imgs```: Contains the images used as icons in the game board

## Code Structure
KnightFall's source code contians 3 major classes: ```BoardModel```, ```Items```, and ```View```

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

## Extending the Code
Adding new items of your choice is easy with the modular and extendable design of KnightFall's source code. All item's shpuld inherit from the ```Item``` class, which provides basic functionality for a given item. For example, let's say you wanted to add a ```helmet``` item. It can be done int he following way:


    class Helmet(Items):
        def __init__(img_path, points, xCoord, yCoord):
            super().__init__(img_path, points, xCoord, yCoord)
        # Now have access to methods such as get_path and get_points. Now, add 
        # new method called change_helmet
        def change_helmet(new_path):
            self.path = new_path
