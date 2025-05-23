# Classic Games POC

## Description
This project is a proof-of-concept (POC) for several classic games written in Python using the Pygame library.

## Games Included
- Pong  
- Tic-tac-toe  
- Breakout  
- Snake  

## Installation Guide

**Using Conda**

1.  Install Conda: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
2.  Clone the repository
3.  Create a Conda environment from the `environment.yml` file:
    ```bash
    conda env create -f environment.yml
    ```
4.  Activate the Conda environment:
    ```bash
    conda activate classic-games
    ```
5. Install the main module:
    ```bash
    pip install -e .
    ```

**Using Pip**

1.  Install Python 3.x
2.  Clone the repository
3.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4.  Activate the virtual environment:
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
5.  Install the dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
6. Install the main module:
    ```bash
    pip install -e .
    ```

## How to Play with Game Launcher

After activate the virtual environment:

1.  Run the game launcher:
    ```bash
    python main.py
    ```
2.  Select a game from the menu.

Read each game's README file to know how to run individual game.

## Code Formatting & Linting

Before committing, ensure your code meets formatting and linting standards using:

```bash
isort .
black .
flake8 --max-line-length=88 --extend-ignore=E203,W503 .
```
