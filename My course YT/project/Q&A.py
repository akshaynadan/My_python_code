questions = {"what is your name?":"A", "Are you a human?":"B","How old are you?":"A","Where do yu live?":"A"}
answer = [["A.Mohan","B.Ravi","C.Kishore","D.Manoj"],["A.Yes","B.Maybe","C.No","D.IDK"],["A.15","B.10","C.27","D.50"],["A.Mansion","B.Roadside","C.Kostel","D.Mahal"]]

# Starting Game function
def Start_game():
    qn = 1
    ans =  None
    collect_answer = []
    score = 0
    for key in questions:
        print("*******************")
        print(key)
        for options in answer[qn-1]:
            print(options)
        qn +=1
        ans = input("Enter your Answer 'A','B','C' or 'D':").upper()
        collect_answer.append(ans)
        score += check_ans(ans,questions[key])
    calculate_score(score)
    

    print("*******************")

#checking anwser Function 
def check_ans(answer,check):
    if answer == check:
        print("Correct Answer")
        return 1
    else:
        print("incorret")
    
        return 0
#calcute the correct answer in percentage 
def calculate_score(score):
     print(f"you Scored:{(score/len(questions))*100}") 

Start_game()
