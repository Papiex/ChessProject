# Tournament Chess program

  * [Requirements](#requirements)
  * [Gitbash](#gitbash)
  * [Installation on Windows](#installation-on-windows)
  * [Installation on Linux](#installation-on-linux)
  * [Installation on Mac](#installation-on-mac)
  * [Libraries](#libraries)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


#### This program allows you to :

- Create tournaments or players and save them in a database.

- Pair players for a tournament on a four-round basis according to the Swiss tournament system

- To stop the tournament between two rounds and to resume the tournament

- Record the scores of the players in a database

- Change a player's ranking at any time

- To have a report menu for the information of a player or a round or a tournament

*See below for a demonstration*

## Requirements
This script is write with Python 3 and require minimum :
```bash
Python 3.9.0
```
## Gitbash
You have to clone the deposit with this command on gitbash and naviguate to the develop branch :
```
git clone https://github.com/Papiex/ChessProject
```
```
git checkout develop
```
## Installation on Windows
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python -m venv env```

__2- Now you have to activate your virtual env, the default path is :__
- if you use PowerShell :
``` env/Scripts/activate.ps1```
- if you use CMD or terminal that supports __.bat__ :
``` env/Scripts/activate.bat```

## Installation on Linux
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python -m venv env```

__2- Now you have to activate your virtual env, the default path is :__
``` source env/bin/activate```

## Installation on Mac
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python -m venv env```

__2- Now you have to activate your virtual env, the default path is :__
``` source env/bin/activate```

## Libraries
__This program need some libraries, for installing them, use this command (in your virtual env) :__

*View requirements.txt to know which library/version is used*

- ```pip install -r requirements.txt```

# Demonstration

![image](https://user-images.githubusercontent.com/81369778/136022869-22b1f44c-b777-46e4-9f4b-4c334afbe9a0.png)

## MAIN MENU - TABLE OF CONTENTS
 * [ [1] Create a tournament](1-create-a-tournament)
 * [2 Add players to a Tournament](2-add-players-to-a-tournament)
 * [3 Launch or continue a tournament](3-launch-or-continue-a-tournament)
 * [4 Add player to database](4-add-player-to-database)
 * [5 Modify player general score](5-modify-player-general-score)
 * [6 Report menu](6-report-menu)
 * [7 Exit the program](7-exit-the-program)

## [1] Create a tournament

¤ ***THE PROGRAM WILL ASK YOU :***
- The name
- The place
- The start and end date
- The time between tour
- The description

...and will save the tournament into the database.

![image](https://user-images.githubusercontent.com/81369778/136024702-b5e2a6e7-1aeb-4160-bffc-27826356c941.png)

## [2] Add players to a Tournament :

¤ ***THE PROGRAM WILL SHOW YOU ALL THE TOURNAMENTS
AND WAIT YOU CHOOSE TOURNAMENT ID FOR ADD PLAYERS 🠋***

![image](https://user-images.githubusercontent.com/81369778/136026037-f0a6370e-428d-4f8f-b940-3eaea5b41beb.png)

¤ ***NOW YOU HAVE TO SELECT 8 PLAYERS ID 🠋***

![image](https://user-images.githubusercontent.com/81369778/136026617-9a513a54-59df-4e91-abb5-3e4b91040ae1.png)

¤ ***AFTER THAT THE LIST OF SELECTED PLAYERS IS DISPLAYED 🠋***

![image](https://user-images.githubusercontent.com/81369778/136037072-357847c4-6f50-411b-bc88-3a33c729d4de.png)

## [3] Launch or continue a tournament :

## [4] Add player to database :

¤ ***THE PROGRAM WILL ASK YOU :***
- The first name
- The last name
- The birthday
- The genre

...and will save the player into the database.

![image](https://user-images.githubusercontent.com/81369778/136023836-f68d5432-e6f1-4aeb-8385-d900e0da2640.png)

## [5] Modify player general score :

## [6] Report menu

¤ ***🠋SEE BELOW FOR ITS USE🠋***
             (link)

## [7] Exit the program

¤ ***SIMPLY EXIT THE PROGRAM***
