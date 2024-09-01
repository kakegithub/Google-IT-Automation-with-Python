####################################################
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


####################################################
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


factorial(4)


###################################################
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15


####################################################
def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number // base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False

############################################################

""" 
def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
         else:
      count += 1
    return count


print(count_users("sales"))  # Should be 3
print(count_users("engineering"))  # Should be 8
print(count_users("everyone"))  # Should be 18
 """
#################################################################3
