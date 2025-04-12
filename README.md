# Classic Games POC

## Description
This project is a proof-of-concept (POC) for several classic games written in Python using the Pygame library.

## Games Included
- Pong  
- Tic-tac-toe  
- Breakout  
- Snake  

## Installation Guide
1. Install Python 3.x  
2. Install Poetry  
3. Clone the repository  
4. Run `poetry install` to install dependencies  

## How to Play

1. Pong  
    ```bash
    poetry run python src/games/pong/main.py
    ```

2. Tic-tac-toe  
    ```bash
    poetry run python src/games/tictactoe/main.py
    ```

3. Breakout  
    ```bash
    poetry run python src/games/breakout/main.py
    ```

4. Snake  
    ```bash
    poetry run python src/games/snake/main.py
    ```

## Code Formatting & Linting

Before committing, ensure your code meets formatting and linting standards using:

```bash
poetry run isort .
poetry run black .
poetry run flake8 --max-line-length=88 --extend-ignore=E203,W503 .
```
