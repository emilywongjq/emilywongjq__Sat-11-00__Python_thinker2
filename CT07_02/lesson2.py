#🤦‍♀️🤦‍♀️       🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️  🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️
#🤦‍♀️🤦‍♀️       🤦‍♂️🤦‍♂️         🤷‍♀️🤷‍♀️     🤷‍♀️
#🤦‍♀️🤦‍♀️       🤦‍♂️🤦‍♂️           🤷‍♀️🤷‍♀️
#🤦‍♀️🤦‍♀️       🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️       🤷‍♀️🤷‍♀️
#🤦‍♀️🤦‍♀️       🤦‍♂️🤦‍♂️                 🤷‍♀️🤷‍♀️
#🤦‍♀️🤦‍♀️🤦‍♀️🤦‍♀️  🤦‍♂️🤦‍♂️          🤷‍♀️      🤷‍♀️
#🤦‍♀️🤦‍♀️🤦‍♀️🤦‍♀️  🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️   🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️
# for i in range (0 , 21):
#     print(i)

# for i in range (1 , 31):
#     print(i)

# for i in range (2,25,2):
#     print(i)
#_______________________________________________________
# count = 0

# while count <= 20:
#     print(count)
#     count += 1


# count = 1

# while count <= 30:
#     print(count)
#     count += 1

# count = 2

# while count <= 24:
#     print(count)
#     count += 2

#__________________________________________________

# counter = 1
# while True:
#     if counter == 5:
#         break

# counter = 1
# while counter < 11:
#     if counter > 5:
#         break
#     else:
#         print(counter)
#         counter += 1
# else:
#     print("count has reached 10")\

#______________________________________________________________

# topping = ""
# userInput = ""
# while True:
#     userInput = input("what topping do you want to add: ")
#     if userInput == "finish":
#         break
#     else:
#         topping += userInput + " "
# print(topping)

#_________________________________________________________
max_attempt = 3
score = 0
user_input = ""
question_answer = ["What is 1 + 1?","2",
            "What is 1 + 2?","3",
            "What is 1 + 3?","4"]

for i in range( 0 , len(question_answer),2):
    question = question_answer[i]
    ans = question_answer[i + 1]
    attempt = 0

    while attempt < max_attempt:
        user_input = input(question)
        if user_input.lower() == ans.lower():
            print("correct")
            score += 1
            break
        elif user_input.lower() == "skip":
            print("SKIPPED")
        else:
            print("NOT CORRECT YOU SUCK")

        if attempt == max_attempt:
            print("TOO MANY ATTEMPTS, YOU DIED!😡")

print("Your final score is "+ str(score))