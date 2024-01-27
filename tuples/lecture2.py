# Tuple
item1 = ("Mango","Banana","Orange","Orange","cherry")
print(item1[0])
print(item1[2])
print(item1[2:])
print(item1[:])

# looping through a tuple
for i in item1:
    if "an" in i:
        print(i)

numbers = ("8051725775", "7082155821", "806390533")
for i in numbers:
    if "57" in i:
        print(i)

list_numbers = list(numbers)
list_numbers.append("817081999")
numbers = tuple(list_numbers)
print(numbers)

numbers2 = numbers
print(numbers2)

# tuples of students name and age
print("---Nested Tuples-----")
students = (("Winifred",23),("Mfon",26),("Tolu",25))
print(f"all students: {students}")
print(f"first student: {students[0]}")
print(f"second student: {students[1]}")
print(f"third student: {students[2]}")

# student names
print(f"first student: {students[0][0]}")
print(f"second student: {students[1][0]}")
print(f"third student: {students[2][0]}")
