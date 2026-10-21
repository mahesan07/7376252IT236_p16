questionData = {
    1: [
        [
            "What is the output of print(2 + 3)?",
            "1. 5",
            "2. 6",
            "3. 23",
            "4. 2",
        ],
        [
            "Which keyword is used to define a function in Python?",
            "1. function",
            "2. def",
            "3. fun",
            "4. define",
        ],
        [
            "Which data type stores True or False?",
            "1. int",
            "2. str",
            "3. bool",
            "4. list",
        ],
        [
            "Which symbol is used for comments in Python?",
            "1. //",
            "2. <!-- -->",
            "3. **",
            "4. #",
        ],
        [
            "Which method adds an item to the end of a list?",
            "1. add()",
            "2. append()",
            "3. insertEnd()",
            "4. push()",
        ],
    ],
    2: [
        [
            "Which planet is known as the Red Planet?",
            "1. Earth",
            "2. Venus",
            "3. Mars",
            "4. Jupiter",
        ],
        [
            "How many days are there in a leap year?",
            "1. 365",
            "2. 366",
            "3. 364",
            "4. 360",
        ],
        [
            "Which is the largest ocean on Earth?",
            "1. Atlantic Ocean",
            "2. Indian Ocean",
            "3. Arctic Ocean",
            "4. Pacific Ocean",
        ],
        [
            "What is the boiling point of water at sea level?",
            "1. 50 C",
            "2. 75 C",
            "3. 100 C",
            "4. 150 C",
        ],
        [
            "Which gas do plants mainly absorb for photosynthesis?",
            "1. Oxygen",
            "2. Carbon dioxide",
            "3. Nitrogen",
            "4. Hydrogen",
        ],
    ],
    3: [
        [
            "What is 7 * 8?",
            "1. 54",
            "2. 56",
            "3. 64",
            "4. 48",
        ],
        [
            "What is the square root of 81?",
            "1. 7",
            "2. 8",
            "3. 9",
            "4. 10",
        ],
        [
            "What is 15 + 27?",
            "1. 32",
            "2. 40",
            "3. 41",
            "4. 42",
        ],
        [
            "What is 100 / 4?",
            "1. 20",
            "2. 25",
            "3. 30",
            "4. 40",
        ],
        [
            "What is 9 squared?",
            "1. 18",
            "2. 72",
            "3. 81",
            "4. 99",
        ],
    ],
}

# Correct answer numbers match the option numbers shown above.
answerData = {
    1: [1, 2, 3, 4, 2],
    2: [3, 2, 4, 3, 2],
    3: [2, 3, 4, 2, 3],
}


def availableTopic():
    print("1. Python")
    print("2. General Knowledge")
    print("3. Mathematics")


# Return questions for the selected topic.
def questions(questionTopic):
    return questionData[questionTopic]


# Return correct answers for the selected topic.
def answer(questionTopic):
    return answerData[questionTopic]