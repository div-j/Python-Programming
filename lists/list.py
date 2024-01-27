fruits =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#printing the first item in the list
print(fruits[0])
#printing the second item in the list
print(fruits[1])
#printing the last item in the list
print(fruits[-1])

#printing the first three of the items in the list
print(fruits[0:3])

#printing the last three of items in the list
print(fruits[-3:])

#printing the reverse of items in the list
print(fruits[::-1])

#checking if an item is in a list
print("apple" in fruits)
print("pawpaw" in fruits)

#changing/replacing/updating items in a list
fruits[0]="pawpaw"
fruits[-3]="apple"
fruits[0:2]=["grape","coconut"]
print(fruits)

#adding items to a list
fruits.append("Date")
fruits.append("pineapple")
print(fruits)
#adding items base of position
fruits.insert(2,"Strawberry")
print(fruits)
#"---Removing items in a list----
print("---Removing items in a list----")
fruits.remove("cherry")
fruits.pop(2)
del fruits[3]
print(fruits)
print()
print()
print()

#"---concating/merging lists----
print("---concating/merging lists----")
print()
print()

NewFruits = ["cherry","banana","watermelon" ]
mergedFruits = NewFruits+fruits
print(fruits)
print(f"Merging list using + operator: {mergedFruits}")
print()
print()

fruits.extend(NewFruits)
print(f"Merging list using extend method: {fruits}")
print()

#Coping a list

# 1. Shallow copying
print('Coping a list')
print()
#creating a new list
list1 = [2,4,2,5,6]
list2 = list1
print(f"list1: {list1}") 
print(f"list2: {list2}")
del list1[0]
print(f"removed values in list2: {list2}")
list2.pop(0)
print(f"list1 is affected: {list1}") 
# 1. Deep copying
print()
print("Deep copying")
list3 = list1.copy()
print(f"list3: {list3}")
list3.append(3)
list3.append(7)
print(f"adding new values to list3: {list3}")
print(f"list1 is not affected: {list1}")
list3.sort()
print(list3)
list3.reverse()
print(list3)
fruits.sort()
print(fruits)
max_val = max(list3)
min_val = min(list3)
print(max_val)
print(f'maximum value in list3 is: {max_val}')
print(f'minimum value in list3 is: {min_val}')

#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango","orange","water melon","date"]
# print(fruits[0])
# print(fruits[1])
# print("winifred")
# print("winifred")

for x in fruits:
    print(x)
print()

newFruits = []
for x in fruits:
    if 'a' in  x:
        newFruits.append(x)

print(newFruits)

newFruits2=[x.upper() for x in fruits]

print(newFruits2)

nums = [2,4,5,[23,12,[43,5],5],6,4,5]
nums.insert(1,[13,14,15])
# print("initial list: ",nums)

# print("index 4 list: ",nums[4])
# print("index 2 of index 4 list: ", nums[4][2])
print("index 0 of index2 of index 4 list: ",nums[4][2][0])



