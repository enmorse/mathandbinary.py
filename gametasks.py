def print_instructions(instruction):
    print(instruction)


def get_user_score(user_name):
    try:
        file_input = open('user_scores.txt', 'r')
        for line in file_input:
            content = line.split(', ')
            if content[0] == user_name:
                file_input.close()
                return content[1]
        file_input.close()
        return '-1'
    except IOError as e:
        print(e)
        print("That file was not found. A new file will "
              "be created.")
        file_input = open('user_scores.txt', 'w')
        file_input.close()
        return '-1'


def update_user_score(new_user, user_name, score):
    from os import remove, rename

    if new_user:
        file_input = open('user_scores.txt', 'a')
        file_input.write(user_name + ', ' + score + '\n')
        file_input.close()
    else:
        temp_file_input = open('user_scores.tmp', 'w')
        file_input_read = open('user_scores.txt', 'r')
        for line in file_input_read:
            content = line.split(', ')
            if content[0] == user_name:
                temp_file_input.write(user_name + ', ' +
                                      score + '\n')
            else:
                temp_file_input.write(line)

        file_input_read.close()
        temp_file_input.close()

        remove('user_scores.txt')
        rename('user_scores.tmp', 'user_scores.txt')
