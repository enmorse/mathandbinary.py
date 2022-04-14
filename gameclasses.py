class Game:
    def __init__(self, no_of_questions=0):
        self._no_of_questions = no_of_questions

    @property
    def no_of_questions(self):
        return self._no_of_questions

    @no_of_questions.setter
    def no_of_questions(self, value):
        if value < 1:
            self._no_of_questions = 1
            print("\nMinimum Number of Questions = 1")
            print("Hence, number of questions will be "
                  "set to 1")
        elif value > 10:
            self._no_of_questions = 10
            print("\nMaximum Number of Questions = 10")
            print("Hence, number of questions will be "
                  "set to 10")
        else:
            self._no_of_questions = value


class BinaryGame(Game):
    def generate_questions(self):
        from random import randint
        score = 0

        for i in range(self.no_of_questions):
            base10 = randint(1, 100)
            user_result = input("\nPlease convert %d to "
                                "binary: " % base10)
            while True:
                try:
                    answer = int(user_result, base=2)
                    if answer == base10:
                        print("Correct Answer!")
                        score = score + 1
                        break
                    else:
                        print(
                            "Wrong answer. The correct answer "
                            "is {:b}.".format(base10))
                        break
                except IOError:
                    print(
                        "You did not enter a binary number. "
                        "Please try again.")
                    user_result = input(
                        "\nPlease convert %d to binary: " % base10)

        return score


class MathGame(Game):
    def generate_questions(self):
        from random import randint
        score = 0
        number_list = [
            0,
            0,
            0,
            0,
            0,
        ]
        symbol_list = [
            '',
            '',
            '',
            '',
        ]
        operator_dict = {
            1: ' + ',
            2: ' - ',
            3: '*',
            4: '**',
        }

        for i in range(self.no_of_questions):
            for index in range(0, 5):
                number_list[index] = randint(1, 9)

            for index in range(0, 4):
                if index > 0 and symbol_list[index - 1] == '**':
                    symbol_list[index] = operator_dict[randint(1, 3)]
                else:
                    symbol_list[index] = operator_dict[randint(1, 4)]

            question_string = str(number_list[0])

            for index in range(0, 4):
                question_string = question_string + symbol_list[index] + str(
                    number_list[index + 1])

            result = eval(question_string)

            question_string = question_string.replace("**", "^")

            user_result = input("\nPlease evaluate %s: "
                                % question_string)

            while True:
                try:
                    answer = int(user_result)
                    if answer == result:
                        print("Correct Answer!")
                        score = score + 1
                        break
                    else:
                        print(
                            "Wrong answer. The correct answer "
                            "is {:d}.".format(result))
                        break
                except IOError:
                    print(
                        "You did not enter a valid number. "
                        "Please try again.")
                    user_result = input(
                        "\nPlease evaluate %s: " % question_string)

        return score
