# Battle Ships - Project Portfolio 3

## - By Bradley Hammond

### [View the live project here](https://battleships-p3p-d6bcfe559667.herokuapp.com/)

### [View the repository here](https://github.com/Brad-Hammond/BattleShips/settings/pages)

## Table of Contents

![Overview of Game](assets/images/LoadingImage.png)

### About my Game

This is my command line Battle Ships game which allows the user to play against the computer by guessing it's fleets locations.

This game is run on the Code Institute mock terminal on heroku.

### How to Play

- Once the program is ran, the user can input their name and view the game instructions by typing "yes" in the terminal.
- The instructions inform the user of how to play the game.
- The user then chooses their diffuculty (easy, medium or hard).
- The user then choses their grid size, please note that the smallest size can be 3x3 and the largest 10x10.
- Once the user proceeds with desired grid size, they then start the game loop.
- Once the user has correctly guessed and sunk the enemies ships, they have won the game!
- If they miss and run out of turns, they lose and the game is over.

### Flow Chart

![Flow Chart](assets/images/BattleShips%20Flow%20Chart.jpg)

### Features

#### Existing Features

- #### Button

![Run Button](assets/images/RunButton.png)

- This is the button that is already displayed via the Code Institute template I was given, which allows the user to play the game.

- #### Landing Screen
  ![Landing Screen](assets/images/LoadingImage.png)
- Once the programme is ran, the user is greeted with a landing page which has an image of a battle ship with the name of the game printed out for the user to see.

- #### Name Input
  ![Input Name](assets/images/InputName.png)
- The user is then promted to input their name, the name the user gives is then also used throughout the game in different scenarios.
- There is also input validation on the name input so the user cannot just press enter.

- #### Instructions
  ![View Instructions Prompt](assets/images/InstructionsYorN.png)
- The user is asked if they want to view the instructions, they have the option to press yes or no.
- This input has input validation on so the user either has to put "yes" or "no".
  ![Displayed Instructions](assets/images/InstructionsDisplayed.png)
- If the user choses to view the instructions, they are displayed as the above.
- The instructions tell the user how to play the game, and include the settings for the difficulty (e.g how many turns and that you cannot change once chose) <br> as well as the maximum and minumum grid sizes.

- #### Difficulty

![Difficulty Selection](assets/images/DifficultySelection.png)

- The user can chose what difficutly they want.
- This input has input validation on so the user can only type "easy", "medium" or "hard".
- The settings for each difficulty are explained in the instructions.
- Once the user has chose their difficulty, they cannot change unless they restart the programme.

- #### Board Size
  ![Preview Board Size](assets/images/PreviewGrid.png)
- The user has the option to chose their own grid size.
- This input also has input validation on.
- The prompt explains what format they must type it in, e.g 5 for a 5x5 grid.
- #### Preview Board Size
  ![Preview Board Size](assets/images/PreviewGrid.png)
- Once the user has chose, they can preview the board size and chose whether they want to continue or not.
- This input has input validation on, so the user can only type "yes" or "no".
- If the user does not like the board size, they are able to to type "no" and chose another size until satisfied.

- #### Game Start
  ![Lets Play BattleShips](assets/images/LetsPlayBattleShip.png)
- When the user starts the game, they are greeetd with "Let's play Battleships!" and their grid.
- At the top of the grid is the users turns and along the top and left hand side are the col and row numbers.
  ![Input Col and Row](assets/images/RowAndColumnIput.png)
- The user is then promted to input their row and column guesses.
- These inputs have input validation applied so they can only input valid integars.
- Please see below message for invalid input:
  ![Invalid Input](assets/images/InvRandCGuess.png)

- #### Hit and Miss
- When the user hits the ship, it is maked with "X", and the below message appears:
  ![Hit a Ship](assets/images/YouHitaShip.png)
- Once the user has sunk a ship, either size 2 or 3 - the below messages appear:
  ![Sunk 2 Unit Ship](assets/images/Sunk2UnitShip.png)
  ![Sunk 3 Unit Ship](assets/images/Sunk3UnitShip.png)
- Also, as the user sinks the ships, the below messages appear telling them how many remain:
  ![1 Ship Remaining](assets/images/OneShipRemaining.png)
  ![0 Ships Remaining](assets/images/ZeroShipsRemaining.png)
