#if Statement
# users = ['mfon', 'winifred', 'Tolu', 'Ify' ]

# name =input('please enter user name: ')


# if name in users:
#     print('Welcome! as a member of the data scientists, you are now logged in')

# else:
#     print("Sorry you are not a member")


#A program to deliver a product

des = input('Please enter destination: ')
print('Welcome to our delivery service')
print("Your delivery destination is ", des)

if des:
    route1 ='sabo'
    call = input('Please is destination free or block: ')
    if call == 'free':
        print('Now heading towards sabo ')
        route2 ='yaba'
        call = input('Please is destination free or block: ')
        if call == 'free':
            print('Now heading towards yaba ') 
    else:
        print('taking another route')
    