# Tournament Chess Program

<li><a href="#requirements">Requirements</a></li>
<li><a href="#gitbash">Gitbash</a></li>
<li><a href="#installation-on-windows">Installation on Windows</a></li>
<li><a href="#installation-on-linux">Installation on Linux</a></li>
<li><a href="#installation-on-mac">Installation on Mac</a></li>
<li><a href="#libraries">Libraries</a></li>
<li><a href="#demonstration">Demonstration</a></li>

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

🠋See the three drop-down menus below for an example of each menu option🠋

<details>
  <summary><b>MAIN MENU</b></summary>

<li><a href="#1---create-a-tournament">1 - Create a tournament</a></li>
<li><a href="#2---add-players-to-a-tournament">2 - Add players to a Tournament</a></li>
<li><a href="#3---launch-or-continue-a-tournament">3 - Launch or continue a tournament</a></li>
<li><a href="#4---add-player-to-database">4 - Add player to database</a></li>
<li><a href="#5---modify-player-general-score">5 - Modify player general score</a></li>
<li><a href="#6---report-menu">6 - Report menu</a></li>
<li><a href="#7---exit-the-program">7 - Exit the program</a></li>

![image](https://user-images.githubusercontent.com/81369778/136022869-22b1f44c-b777-46e4-9f4b-4c334afbe9a0.png)

## 1 - Create a tournament

¤ ***THE PROGRAM WILL ASK YOU :***
- The name
- The place
- The start and end date
- The time between tour
- The description

...and will save the tournament into the database.

![image](https://user-images.githubusercontent.com/81369778/136024702-b5e2a6e7-1aeb-4160-bffc-27826356c941.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>  
  
## 2 - Add players to a Tournament

¤ ***THE PROGRAM WILL SHOW YOU ALL THE TOURNAMENTS
AND WAIT YOU CHOOSE TOURNAMENT ID FOR ADD PLAYERS 🠋***
- If database have no tournament, the program will raise an error

![image](https://user-images.githubusercontent.com/81369778/136026037-f0a6370e-428d-4f8f-b940-3eaea5b41beb.png)

¤ ***NOW YOU HAVE TO SELECT 8 PLAYERS ID 🠋***

![image](https://user-images.githubusercontent.com/81369778/136026617-9a513a54-59df-4e91-abb5-3e4b91040ae1.png)

¤ ***AFTER THAT THE LIST OF SELECTED PLAYERS IS DISPLAYED 🠋***

![image](https://user-images.githubusercontent.com/81369778/136037072-357847c4-6f50-411b-bc88-3a33c729d4de.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>  
  
## 3 - Launch or continue a tournament

¤ ***THE PROGRAM WILL SHOW YOU ALL THE TOURNAMENTS
AND WAIT YOU CHOOSE TOURNAMENT ID TO LAUNCHED 🠋***
- If database have no tournament, the program will raise an error

![image](https://user-images.githubusercontent.com/81369778/136172114-2ff6d040-ad7c-4161-a42a-244ea669028b.png)

¤ ***THE FIRST ROUND IS RUN ONLY IF 8 PLAYERS HAVE BEEN PREVIOUSLY ADDED TO THE TOURNAMENT SELECTED***

¤ ***NOW YOU HAVE TO ENTER EVERY MATCH RESULT FOR THE ROUND 1 ACCORDING TO THE BOARD***
- You only need to enter the result of the first player of players pair, the result of second player is
  automatically selected according to the result of the first player

![image](https://user-images.githubusercontent.com/81369778/136173207-ba3fea52-c03e-4dfc-af21-d5fcc4b4edf5.png)

![image](https://user-images.githubusercontent.com/81369778/136175079-b1ab532a-a326-4a52-acd6-ca1e4e6e000b.png)

¤ ***WHEN A ROUND IS FINISHED YOU HAVE TO CHOOSE IF YOU WANT TO CONTINUE TO THE NEXT ROUND OR EXIT AND SAVE🠋***
- If you choose to exit and save,
the next time you restart this tournament, you will continue in the round where you stopped
- When at least one round is finished you can view the report in the round report menu of this tournament

![image](https://user-images.githubusercontent.com/81369778/136175829-f29bf63e-c6fc-470e-861f-78119a1ec113.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>  
  
## 4 - Add player to database

¤ ***THE PROGRAM WILL ASK YOU :***
- The first name
- The last name
- The birthday
- The genre

...and will save the player into the database.

![image](https://user-images.githubusercontent.com/81369778/136023836-f68d5432-e6f1-4aeb-8385-d900e0da2640.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>  
  
## 5 - Modify player general score

¤***THE PROGRAM WILL SHOW YOU THE LIST OF ALL PLAYERS AND WAIT YOU TO CHOOSE
ID OF ONE PLAYER TO MODIFY HIS GENERAL RANKING🠋***
- After you enter the new score, the program display the new score of the player

![image](https://user-images.githubusercontent.com/81369778/136179371-51fbc1aa-e7ad-475f-b4ec-4cf9e509cb68.png)

![image](https://user-images.githubusercontent.com/81369778/136180493-fb24f919-0ee1-45a4-999b-387a1298b8ae.png)

![image](https://user-images.githubusercontent.com/81369778/136180554-73761747-0334-4414-ac36-ac8560af2d11.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>  
  
## 6 - Report menu

¤ ***GO TO THE***
<a href="#demonstration">REPORT MENU</a>

<li><a href="#demonstration">Click here for back to the table contents</a></li>  
  
## 7 - Exit the program

¤ ***SIMPLY EXIT THE PROGRAM***

<li><a href="#demonstration">Click here for back to the table contents</a></li>  
  
</details>

&nbsp;

&nbsp;

&nbsp;
  
<details>
  <summary><b>REPORT MENU</b></summary>

<li><a href="#1---show-all-tournaments">1 - Show all tournaments</a></li>
<li><a href="#2---show-all-saved-players">2 - Show all saved players</a></li>
<li><a href="#3---show-players-of-specific-tournament">3 - Show players of specific tournament</a></li>
<li><a href="#4---show-round-report-menu-of-specific-tournament">4 - Show round report menu of specific tournament</a></li>
<li><a href="#5---back-to-the-main-menu">5 - Back to the main menu</a></li>

![image](https://user-images.githubusercontent.com/81369778/136050952-cace051e-2370-4967-8742-f1aecd4bf530.png)

## 1 - Show all tournaments

¤***SHOW ALL TOURNAMENTS SAVED IN DATABASE🠋***

![image](https://user-images.githubusercontent.com/81369778/136192951-357076c9-fa3d-4cb6-9400-d7f72edc77a7.png)

<li><a href="#<summary><b>demonstration</b></summary>">Click here for back to the table contents</a></li>

## 2 - Show all saved players

¤***SHOW ALL PLAYERS SAVED IN DATABASE BY RANKING OR ALPHABETICAL ORDER🠋***

![image](https://user-images.githubusercontent.com/81369778/136193157-55b7faa0-d6a1-45dc-800d-961082562754.png)

![image](https://user-images.githubusercontent.com/81369778/136193200-556d8df6-a8d0-424d-919e-4df3f4f75d6f.png)

<li><a href="demonstration">Click here for back to the table contents</a></li>

## 3 - Show players of specific tournament

¤***THE PROGRAM WAIT YOU TO CHOOSE A TOURNAMENT ID FOR VIEW ASSOCIATED PLAYERS🠋***

![image](https://user-images.githubusercontent.com/81369778/136193432-2733e213-b24f-4b12-936e-99c5ae6817bd.png)

![image](https://user-images.githubusercontent.com/81369778/136193486-e32a754f-9689-4c58-a95f-002e9e9de004.png)

<li><a href="demonstration">Click here for back to the table contents</a></li>

## 4 - Show round report menu of specific tournament

¤ ***THE PROGRAM WAIT YOU TO CHOOSE A TOURNAMENT ID AND LOAD THE ROUND MENU REPORT OF THE SELECTED TOURNAMENT🠋***
- View the round report menu below too see an example of each round report menu option

![image](https://user-images.githubusercontent.com/81369778/136195601-7f21d9a7-0240-4189-88d4-3be3e04bb8de.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>

## 5 - Back to the main menu

¤***SIMPLY BACK TO THE MAIN MENU***

¤ ***GO TO THE***
<a href="#demonstration">MAIN MENU</a>

<li><a href="#demonstration">Click here for back to the table contents</a></li>

</details>

&nbsp;

&nbsp;

&nbsp;

<details>
  <summary><b>ROUND REPORT MENU</b></summary>

  
<li><a href="#1---show-all-rounds-results">1 - Show all rounds results</a></li>
<li><a href="#2---show-round-x-results">2, 3, 4, 5 - Show round X results</a></li>
<li><a href="#6---back-to-the-report-menu">6 - Back to the report menu</a></li>

![image](https://user-images.githubusercontent.com/81369778/136052754-13420d89-8f89-463a-9d51-e2ab289c99a7.png)

## 1 - Show all rounds results

¤***SHOW ALL ROUNDS RESULT OF THE SELECTED TOURNAMENT🠋***

![image](https://user-images.githubusercontent.com/81369778/136208089-65950399-861d-4a69-a914-31bdc04939ab.png)

![image](https://user-images.githubusercontent.com/81369778/136208171-2a9a8afd-e95a-4378-a66f-9b4d1a62633c.png)

![image](https://user-images.githubusercontent.com/81369778/136208216-bda23ec8-02ac-4668-8502-c4b85521c63d.png)

![image](https://user-images.githubusercontent.com/81369778/136208246-641ddf9c-bd5f-48e4-9040-0ef4f44afb39.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>

## 2 - Show round X results

¤***SHOW RESULT OF A SPECIFIC ROUND🠋***

![image](https://user-images.githubusercontent.com/81369778/136208216-bda23ec8-02ac-4668-8502-c4b85521c63d.png)

<li><a href="#demonstration">Click here for back to the table contents</a></li>

## 6 - Back to the report menu

¤***SIMPLY BACK TO THE REPORT MENU***

<li><a href="#demonstration">Click here for back to the table contents</a></li>

</details>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;
