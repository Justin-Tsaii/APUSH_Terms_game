
#Get the contents of the text file
questions = []
answers = []
questionAmount = 0

def read_file(text):
    file = open(text, "rt")
    fillTermNumbers()
    file1 = open("NumberList.txt", "rt")
    num_questions = 0
    index = 0
    num_list = file1.readlines()
    for e in num_list:
        num_list[index] = e.replace(" \n", "")
        index += 1
    #print(num_list)
    for line in file:
        text_split = line.split(" ")
        if text_split[0] not in num_list:
            #print(text_split[0])
            text = line.replace("â€™", "'")
            #print(text)
            questions.append(text)
            num_questions += 1
        else:
            answer = ""
            for word in text_split:
                if word != text_split[0]:
                    answer += word + " "
            #print(answer)
            answers.append(answer)
    setQuestionAmount(num_questions)
    file.close()

def fillTermNumbers():
    numFile = open("NumberList.txt", "w")
    for i in range(1, 1604):
        numFile.write(str(i) + "." + " \n")
    numFile.close()

def getQuestions():
    return questions

def getAnswers():
    return answers

def getQuestionAmount():
    #global questionAmount
    return questionAmount

def setQuestionAmount(amount):
    global questionAmount
    questionAmount = amount

#def setAnswers(a)
