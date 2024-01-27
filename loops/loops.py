fruitList = ["apple","banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "orange",
    "papaya",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "watermelon",
    "apricot",
    "blueberry",
    "coconut",
    "dragonfruit",
    "guava",
    "lime",
    "nectarine",
    "peach",
    "pineapple",
    "quince",
    "blackberry",
    "cantaloupe",
    "grapefruit",
    "jackfruit",
    "lychee",
    "olive",
    "pear",
    "plum",
    "raisin",
    "tamarind",
    "boysenberry",
    "cranberry",
    "kiwifruit",
    "pomegranate",
    "tamarillo",
    "apricot",
    "clementine",
    "mulberry",
    "passion fruit",
    "starfruit"
]

fruits_starting_with_a_and_b = []
rest_of_fruits = []
fruits_starting_with_a = []
fruits_starting_with_b = []
for x in fruitList:
    if 'a' == x[0] or 'b' ==x[0]:
        fruits_starting_with_a_and_b.append(x)
        if 'a'==x[0]:
            fruits_starting_with_a.append(x)
        else:
            fruits_starting_with_b.append(x)
    else:
        rest_of_fruits.append(x)

# print(fruits_starting_with_a_and_b)
# print(rest_of_fruits)
print(fruits_starting_with_b)

        
