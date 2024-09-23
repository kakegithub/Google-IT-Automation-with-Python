###############################################################################################################


animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))

# Total characters: 22, Average length: 5.5


##############################################################################################################


winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


# 1 - Ashley
# 2 - Dylan
# 3 - Reese


###################################################################################################################


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(
    full_emails(
        [("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]
    )
)

# ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']


######################################################################################################################3


def skip_elements(elements):
    # code goes here
    result = [element for index, element in enumerate(elements) if index % 2 == 0]
    return result


print(
    skip_elements(["a", "b", "c", "d", "e", "f", "g"])
)  # Should be ['a', 'c', 'e', 'g']
print(
    skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"])
)  # Should be ['Orange', 'Strawberry', 'Peach']


##########################################################################################################################
