import random
#Get the contents of the text file
file = open("Terms101-150.txt", "rt")
num_questions = 0
questions = []
answers = []
for line in file:
    if line[0] != "1":
        text = line.replace("â€™", "'")
        questions.append(text)
        num_questions += 1
    else:
        text = line.replace("â€™", "'")
        answers.append(text)
initial_questions = num_questions
file.close()

def start_game(number_questions):
    score = 0
    answer_char = 0
    correct_char = 0
    word_char_correct = 0
    while number_questions > 0:
        selector = random.randint(0, number_questions-1)
        question_text_list = questions[selector].split(" ")
        answer_text_list = answers[selector].split(" ")
        answer_text_list.pop(0)

        question_text = select_question(selector, answer_text_list, question_text_list)
        answer_text = select_answer(answer_text_list)

        print("\n" + question_text)
        response = input("Type the Answer: ")
        response_list = response.split(" ")

        correct_char = score_response(0, response, answer_text, answer_char, correct_char, word_char_correct, response_list, answer_text_list, len(answer_text))
        if(point_earned(correct_char, len(answer_text))):
            score += 1

        answer_char = 0
        correct_char = 0
        number_questions -= 1
        questions.remove(questions[selector])
        answers.remove(answers[selector])
    end_game(score, initial_questions)

def select_answer(answer_text_list):
    for word in answer_text_list:
        if word.startswith("(") or word.isnumeric():
            answer_text_list.remove(word)
        elif word.endswith("\n"):
            word_txt = word.replace("\n", "")
            answer_text_list.remove(word)
            answer_text_list.append(word_txt)
    answer_text = " ".join(answer_text_list)
    return answer_text

def select_question(selector, answer_text_list, question_text_list):
    index = 0
    for word in question_text_list:
        if word in answers[selector] and word[0].isupper() and len(word) > 3 and len(answer_text_list) < 4:
            question_text_list[index] = "___"
        index += 1
    question_text = " ".join(question_text_list)
    return question_text

def score_response(args, response, answer_text, answer_char, correct_char, num_correct, response_list, answer_text_list, total_char):
    match args:
        case 0:
            for c in response:
                if c == answer_text[answer_char]:
                    correct_char += 1
                    if correct_char == total_char:
                        return correct_char
                else:
                    num_correct = score_response(1, None, None, None, None, num_correct, response_list, answer_text_list, total_char)
                    return num_correct
                answer_char += 1
            return correct_char
        case 1:
            word_index = 0
            while word_index < len(response_list):
                word = response_list[word_index]
                if word in answer_text_list:
                    num_correct += len(word)
                    response_list.remove(word)
                else:
                    word_index += 1
            return num_correct

def point_earned(number_correct, total_char):
    accuracy = number_correct / total_char
    if accuracy > 0.7:
        return True
    else:
        return False


def end_game(points_earned, total):
    percentage = points_earned/total
    accuracy = round(percentage, 2) * 100
    print("You got " + str(points_earned) + " out of " + str(total) + ".")
    print("Accuracy: " + str(accuracy) + "%")


start_game(num_questions)




