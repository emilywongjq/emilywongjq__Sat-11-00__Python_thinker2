################ RECAP #1 #################
# import time
# counter = 10
# while counter > 0:
#     print(counter)
#     counter -= 1
#     time.sleep(1)
# else:
#     print("Happy new year!")

###############   TASK #1   ################

planets = [
    "Mercury", 
    "Venus", 
    "Earth", 
    "Mars", 
    "Jupiter", 
    "Saturn", 
    "Uranus", 
    "Neptune"
]

# # # print(planets)

# for i in range(len(planets)):
#     print(planets[i])

# # # for planet in planets:
# # #     print(planet)

# planets[3] = "!!!"

# planets.append("pluto")

# planets.insert(3,"lalaland")

# # planets.remove("Jupiter")

# planets.pop(5)

# for i in range(len(planets)):
#     print(planets[i])

#################### TASK #2 #######################

# for i in range(len(planets)):
#     if planets[i] == "Earth":
#         print(f"{planets[i]} ,is my home")
#     elif planets[i] == "!!!":
#         print(f"{planets[i]} , I have conquered")
#     elif planets[i] == "lalaland":
#         print(f"{planets[i]} , I created this")
#     else:
#         print(planets[i])

#################### TASK #3 #####################
# countries = []
# user_input = ""
# while user_input != "end":
#     user_input = input("What country would you like to visit?")
#     if user_input.lower() == "end":
#         break
#     else:
#         countries.append(user_input)

# print(countries)

#################### TASK #4 #####################

menu = []
user_input = ""
while user_input != "end":
    user_input = input("What would you like to add?")
    if user_input.lower() == "end":
        break
    else:
        menu.append(user_input)

customer_input = input("What would you like to eat today?")

if customer_input in menu:
    print("Yes, we sell that, please have a seat.")
else:
    print("Sorry, we do not sell that , please go next door.")
