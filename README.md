[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588368&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

#  Air Hockey Mania 
## CS110 Final Project  Spring, 2024

## Team Members

Daniel Sirota and Julian Bakula
-dsirota@binghamton.edu
-jbakula1@binghamton.edu
** WE JOINED INTO A TEAM AFTER THE REPOSITORIES WERE ALREADY MADE AND FORGOT TO FILL OUT THE TEAM GOOGLE FORM. WE HAVE THE SAME CODE AND THE SAME PROJECT AS WE WORKED ON IT TOGETHER BUT WE ARE SUBMITTING TWICE IN EACH OF OUR INDIVIDUUAL REPOSITORIES AS WE DO NOT HAVE A SHARED ONE.

## Project Description

The project is a simulation of a simple and well known arcade game known as air hockey. Two players use bumpers on a "icey" surface to knock a puck aorund within a rectangular space until the puck goes past either player's bumper. They would then restart and keeping playing until somebody score three times. The winner is declared and they can play as many times as they want until they are happy with the result.

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Home Screen
2. Game Screen (including score)
3. Bumpers
4. Puck
5. Game Over Screen

### Classes

- Puck: The puck class creates the puck and takes in three arguments (x location, y location, and radius). This class also has a method that moves the puck across the screen and a reset method that resets the puck to the middle of the screen.

- Bumper: The bumper class creates a bumper and takes in multiple arguments (x location,y location, the color of the bumper, the width of the bumper, and the height of the bumper). The paddle has a move method that moves right when the direction that it takes in is "right" and left when the direction is "left". The Bumper class also has a reset method that resets the bumper to its starting position.

- Controller: The Controller class creates the entire program and puts all of the different classes together so they have a purpose and use. The Controller class has the following methods:

    init(): Initializes all of the objects and variables used in the program.

    startscreenloop(): Creates the home screen with all of the information on the screen that opens right when the program is ran.

    score(): Responsible for displaying the score on the screen.

    ameloop(): Creates and organizes everything that is used in the actual game. This includes but is not limited to drawing the game board, accounting for collisions between the ball, paddle, and walls, and changing the score when a goal is scored.

    endscreenloop(): Creates the end screen that displays the winner of the game and the final score when one of the teams reaches the maximum score.

    mainloop(): Responsible for changing the screens based on what state the program is in.

- Screen: The screen class creates multiple various screens throughout the game. The class has the following methods: 

    init(): initializes the window necessary for any screen to be displayed

    startscreen(): displays the starter screen that displays the instructions as well as the name of the game

    gamescreen(): displays the creen on which the game itself is played and draws a line through the middle of the screen as part of the game screen

    endscreen(): displayes a screen signifying that the game is over and displays the winner of the game as well as the final score of the game

## ATP
Test Case #1: Bumper Movement 
Check to see if the bumpers slide left and right as intended.

Steps to Test: Launch the software. To start the game, press the Space Bar. Press the arrow key to the right. Make sure the right-hand blue bumper moves. On the left arrow key, press. Make sure the left-hand blue bumper moves. Press the "d" key. Check to see if the red bumper shifts right. Press the "a" key. Make sure the left-hand red bumper moves.

Anticipated Result: In reaction to keyboard key inputs, the bumpers ought should shift to the left and right.


Test Case #2: Hitting the Bumper
Check that the puck bounces off the bumpers in this test description.

Steps to Test: Launch the software. To start the game, press the Space Bar. To start the game, press the Space Bar. To make the puck bounce off the first bumper, move it. Make sure the puck bounces off the bumper by checking. To make the puck bounce off this bumper, move the other bumper. Check to make sure the puck bounces off this bumper.

Expected Result: The puck should bounce off each bumper when the space bar is first pressed.


Test Case #3: The Direction and Overall Movement of the Puck
Check to see if the puck moves on the screen accurately at first.

Steps to Test: Launch the software. To start the game, press the Space Bar. To start the game, press the Space Bar. Never adjust the bumpers or paddles. Make sure the puck is moving on the screen.

Expected Result: Depending on how the puck bounces off the bumpers, it should travel across the screen when the space bar is first pressed.


Test Case #4: The Ending After Someone Scores 3 Points
Verify that the screen transitions to the final screen upon a player's achievement of three goals in the test description.

Steps to Test: Launch the software. To start the game, press the Space Bar. To start the game, press the Space Bar. Continue playing until a player reaches three points. Make sure the final score and the player who won the game appear on the screen.

Anticipated Result: The ultimate score and the player who won the game are displayed on the screen after a player reaches three points.


Test Case #5: The Scoring System of the Game
Test description: Verify that if a goal is scored, all the necessary adjustments are made.

Steps to Test: Launch the software. To start the game, press the Space Bar. To start the game, press the Space Bar. Permit the puck to go through a bumper. Check to see if the score of the other player rises by one. Make sure the puck returns to the center of the screen, just as it did when the game started. To start the game again, press Space Bar. Permit the puck to get beyond the opposing bumper. Check to see if the score of the other player rises by one. Make sure the puck returns to the center of the screen, just as it did when the game started.

Anticipated Result: The puck resets to the center of the screen, just as it did at the start of the game, and the opposing player's score increases by one when it passes a bumper.