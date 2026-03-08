################### Lesson 5 - List Variables II ######################

#____________________________ Recap 1: Favourite Food List____________________________________#
# **Recap 1a**:
# Create a list of 5 food that you like to eat 

# fav_foods = [
#     "Pizza",
#     "stuff",
#     "burger",
#     "food",
#     "Sushi"
# ]
# for i in range(len(fav_foods)):
#     print(fav_foods[i])

# # **Recap 1b**:
# # You no longer like to eat the 3rd item on your list,
# # delete it

# del (fav_foods[2])
#OR#
# fav_foods.pop(2)

# ---------------------------------------------------------------

# ## Task 1: List of 100 numbers 
# You are preparing for an upcoming lucky draw session at your
# school. You have been tasked to create a program that will pick
# 100 lucky winners.

# By importing the 'random' library and using 'random.randint()',
# create a program to create 100 random numbers in a list
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000

# import random
# winners = []
# for i in range(0,100):
#     random_number = random.randint(1,1000)
#     winners.append(random_number)

# for i in range(len(winners)):
#     print(winners[i])

# ---------------------------------------------------------------

# ## Task 2: List of 100 unique numbers
# The program you have created from the previous task will
# sometimes generate duplicate numbers. Modify your program so
# that the 100 numbers generated are all unique.

# Modify your program from the previous task to create 100 random
# unique numbers in a list.
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique
# 4. Print the list of 100 unique numbers created
# Hint: Use a while loop to check if the number already exists in
# the loop

# import random
# winners = []
# for i in range(0,100):
#     random_number = random.randint(1,1000)
#     if random_number in winners:
#         random_number = random.randint(1,1000)
#     winners.append(random_number)

# for i in range(len(winners)):
#     print(winners[i])

# ---------------------------------------------------------------

# ## Task 3: Score Taker
# Imagine the list that you have created in Task 2 represent the
# score of a 100 students.

# Find the maximum, minimum and average from the list.

# 1. Using the 'max()' function, find the maximum score.
# 2. Using the 'min()' function, find the minimum score.
# 3. Using the 'sum()' and 'len()' function, calculate the
#    average score.

# largest_number = max(winners)
# smallest_number = min(winners)

# total_sum = sum(winners)
# total_count = len(winners)
# average = total_sum / total_count

# ---------------------------------------------------------------

# ## Task 4: Who is the tallest?
# Task: You are given 2 lists, 
# **namelist** contains a list of students in your class
# **heightlist** contains a list of the corresponding student's
#                height

# 1. Determine who is the tallest in class, and what is his/ her
#    name
# 2. Determine who is the shortest in class, and what is his/ her
#    name

# Sample Data (Copy + paste the below code):
# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#             "Sophia", "Lucas", "Mia", "Aiden"
#             ]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# Hint:
# use .index("value of something in the list") to find the index
# of an item

# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#             "Sophia", "Lucas", "Mia", "Aiden"
#             ]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# max_height = max(heightlist)
# index = heightlist.index(max_height)
# tall_name = namelist[index]

# print("The tallest person in class is " + str(tall_name) + " at " + str(max_height))

# min_height = min(heightlist)
# index1 = heightlist.index(min_height)
# short_name = namelist[index1]

# print("The shortest person in class is " + str(short_name) + " at " + str(min_height))

# ---------------------------------------------------------------

# ## Task 5: Pokemon, I choose you!
# Task: You are given 2 lists,
# **pokemons** contains a list of pokemons
# **powers** contains a list of the corresponding pokemon's
#            powers

# 1. Choose 2 random pokemons from the list
# 2. Compare the powers of the 2 pokemons
# 3. Calculate who is the winner of the fight between these 2
#    pokemons
#    (pokemon with the higher power will always win)

# Sample data (Copy + paste the below code):
# pokemons = [
#     "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
#     "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
#     "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
#     "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
#     "Electabuzz"
# ]

# powers = [
#     55, 84, 49, 48, 45,
#     45, 52, 55, 110, 110,
#     85, 65, 134, 130, 110,
#     50, 125, 65, 110, 83
# ]


# Hint: import the random library and use random.choice(listname)
import random
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
num1 = random.randint(0,21)
num2 = random.randint(0,21)
if num1 == num2:
    num2 = random.randint(0,21)

powers1 = powers[num1]
powers2 = powers[num2]

pokemons1 = str(pokemons[num1])
pokemons2 = str(pokemons[num2])

if powers1 > powers2 :
    print(pokemons1 + " has won against " + pokemons2)
elif powers2 > powers1 :
    print(pokemons2 + " has won against " + pokemons1)
else:
    print("Its a tie between " + pokemons1 + " and " + pokemons2)

###OR####

# pokemons1 = random.choice(pokemons)
# pokemons2 = random.choice(pokemons)

# print(pokemons1)
# while pokemons2 == pokemons1:
#     pokemons2 = random.choice(pokemons)
# print(pokemons2)