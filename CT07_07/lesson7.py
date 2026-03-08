# # -------- Recap 1 ---------
# students = []

# student1 = [
#     "Name1",
#     "Phoney1",
#     "cCaAAa1"
# ]
# student2 = [
#     "Name2",
#     "Phiney2",
#     "CcAaAaA2"
# ]
# student3 = [
#     "Name3",
#     "Foney3",
#     "CCAaAaAaA3"
# ]

# students.append(student1)
# students.append(student2)
# students.append(student3)

# print(students)

# for student in students:
#     name, phoneNum, cca = student
#     print("Name: " + name)
#     print("Phone Num: " + phoneNum)
#     print("CCA: " + cca)
#     print("------------------------------")

#--------Task1--------

# list1 = ["Apple","Banana","Cherry"]
# list2 = ["Durian","Elderberry","Figs"]
# list = list1 + list2
# print(list)

# ## Task 2: Ordered List Merging
# You are given 2 lists that contain the price of fruits. Now,
# merge 2 given lists and ensure the resulting list is sorted.

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]

# 1. Merge the lists using the + operator.
# 2. Use the sorted() function to sort the combined list.
# 3. Print the sorted list.
# list4 = []
# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]
# list3 = list1 + list2
# list4 = sorted(list3)
# print(list3)
# print(list4)


# sliced = list4[:3]
# print(sliced)

### Task 3: Splitting Lists at a Point
# You are required to divide a basket of fruits.
# Split the given list at the specified index:

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3

# 1. Use slicing to split the list at the provided index.
# 2. Print the resulting sublists.
# sliced = fruits[:3]
# print(sliced)

# ## Task 4: Splitting a List in Half
# You have been tasked to divide the basket of fruits into
# 2 equal halves. Given a list of even length, split it
# into 2 equal halves.

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# # 1. Find the midpoint of the list.
# # 2. Split the list into 2 halves using slicing.
# # 3. Print both halves.

# mid_point = len(fruits)//2
# list1 = fruits[:mid_point]
# list2 = fruits[mid_point:]
# print(list1)
# print(list2)

# ## Task 5: Identifying Common Elements in Lists
# You have been given 2 lists of fruits. However, there might be
# duplicates. Your job is to identify and print the common fruits
# between them.

list1 = ["Apple", "Banana", "Cherry", "Durian"]
list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

# 1. Create an empty list named 'common'
# 2. Using 'for' loops, append common elements into 'common'
# 3. Print the common elements

common = []
for item in list1:
    if item in list2:
        common.append(item)
print(common)