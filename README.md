# Tournament Chess Program

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Main Table of Contents</summary>
  <ol>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#gitbash">Gitbash</a></li>
    <li><a href="#installation-on-windows">Installation on Windows</a></li>
    <li><a href="#installation-on-linux">Installation on Linux</a></li>
    <li><a href="#installation-on-mac">Installation on Mac</a></li>
    <li><a href="#libraries">Libraries</a></li>
    <li><a href="#demonstration">Demonstration</a></li>
  </ol>
</details>


### This program allows you to 🠋

- Create tournaments or players and save them in a database.

- Pair players for a tournament on a four-round basis according to the Swiss tournament system

- To stop the tournament between two rounds and to resume the tournament

- Record the scores of the players in a database

- Change a player's ranking at any time

- To have a report menu for the information of a player or a round or a tournament

*See below for a* <a href="#demonstration">Demonstration</a>

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

__1- Launch the program with this command in your virtual env :__

- ```py main.py```

When the program is started, the main menu is displayed.

There are three different menus in the program.

See the three drop-down menus below for an example of each menu option.

<details>
  <summary><b>MAIN MENU</b></summary>

<li><a href="#create-a-tournament">Create a tournament</a></li>
<li><a href="#add-players-to-a-tournament">Add players to a Tournament</a></li>
<li><a href="#launch-or-continue-a-tournament">Launch or continue a tournament</a></li>
<li><a href="#add-player-to-database">Add player to database</a></li>
<li><a href="#modify-player-general-score">Modify player general score</a></li>
<li><a href="#report-menu">Report menu</a></li>
<li><a href="#exit-the-program">Exit the program</a></li>

![image](https://user-images.githubusercontent.com/81369778/136022869-22b1f44c-b777-46e4-9f4b-4c334afbe9a0.png)

## Create a tournament

¤ ***THE PROGRAM WILL ASK YOU :***
- The name
- The place
- The start and end date
- The time between tour
- The description

...and will save the tournament into the database.

![image](https://user-images.githubusercontent.com/81369778/136024702-b5e2a6e7-1aeb-4160-bffc-27826356c941.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>  
  
## Add players to a Tournament

¤ ***THE PROGRAM WILL SHOW YOU ALL THE TOURNAMENTS
AND WAIT YOU CHOOSE TOURNAMENT ID FOR ADD PLAYERS 🠋***

![image](https://user-images.githubusercontent.com/81369778/136026037-f0a6370e-428d-4f8f-b940-3eaea5b41beb.png)

¤ ***NOW YOU HAVE TO SELECT 8 PLAYERS ID 🠋***

![image](https://user-images.githubusercontent.com/81369778/136026617-9a513a54-59df-4e91-abb5-3e4b91040ae1.png)

¤ ***AFTER THAT THE LIST OF SELECTED PLAYERS IS DISPLAYED 🠋***

![image](https://user-images.githubusercontent.com/81369778/136037072-357847c4-6f50-411b-bc88-3a33c729d4de.png)

## Launch or continue a tournament

## Add player to database

¤ ***THE PROGRAM WILL ASK YOU :***
- The first name
- The last name
- The birthday
- The genre

...and will save the player into the database.

![image](https://user-images.githubusercontent.com/81369778/136023836-f68d5432-e6f1-4aeb-8385-d900e0da2640.png)

## Modify player general score

## Report menu

¤ ***GO TO THE***
<a href="#report-menu">REPORT MENU</a>

## Exit the program

¤ ***SIMPLY EXIT THE PROGRAM***
</details>
  
<details>
  <summary><b>REPORT MENU</b></summary>

<li><a href="#show-all-tournaments">Show all tournaments</a></li>
<li><a href="#show-all-saved-players">Show all saved players</a></li>
<li><a href="#show-players-of-specific-tournament">Show players of specific tournament</a></li>
<li><a href="#show-round-report-menu-of-specific-tournament">Show round report menu of specific tournament</a></li>
<li><a href="#back-to-the-main-menu">Back to the main menu</a></li>

![image](https://user-images.githubusercontent.com/81369778/136050952-cace051e-2370-4967-8742-f1aecd4bf530.png)

## Show all tournaments

## Show all saved players

## Show players of specific tournament

## Show round report menu of specific tournament

## Back to the main menu
 
</details>

<details>
  <summary><b>ROUND REPORT MENU</b></summary>

  
<li><a href="#show-all-rounds-results">Show all rounds results</a></li>
<li><a href="#show-round-x-results">Show round X results</a></li>
<li><a href="#back-to-the-report-menu">Back to the report menu</a></li>

![image](https://user-images.githubusercontent.com/81369778/136052754-13420d89-8f89-463a-9d51-e2ab289c99a7.png)

## Show all rounds results

## Show round X results

## Back to the report menu
  
</details>
