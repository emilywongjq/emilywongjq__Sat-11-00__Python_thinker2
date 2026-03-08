# # code
# #1  check if the item is glass
# #2  if it is, place item in the glass bin
# #3  if its not, check if the item is plastic
# #4  if it is, place item in plastic bin
# #5  else, place in the paper bin    

# #take number of red plates and multiply by 1
# #take number of blue plates and multiply by 2
# #take number of green plates and multiply by 3

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print ("Average score for " + student_name + " is: " + str(average_score))

#______________________________________________________________

# ## Recap 4: If..elif..else & Flowchart
# Write a program that asks the user to input a score
# (as an integer) and then assigns a grade based on that score.
# Use the following grading scheme:

# If the score is 75 or higher, the grade is 'A'.
# If the score is between 60 and 74 (inclusive), the grade is 'B'.
# If the score is between 50 and 59 (inclusive), the grade is 'C'.
# Any score below 50 will be graded as 'Fail'.

# Use flowchart to draw out all decisions that are to be made
# before starting on your code.

score = int(input("What is your score? 😈😼"))

if score >= 75:
    print("Grade A")
elif score >= 60:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("YOU DIED")