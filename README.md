# High-Low-Game
The High Low Game is a simple betting game where the player bets credits on whether the next randomly generated number will be high (8-13) or low (1-6). If the number is 7, it's a tie.

## Files
- `main.py`: The main entry point of the game.
- `functions.py`: Contains all the functions used in the game.

## How to Play
1. Run the `main.py` file to start the game.
2. You start with 1000 credits.
3. Enter the number of credits you want to bet.
4. Choose whether the next number will be "High" or "Low".
5. The game will generate a random number between 1 and 13.
6. If your guess is correct, you win the bet amount. If it's a tie, you neither win nor lose credits. If your guess is incorrect, you lose the bet amount.
7. The game continues until you decide to stop or you run out of credits.

## Requirements
- Python 3.x
- `easygui_qt` library

## Installation
1. Clone the repository or download the files.
2. Install the required library using pip:
    ```sh
    pip install easygui_qt
    ```
    ```sh
    pip install easygui_qt
    ```
3. Run the game:
    ```sh
    python main.py
    ```

## Author
Neil Rathod
