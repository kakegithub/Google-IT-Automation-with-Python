# Example 1:


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")


username = "Clarice"
hint_username(username)
print("")

# Example 2:


def is_even(number):
    if number % 2 == 0:
        return True
    return False


number = 9
print(is_even(number))
print("")
# Example 3


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")


username = "blackman"
hint_username(username)
print("")


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")


username = "Jordan"
hint_username(username)
print("")
