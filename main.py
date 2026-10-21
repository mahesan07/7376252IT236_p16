import question

def questionDetail(questionTopic):
    query = question.questions(questionTopic)
    answer = question.answer(questionTopic)
    ind = 0
    score = 0

    print("------------------------------- Quiz Start -------------------------------")

    for i in range(len(query)) :
        print(query[i][0])
        for j in range(1, 5):
            print(query[i][j])
        while True:
            try :
                result = int(input("Enter Your Choice : "))
                if result in [1, 2, 3, 4]:
                    break
                print("Enter valid Choice .")

            except ValueError:
                print("Invalid Input !")
        if result == answer[ind]:
            score+=1
        ind+=1
    return score

def showLeaderBoard(playerDetails):
    print("============================== LeaderBoard ==============================")
    sortedPlayers = playerDetails.copy()
    for i in range(len(sortedPlayers)):
        for j in range(i + 1, len(sortedPlayers)):
            if sortedPlayers[j][1] > sortedPlayers[i][1]:
                temp = sortedPlayers[i]
                sortedPlayers[i] = sortedPlayers[j]
                sortedPlayers[j] = temp

    count = 0
    for i in range(len(sortedPlayers)):
        if count < 10:
            print(f"Rank : {i+1} | Name : {sortedPlayers[i][0]} | Score : {sortedPlayers[i][1]}")
        else:
            break
        count+=1

    print("=========================================================================")



print("------------------------------------------------------Welcome to Quiz Game Terminal------------------------------------------------------\n")
while True:

    print("Enter How Many Peoples Are Going To Play :", end=" ")

    try:
        n = int(input())
        if n > 0 :
            break
        print("Enter Valid Number Of Players.")
    except ValueError:

        print("Invalid Input. Try Again !")

print("------------------Available Topics Of Question------------------\n")
question.availableTopic()

while True:

    try:
        questionTopic = int(input("Select a Topic : "))

        if questionTopic in question.questionData:
            break
    except ValueError:
        print("Invalue Input. Try Again !")

playerDetail = []
for i in range(n):
    print(f"--------------------------- Player {i+1} ---------------------------")

    name = input(f"Enter player Name : ")

    score = questionDetail(questionTopic)
    playerDetail.append([name, score])

    print(f"{name}, your score is {score}/{len(question.questions(questionTopic))}.")

showLeaderBoard(playerDetail)




