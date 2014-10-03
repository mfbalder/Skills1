# Things you should be able to do.

# Start 11:15

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    ###### with list comprehension ######
    return [x for x in number_list if x % 2 != 0]

    #### with functional programming ######
    # return filter(lambda x: x % 2 != 0, number_list)

    #### with iteration ####
    # new_list = []
    # for num in number_list:
    #     if x % 2 != 0:
    #         new_list.append(num)
    # return new_list


# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    ###### with list comprehension ######
    return [x for x in number_list if x % 2 == 0]

    #### with functional programming ######
    # return filter(lambda x: x % 2 == 0, number_list)

    #### with iteration ####
    # new_list = []
    # for num in number_list:
    #     if x % 2 == 0:
    #         new_list.append(num)
    # return new_list

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    ###### with list comprehension ######
    return [x for x in word_list if len(x) >= 4]
    
    #### with functional programming ######
    # return filter(lambda x: len(x) >= 4, word_list)

    #### with iteration ####
    # new_list = []
    # for word in word_list:
    #     if len(word) >= 4:
    #         new_list.append(word)
    # return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    #### with functional programming ######
    return reduce(lambda x, y: y if y < x else x, number_list)
    
    #### with iteration ####
    # smallest_index = 0
    # for number_index in range(len(number_list)):
    #     if number_list[number_index] > number_list[smallest_index]:
    #         smallest_index = number_index
    # return smallest_index

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    #### with functional programming ######
    return reduce(lambda x, y: y if y > x else x, number_list)

    #### with iteration ####
    # largest_index = 0
    # for number_index in range(len(number_list)):
    #     if number_list[number_index] > number_list[largest_index]:
    #         largest_index = number_index
    # return largest_index


# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    ###### with list comprehension ######
    return [x / 2.0 for x in number_list]

    #### with functional programming ######
    # return map(lambda x: x / 2.0, number_list)

    #### with iteration ####
    # new_list = []
    # for num in number_list:
    #     new_list.append(num / 2.0)
    # return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return[len(x) for x in word_list if len(x) >= 4]

    #### with functional programming ######
    # return map(lambda x: len(x), word_list)
    
    #### with iteration ####
    # new_list = []
    # for word in word_list:
    #     new_list.append(len(word))
    # return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    #### with functional programming ######
    return reduce(lambda x, y: x + y, number_list)

    #### with iteration ####
    # sum = 0
    # for number in number_list:
    #     sum = sum + number
    # return sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    #### with functional programming ######
    return reduce(lambda x, y: x * y, number_list)

    #### with iteration ####
    # total = 1
    # for number in number_list:
    #     total = total * number
    # return total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    #### with functional programming ######
    return reduce(lambda x, y: x + y, word_list)

    #### with iteration ####
    # single_string = ""
    # for word in word_list:
    #     single_string = single_string + word
    # return single_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    #### with functional programming ######
    return reduce(lambda x, y: x + y, number_list) / len(number_list)

    #### with iteration ####
    # total = 0
    # count = 0
    # for number in number_list:
    #     total = total + number
    #     count = count + 1
    # return total / float(count)

def custom_map(function, iterable):
    """Applies a function to every item of the iterable list, and returns a list of the results"""
    new_list = []
    for item in iterable:
        new_list.append(function(item))
    return new_list

def custom_filter(function, iterable):
    """Constructs a list of the elements in iterable for which the function returns true"""
    new_list = []
    for item in iterable:
        if function(item) == True:
            new_list.append(item)
    return new_list

def custom_reduce(function, iterable, initializer=None):
    """Applies function of two arguments cumulatively to the items of iterable, from left to right, to 
    reduce the iterable to a single value"""
    if initializer == None:
        counter = iterable[0]
        for item in iterable[1:]:
            counter = function(counter, item)
    else:
        counter = initializer
        for item in iterable:
            counter = function(counter, item)
    return counter

    



def main():
    # print all_odd(number_list)
    # print all_even(number_list)
    # print long_words(word_list)
    # print smallest(number_list)
    # print largest(number_list)
    # print halvesies(number_list)
    # print word_lengths(word_list)
    # print sum_numbers(number_list)
    # print mult_numbers(number_list)
    # print join_strings(word_list)
    # print average(number_list)

    print custom_map(lambda x: x * 2, number_list)
    print custom_filter(lambda x: x % 2 == 0, number_list)
    print custom_reduce(lambda x, y: x + y, number_list)


if __name__ == '__main__':
    main()