def greet():
    '''
    this is a function that greets
    '''
    name = input("Please enter your name: ")
    gender = input('male or female?')
    if gender=='male':
        return f"Hello Mr. {name}, how are you doing today"
    else:
        return f"Hello Miss/Mrs {name}, how are you doing today"

    
# print(greet())

first_name = 'John'
def DollaToNaira(amount):
    last_name = 'Divine'
    """
    this is a function that converts dollar to naira
    """
    NairaValue = 1000*amount
    return f"{amount} in Dollar is {NairaValue} in Naira"

print(DollaToNaira.__doc__)
print()
print(first_name)
print()
