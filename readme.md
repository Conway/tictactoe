# 3D TicTacToe


[![Build Status](https://travis-ci.org/Conway/tictactoe.svg?branch=master)](https://travis-ci.org/Conway/tictactoe)

---


This is a 3D game of Tic Tac Toe. Currently, 2 Humans can play against eachother, 2 computers can play against each other, or 1 human can play 1 computer.

---
##Writeup:

###Reflection

When I originally started this project, I didn't know how far I would be able to get, and I had no idea how to program a basic computer to play against. I was able to program three different gameplays: human v. human, computer v. computer and human v. computer. I also programmed unittests for some classes, and added continuous integration.

For this project, I had to learn how to write unittests, how to use git and how to use continuous integrations. I feel that I know all of these somewhat well now. These tools will also help me on future projects.

I found the manual testing to be challenging due to all of the possible rows that have to be accounted for. It also became difficult to manage some of the if/else statements in this program due to their size.

If I had more time, I would work on squashing bugs and adding some sort of visual interface. I had attempted to add a web interface using Flask, and updating the page with jquery, but was unable to make it work in the timeframe for this project. I had the website mocked up with clickable buttons, but they did not update on server response.

###Known Bugs

Sometimes the various AIs will not block a move. Users could find patterns and exploit them. However, it could also be thought of as a "feature" as no human player is perfect, either.

###Earned Grade

I feel that I deserve a 95%. Although this project seems basic, I learned many skills from it. I learned from my failures, built on my existing Python knowledge and learned how to use new packages and technologies.