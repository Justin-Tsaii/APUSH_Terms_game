import random
import TermsDirectory.TermsClass as termsCls
#Get the contents of the text file
textFile = "TermsDirectory/Terms151-200.txt"
termsCls.read_file(textFile)

questions = termsCls.getQuestions()
answers = termsCls.getAnswers()
num_questions = termsCls.getQuestionAmount()
initial_questions = num_questions

def start_game(number_questions):
    score = 0
    while number_questions > 0:
        selector = random.randint(0, number_questions-1)
        question_text_list = questions[selector].split(" ")
        answer_text_list = answers[selector].split(" ")

        question_text = select_question(selector, answer_text_list, question_text_list)

        print("\n" + question_text)
        response = input("Type the Answer: ")
        answer_tup = compare_answer(response, answers[selector])
        if(answer_tup[1] == True):
            if(point_earned(answer_tup[0], getTotalChar())):
                score += 1

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

def compare_answer(response, answer):
    answer_letters = []
    num_letters = []
    total = 0
    answer_total = 0
    answer_index = 0
    for a in answer:
        if a.isalnum() and a not in answer_letters:
            answer_letters.append(a)
    for i in answer_letters:
        count = answer.count(i)
        resp_count = response.count(i)
        num_letters.append(count)
        if resp_count >= count:
            resp_count = count
        total += resp_count
        answer_total += count
    setTotalChar(answer_total)
    for c in response:
        if c == answer[answer_index]:
            return (total, True)
        answer_index += 1
    return (total, False)

def setTotalChar(amount):
    global question_char
    question_char = amount

def getTotalChar():
    return question_char

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




