from gametasks import print_instructions, get_user_score, update_user_score
from gameclasses import Game, MathGame, BinaryGame

try:
    math_instructions = '''
In this game, you will be given a simple arithmetic question.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.
'''

    binary_instructions = '''
In this game, you will be given a number in base 10.
Your task is to convert this number to base 2.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.
'''
    mg = MathGame()
    bg = BinaryGame()

    user_name = input("\nPlease enter your username: ")

    score = int(get_user_score(user_name))

    if score == -1:
        new_user = True
        score = 0
    else:
        new_user = False

    print("\nHello %s, welcome to the game." % user_name)
    print("Your current score is %d." % score)

    user_choice = 0

    while user_choice != '-1':
        game = input("\nMath Game (1) or Binary Game (2)?: ")
        while game != '1' and game != '2':
            print("You did not enter a valid choice. Please try again.")
            game = input("\nMath Game (1) or Binary Game (2)?: ")

        num_prompt = input(
            "\nHow many questions do you want per game (1 to 10)?: ")
        while True:
            try:
                num = int(num_prompt)
                break
            except IOError:
                print("You did not enter a valid number. "
                      "Please try again.")
                num_prompt = input(
                    "\nHow many questions do you want per "
                    "game (1 to 10)?: ")

        if game == '1':
            mg.no_of_questions = num
            print_instructions(math_instructions)
            score = score + mg.generate_questions()
        else:
            bg.no_of_questions = num
            print_instructions(binary_instructions)
            score = score + bg.generate_questions()

        print("\nYour current score is %d." % score)

        user_choice = input("\nPress Enter to continue or -1 to end: ")

    update_user_score(new_user, user_name, str(score))

except Exception as e:
    print("An unknown error occurred. Program will exit.")
    print("Error: ", e)
