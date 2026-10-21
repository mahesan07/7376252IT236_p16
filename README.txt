QUIZ GAME WITH LEADERBOARD
==========================

ABOUT
-----
This is a simple terminal-based quiz game built using Python. Players select a topic, answer multiple-choice questions, and receive a score. After all players finish, a leaderboard displays their scores from highest to lowest.

FEATURES
--------
- Supports multiple players.
- Includes three topics:
  1. Python
  2. General Knowledge
  3. Mathematics
- Contains five sample questions for each topic.
- Checks answers and calculates scores.
- Displays a leaderboard sorted by score.
- Handles invalid player counts and answer choices.

PROJECT FILES
-------------
main.py
    Runs the quiz, accepts player input, calculates scores, and displays the leaderboard.

question.py
    Stores questions and correct answers, displays available topics, and provides questions to main.py.

REQUIREMENTS
------------
- Python 3
- No additional libraries required.

HOW TO RUN
----------
1. Keep main.py and question.py in the same folder.
2. Open a terminal in that folder.
3. Run the following command:

   python3 main.py

HOW TO PLAY
-----------
1. Enter the number of players.
2. Select a topic using its number.
3. Each player enters their name.
4. Answer each question by entering 1, 2, 3, or 4.
5. After all players finish, view the leaderboard.

SCORING
-------
- Each correct answer gives one point.
- Incorrect answers do not add points.
- Players are ranked from highest score to lowest score.

NOTES
-----
- Make sure the question file is named exactly question.py because main.py imports it using "import question".
- Scores are stored only while the program is running.
- Scores are not saved after the program closes.

AUTHOR
------
Created as a beginner-friendly Python project to practice functions, loops, lists, input handling, and sorting.
