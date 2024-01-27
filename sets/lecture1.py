# creating a set
sample = {'Mark', 'Jessa', 25, 75.25}

# converting a list to a set
number_list = [20, 30, 20, 30, 50, 30]
sample_set = set(number_list)
print(sample_set)

# accessing an item in a lis
book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}

#displaying  items
for books in book_set:
    print(books)

#displaying an item
for books in book_set:
    if "Angels" in books:
        print(books)

# removing an item randomly
book_set.pop()
print(book_set)

# removing a specific item
book_set.remove("Harry Potter")
print(book_set)
book_set.discard("Atlas Shrugged")
print(book_set)

# adding an item using add method
book_set.add("Think Big")
print(book_set)

# adding list of items using update method
book_set.update(["Power and principle of vision","Discovering purpose"])
print(book_set)
