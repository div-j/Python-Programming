#Review

#Variable data types

#1. integer
num1 = 20  

#2. float
num2 = 20.561 

#3.Strings
name1 = 'Ifeyinwa'
nam2 = "Tolu"
name3 = '''Mfon'''

#4. List
students = ['Ifeyinwa', 'Tolu','Mfon','Winifred','Mfon']
numbers = [1,3,12,4,5]

#accessing items in a list
third_student = students[2]
last_student = students[-1]
print("Third student: ", third_student)
print("last student: ", last_student)

#adding item to a list
students.append("Joy")
print("My python students are: ",students)

#removing an item from a list
students.pop()
print("My python students are: ",students)

#5. Tuple
private_students = ('Ifeyinwa', 'Tolu','Mfon','Winifred','Ifeyinwa')

#accessing items in a Tuple
first_student = private_students[0]
print("My first student: ", first_student)

#6. Set
unique_Items = {'Ifeyinwa', 'Tolu','Tolu','Mfon','Winifred','Ifeyinwa'}

#adding and removing an item from a set
unique_Items.add("James")
unique_Items.update(["John",'Jane','Janet'])
print("My private students are: ", unique_Items)


#display items or an item in a set
for item in unique_Items:
    if 'Joh' in item:
        print(item)

#when to use a set
#question 1: How many students are there in the attendance list
attendance = ['Mfon', 'Tolu','Tolu','Mfon','Tolu','Winifred','Mfon','Winifred','Ifeyinwa','Winifred','Mfon','Tolu']
#answer
myStudents = set(attendance)
print(f"There are {len(myStudents)} students in the attendance list")

#7. Dictionary

#creating a dictionary using the curly braces
student2 = {'name':'winifred','age':27, 'city':'asaba'}

#creating a dictionary using the dict constructor and zip function
keys = ['name','age','city']
values = ['mfon', 26, 'calabar']
student1 = dict(zip(keys,values))

#displaying a dictionary
print(f"Student1 {student1}")
print(f"Student2 {student2}")
print(f"Student1 age is:  {student1['age']}")
print(f"Student2 age is:  {student1.get('age')}")

#Removing an item in a dictionary
student1.popitem()
print(f"Student1:  {student1}")
student1.pop('name')
print(f"Student1:  {student1}")






