# changes

## 6/1/16
 - Cleaned up code
 - Attempted to create a user interface using Flask, and jquery, but failed.
 - Fixed more bugs

## 5/26/16
 - Squashed a bug that allowed the computer to play twice each round
 - Another bug was found that prevents the computer from defending the board. The cause still needs to be identified.

## 5/16/16
 - Added an option for a human to play a computer (class `HumanAIGame`). Note that it's still a little buggy (for example it played 2 moves in 1 turn one time).

## 5/15/16

 - Added a AI game - 2 computers that play eachother.
 - Refactored some methods. Changed some variables and methods to static (most notably `Cube.allowed`).

## 5/12/16
 - Created Board and Started Cube
 - Created all unit tests for Board
 - Created some unit tests for Cube
 - Added Continuous Integration for Unittests (Travis CI)
 - Added a small 2 player text based demo (`HumanGame`)
