# Wordle Simulation
#### Video Demo: https://youtu.be/Q0ol2NMCUhA
#### Description:
In this project, I recreated the Wordle game. In this game, the player must guess a five-letter English word within six attempts. After each guess, the game provides feedback to help the player gradually deduce the correct answer. The project consists of four files, including a .txt file.
### File: project.py

#### Function: main
=> Handles the overall flow of the game, including:
- Introduction, gameplay instructions, and main menu.
- Uses a while loop to allow the player to play again or exit after finishing each game round.
#### Function: wordle
=> Runs one full game session, including setup and main gameplay.
**Setup phase:**
- Chooses the answer word randomly from a list of five-letter words read from words.txt using the random library.
- Prepares several lists: Incorrect letters, entered words (to display them later), word states (to show colors for feedback)
- Initializes a counter for the number of attempts.
**Main phase:**
- Loops from 0 to 5 (maximum of six attempts).
- In the first attempt, gets input via the type_word function, which validates and stores it in the lists. Compares it to the answer using the check_word function, returning its state.
- If the guess is correct, it displays the result and breaks the loop; otherwise, the attempt counter increases.
- From the second attempt onward, the terminal is cleared using the os library. The program then prints: incorrect letters, all previously entered words with their color-coded states (using functions from colors.py).
After six attempts, if the player hasn’t guessed the word, the loop ends and the result is displayed.

#### Function: type_word
=> Ensures the user input is valid.
- Uses an infinite while loop until the input meets the correct format.
- Validates input with re.search() from the re library.
- If valid, checks whether the word exists in the word list.
- If invalid, displays a message and prompts the player to re-enter.

#### Function: check_word
Determines the state of the guessed word compared to the answer.
- Uses three symbols: "v": correct letter in the correct position; ".": correct letter in the wrong position; "x": incorrect letter
=> These states are stored for easy display later.
- Uses two dictionaries: t: counts the occurrences of each letter in the guessed word. num: counts the occurrences of letters in the answer word, excluding those already correctly matched ("v") to avoid duplication errors.
- A for loop checks each position: If the letters match → add "v". If not, check whether the letter exists in the answer word; if yes, verify that its occurrence count in t + 1 ≤ its count in num → add "."; otherwise, add "x". If it doesn’t exist in the answer → add "x" and update the incorrect-letter list if needed.
- Finally, returns the full state string.

### File: colors.py
=> Uses the colorama library to display color-coded text for different letter states.
Includes helper functions for color printing, handling both positions < 5 and the final position correctly.

### File: test_project.py
=> Contains test functions to verify the accuracy of the check_word function and ensure it returns the correct states.
Other aspects of the program are already validated by their respective functions.

### File: words.txt
=> Contains a list of five-letter English words used to verify input validity and provide the random answer word for the game.

### Libraries Used
- Built-in libraries: random, re, sys, os
- External library: colorama (install using pip install colorama)

