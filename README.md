# Tic-Tac-Toe Game with AI

This Python program implements a Tic-Tac-Toe game where the player competes against an AI opponent. The AI has three difficulty levels: easy, medium, and hard. The game utilizes the PyFiglet library for ASCII art text rendering.

## Game Features
- Player vs. AI gameplay.
- AI difficulty levels: easy, medium, and hard.
- ASCII art rendering for a visually appealing user interface.
- Ability to quit the game at any time by entering 'q'.

## How to Play
1. Run the Python script.
2. Choose the difficulty level for the AI opponent (easy, medium, or hard).
3. Enter your moves by specifying the row (1, 2, or 3) and column (1, 2, or 3).
4. The AI will make its move, and the game continues until a winner is determined, the game ends in a draw, or the player decides to quit.

## AI Difficulty Levels
- **Easy:** The AI makes random moves.
- **Medium:** The AI attempts to make smart moves with a 70% chance of selecting a winning move or blocking the player's winning move.
- **Hard:** The AI uses the minimax algorithm to make optimal moves.

## Requirements
- Python 3.x
- PyFiglet library (install using `pip install pyfiglet`)

## Running the Program
To play the game:
1. Ensure you have Python installed on your system.
2. Install the PyFiglet library using `pip install pyfiglet`.
3. Run the Python script.

## Game Outcome
- If the player wins, a congratulatory message is displayed.
- If the AI wins, a message indicating defeat is displayed.
- If the game ends in a draw, a message indicating a tie is displayed.
- The player can choose to play again or quit the game after each round.

Enjoy playing Tic-Tac-Toe against the AI opponent!
