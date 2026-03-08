# Lesson 6 - 2-dimensional list

## Recap 1: List of 100 unique numbers
# **Recap 1a**:
# You are preparing for an upcoming lucky draw session at your
# school. However, there must be no repeating winning numbers.

# Task: Create a program to create 100 random unique numbers in
# a list
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique

# import random
# numbers = []
# for i in range(0,100):
#     random_number = random.randint(1,1000)
#     if random_number in numbers:
#         random_number = random.randint(1,1000)
#     numbers.append(random_number)

# for i in range(len(numbers)):
#     print(numbers[i])

# # **Recap 1b**:
# # You have been asked to provide some statistics based on the
# # list of numbers generated.

# # 1. Using max(), find the highest number from the list
# highest_number = max(numbers)
# print(highest_number)
# # 2. Using min(), find the lowest number from the list
# lowest_number = min(numbers)
# print(lowest_number)
# # 3. Using sum() and len(), find the average from the list
# total_sum = sum(numbers)
# average = total_sum/len(numbers)
# print(average)
# # 4. By importing the 'random' library and using random.choice(),
# #    print out a random number from the list.
# random_number = numbers[random.randint]
# print(random_number)
# # 5. Using index(), print out the index of the printed random
# #    number.
# index = numbers.index(str(random_number))
# ---------------------------------------------------------------

# ## Task 1: A list within a list 

# You are about to graduate and would like to create a database
# to keep all your friend's contact details using a 2d list.

# Sample Code (Copy + Paste the below code):
# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# 1. append contact1, contact2, and contact3 into contacts
# 2. Write a nested loop to loop through each contact and print
#    the details for each contact

# names = ['John','Adam','Sylvia']
# numbers = ['98453126','93029102','87894032']
# gmail = ["john@gmail.com","adam@gmail.com","sylvia@gmail.com"]

# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)

# #To loop
# #for smth in smth: 1st loop loop thru each object of the big list
# #   for smth in smth: 2nd loop loop thru each item of each object

# for contact in contacts:
#     for i in contact:
#         print(i)
# ---------------------------------------------------------------

# ## Task 2: Student List
# You have been given a 2d list of students from a class
# consisting each student's name and their gender:

# Sample Code (Copy + Paste the below code):
# students = [
#     ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#     ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
#     ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
#     ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#     ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]
# ### the above is a nested list. Study and discuss it before we
# ### move on.

# 1. Write a for loop to print out the names of each student and
#    the gender beside.
   
#    e.g. Olivia F
#         Noah M

# students = [
#     ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#     ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
#     ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
#     ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#     ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]
# # for student in students:
# #     for i in student:
# #         name,gender = student  # ----> this is the unpacking method
# #         print("gender of " + name +":"+ gender)
# # ---------------------------------------------------------------

# # ## Task 3: Boys and Girls
# # Based on the class list given in the previous task, separate
# # the class into 2 lists of boys and girls.

# # 1. Create 2 more lists called boys and girls.
# boys = []
# girls = []
# # 2. Loop through the 'students' list from the previous task

# for student in students:
#     name,gender = student
#     if gender == "M":
#         boys.append(name)
#     elif gender == "F":
#         girls.append(name)
#     else:
#         print(" Not boy not girl")
        
# #    a. if the gender is a boy, add the name into the boys list
# #    b. if the gender is a girl, add the name into the girls list
# # 3. Write a for loop and name all the boys
# print("The boys are: ")
# for i in range(len(boys)):
#     print(boys[i])
# # 4. Write a for loop and name all the girls
# print(" ")

# print("The girls are:")
# for i in range(len(girls)):
#     print(girls[i])
# # 5. Print out how many boys and girls there are -->
# print("There are " + str(len(boys)) + " boys.")
# print("There are " + str(len(girls)) + " girls")

pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]

import random

random_pokemon = 
random_power = 

pokemonlist = []

pokemonlist.append(random_pokemon) 
pokemonlist.append(random_power)

pokedex = []
pokedex.append(pokemons)
pokedex.append(powers)
pokedex.append(pokemonlist)

print(pokedex)