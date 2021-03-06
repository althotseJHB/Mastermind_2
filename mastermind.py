import random

def get_code():
    """
        CPU generates the code
    """
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return (code)


def display_message():
    """Displays the instructions for the user"""
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def display_position(correct_digits_and_position, correct_digits_only):
    """
        Displays the number of correct numbers and
        the number of numbers in the code, but in
        the wrong position.
    """
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))



def end_message(correct_digits_and_position, turns):
    """
        Displays a messages at the end of the game
    """

    correct = False
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))
    return (correct)


def code_breaker(code):
    """
        Where the magic happens;-)
        Game play begins
    """

    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1
        display_position(correct_digits_and_position, correct_digits_only)
        turns += 1
        correct = end_message(correct_digits_and_position, turns)


# TODO: Decompose into functions
def run_game():

    code = get_code()
    display_message()
    code_breaker(code)
    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()
