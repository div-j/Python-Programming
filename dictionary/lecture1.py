# creating a dictionary using {}
student1 = {"name":"mfon","country":"Nigeria","phone":23480973563}
tuple1 = ("name","tolu")
tuple2 = ("age",25)
list1 = ["name",'winifred']
student2 = dict([tuple1,tuple2])
student3 = dict([list1])

print("First Student",student1)
print('****************************')
print(student2)
print("Hi,my name is: ",student1['name'])
print("my phone number is: ", student1['phone'])
print("I am fromm : ",student1['country'])

