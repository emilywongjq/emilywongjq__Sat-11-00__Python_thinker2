# ____________________________riddle_me___________________________
# while True:
#     user_input = input("What starts with T, ends with T, and has T in it?")
#     if user_input == "a teapot" or "teapot":
#         print("correct")
#         break
#     else:
#         print("try again")

#_____________________________Task#1_____________________________

# study_time = input("How many minutes do you plan to study?")

# seconds = int(study_time)*60
# while True:
#     print(seconds/60)
#     import time
#     time.sleep(seconds)
#     print("Good job!")
#     break

#_____________________________Task#2________________________

# savings = 0
# while savings < 100:
#     user_input = float(input("How much did you save today?"))
#     savings += user_input
# print("congratulations! You have saved ${savings}!")

#___________________________Task#3__________________________

import random
lives = 3
questions = 0

for i in range(questions):
    num1 = str(random.randint(2,20))
    num2 = str(random.randint(2,20))
    ans= num1*num2
    while lives > 0:
        qn = input("What is " + str(num1)+ "x" + str(num2)+ "?")

        if qn == ans:
            print("correct")
            break
        else:
            lives -= 1
            print("Wrong try again!")

        if lives == 0:
            print("Go see Ms Tan for remedial")
            break
    if lives == 0:
        break
if lives > 0:
    print("congratulations")
    