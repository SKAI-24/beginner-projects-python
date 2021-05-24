"""
H A N G M A N
"""
import random

def hangman(word):
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    remaining_letters = list(word)
    board = ["__"] * len(word)
    win = False
    wrong = 0
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter of the word: "
        char = input(msg)

        if char in remaining_letters:
            x = remaining_letters.index(char)
            board[x] = char
            remaining_letters[x] = '$'
        else:
            wrong += 1

        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


possible_words = ["cat", "computer", "wire", "bike", "balls", "code", "destitute", "plane", "trees", "birds"]
solution = possible_words[random.randint(0,9)]

hangman(solution)
