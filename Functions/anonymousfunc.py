last_name = 'john'
first_name = 'Divine'

def function():
    middle_name = 'Wisdom'
    print(last_name)
    print(middle_name)

numbers = [12,3,13,2,5,6,7,13,15,21,81,91,52]
def even_numbers():
    for number in numbers:
        if number%2 == 0:
            print(number)




even_num = filter(lambda number: number%2==0,numbers)
print(tuple(even_num))



sqrValues = map(lambda y:y**0.5,numbers)
print(list(sqrValues))
squaredValues = map(lambda y:math.sqrt(y),numbers)
print(list(squaredValues))



