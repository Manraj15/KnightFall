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
