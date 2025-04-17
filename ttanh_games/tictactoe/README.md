# Tic-tac-toe Game

## Description
Tic-tac-toe is a classic board game for two players, X and O. The players take turns marking spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## How to Play

1.  Navigate to the game's directory:
    ```bash
    cd src/games/tictactoe/
    ```
2.  Run the game:
    ```bash
    poetry run python main.py
    ```
3.  Players take turns entering the number of the square they want to mark (1-9).
4.  The first player to get three in a row wins.
5.  If all squares are filled and no one has three in a row, the game is a draw.

## Features

*   Two-player mode: Play against a friend.
*   3x3 grid: The game is played on a 3x3 grid.
*   Turn-based gameplay: Players take turns marking spaces.
*   Win detection: The game detects when a player has won.
*   Draw detection: The game detects when the game is a draw.

## Future Enhancements

*   Single-player mode against an AI opponent.
*   Different grid sizes.
*   Graphical interface.
*   Score tracking.
*   Online multiplayer.
