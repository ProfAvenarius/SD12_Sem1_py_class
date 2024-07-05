#Description: Program to correct mult choice quiz and return grades
#Author: DC Elliott
#Date: July 5/2024

#Program Libraies
import datetime

#Program Constants
TIME_TOTAL = datetime.datetime.now()
CURR_DATE =TIME_TOTAL.strftime("%d-%b-%y")

Corr_Ans =[]
Grade_Quiz =[]
#Program functions

def AnswerKey():
    #Assembles inputed correct answers into a list
    Ans_List = []
    print ("Enter the answer key")
    for x in range(1,num_quest+1):
        while True:
            print() 
            ans = input(f"The Answer to Question {x} is: ").capitalize()
            if ans != "A" and ans != "B" and ans != "C" and ans !=  "D":
                print ("Data Entry Error:Input must be A,B,C or D.")
            else:
                Ans_List.append(ans)
                break
    return Ans_List

def NameQuiz():
    #Assembles inputed names into a list
    Name_List =[]
    print()
    print(f"Enter the names of all {num_quiz} of the students.")
    for n in range (0,num_quiz):
        print()
        while True:
            name = input(f"Enter the name of student #{n+1}: ").title()
            if name == "":
                print ("Data Value Error: A name must be entered")
            else:
                break
        Name_List.append(name)
    return Name_List

def Correct():
    #Checks answers against key and returns number correct
    num_corr = 0
    for x in range(0,num_quest):
        print()
        while True:
            ans = input(f"The Answer to Question {x+1} is: ").capitalize()
            if ans != "A" and ans != "B" and ans != "C" and ans !=  "D":
                print ("Data Entry Error:Input must be A,B,C or D.")
            else: 
                if ans == Ans_Key[x]:
                    num_corr += 1
                    break
                else:
                    break
    return num_corr
            
    




#MAIN - Inputs/calculations

print()
print()
print()
print()
print ("--------------------------------------------------------------------------------")
print ("      MIDDLE SCHOOL MULTIPLE CHOICE QUIZ ASSISTANT - COMPLETE ALL FIELDS")       
print()
while True:
    print()
    while True:
        test_name = input("Enter the title of the quiz:  ")
        if test_name == "":
                print ("Data Value Error: A name must be entered")
        else:
            break       
    print()
    while True:
        while True:
            num_quest = input("Enter the number of questions on the quiz:  ")
            if num_quest.isnumeric() == False:
                print ("Data Entry Error: THe value entered must be a number.")
            else:
                num_quest = int(num_quest)
                break
        print()
        Ans_Key = AnswerKey()
        print()
        print (f"The Answer key for {test_name} is: {Ans_Key}")
        print()
        cont = input("If this answer key is incorrect press 'N' otherwise hit any other key to continue.").capitalize()
        if cont != "N":
            break

    print()
    print()
    while True:
        num_quiz = input("Enter the number of quizes to grade:  ")
        if num_quiz.isnumeric() == False:
                print ("Data Entry Error: THe value entered must be a number.")
        else:
            num_quiz = int(num_quiz)
            break

    Name_Quiz = NameQuiz()

    for n in range(0,num_quiz):
        print()
        print (f"Enter the answers for {Name_Quiz[n]}:")
        corr_ans = Correct()
        Corr_Ans.append(corr_ans)

    for m in range(0,num_quiz):
        print()
        grade_dec = Corr_Ans[m]/num_quest
        grade_per = "{:.0%}".format(grade_dec)
        
        Grade_Quiz.append(grade_per)

            
    print()
    print()

#Output

    print (f"  QUIZ: {test_name:12}      {CURR_DATE}")
    print()
    print ("Student        #Correct        %Grade")
    print ("-------------------------------------")
    for y in range(0,num_quiz):
        print (f"{Name_Quiz[y]:16}   {Corr_Ans[y]}            {Grade_Quiz[y]}")


    print()
    print()
    cont2 = input("If you would like to continue press 'Y' otherwise hit any other key to exit.").capitalize()
    if cont2 != "Y":
        break
print()
print("Have a nice day.")
print()
print()
