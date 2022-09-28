# Countdown: Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    x = list(range(num, -1, -1))
    return x

countdown(5)


# Print and Return: Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(lst1):
    print(lst1[0])
    return lst1[1]

print_and_return([1,2])


# First Plus Length: Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(lst2):
    return lst2[0] + len(lst2)

first_plus_length([1,2,3,4,5])


# Values Greater Than Second: Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(lst3):
    if len(lst3) < 2:
        return False
    x = lst3[1]
    y = []
    for i in range(len(lst3)):
        if lst3[i] > x:
            y.append(lst3[i])
    print(len(y))
    return y

values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3])

# This Length, That Value: Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(x,y):
    lst4 = [y]
    result = lst4 * x
    return result

length_and_value(4,7)
length_and_value(6,2)