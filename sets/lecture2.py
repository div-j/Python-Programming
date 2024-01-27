#set operation
color1 = {'violet', 'indigo', 'blue', 'green', 'yellow'}
color2 = {'indigo','orange','red'}

#Union: using the | operator
unionColor = color1 | color2
print('Union color using the | operator: ',unionColor)
print('***************************')


#using the union method
unionColor2 = color1.union(color2)
print('Union color using the union method: ',unionColor2)
print('***************************')


#Intersection: using the & operator
interColor = color1 & color2
print('Union color using the | operator: ',interColor)
print('***************************')

#using the Intersection method
interColor2 = color1.intersection(color2)
print('Intersection color using the intersection() method: ',interColor2)
print('***************************')

#difference: using the - operator
diffColor = color1 - color2
print('Difference color using the - operator: ',diffColor)
print('***************************')
#using the Intersection method
diffColor2 = color1.difference(color2)
print('Difference color using the difference() method: ',diffColor2)

#symmetric difference: using the ^ operator
symColor = color1 ^ color2
print('symmetric difference color using the - operator: ',symColor)
print('***************************')
#using the symmetric_difference method
symColor2 = color1.symmetric_difference(color2)
print('symmetric difference color using the symmetric_difference() method: ',symColor2)
print('***************************')

#copying of set
color3 = color1
color4 = color1.copy()
print("shallow copy: Using the = operator", color3)
print('***************************')
print("Deep copy: Using the copy method", color4)
print('***************************')

#sorting a set
print("Set is sorted", sorted(color4))
print('***************************')


