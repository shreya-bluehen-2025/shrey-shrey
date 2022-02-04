"""
# Ada's Stats Module
A collection of functions for doing some basic statistics on your data.

# When You Are Done
When you pass all tests, remember to clean and document your code.
Be sure to unit test and document your functions.
"""

from cisc108 import assert_equal

def count(numbers: [int]) -> int:
    
    '''
    This function takes in a list of integers and returns the length
    of that list.
    
    Args:
    numbers [int]: A list of integers is taken by this function. 
    
    Returns:
    (int): A single integer is returned by this function.
    '''
    
    length = 0
    for number in numbers:
        length = length + 1
    return (length)    

assert_equal(count([3, 5, 9, 1, 6, 8]), 6)
assert_equal(count([3, 3, 7, 8, 7]), 5)
assert_equal(count([-9, 4, -7, 0, 1]), 5)
assert_equal(count([2, 4, 6, 8, 10, 12, 14, 16]), 8)
assert_equal(count([-2, 0, 2]), 3)


def summate(numbers: [int]) -> int:
    
    '''
    This function adds up all the integers in the list together,
    to return their total value (sum).
    
    Args:
    numbers [int]: A list of integers is taken by this function.
    
    Returns:
    (int): A single integer is returned by this function. 
    '''
    
    total = 0
    for number in numbers:
        total = total + number
    return (total)

assert_equal(summate([6, 1, 3, 4]), 14)
assert_equal(summate([-2, 6, 1, -9, 3]), -1)
assert_equal(summate([-1, -2, -3, -4]), -10)
assert_equal(summate([30, 10, 20, 50]), 110)
assert_equal(summate([12, 40, 1, 1, 1]), 55)


def mean(numbers: [int]) -> float:
    
    '''
    This function uses the count and summate functions to calculate
    the mean of the integers in the list.
    
    Args:
    numbers [int]: A list of integers is taken by this function.
    
    Returns:
    (float): A decimal value is returned by this function. 
    '''
    if numbers:
        average = summate(numbers) / count(numbers)
        return (average)
    else:
        return (None)

assert_equal(mean([3, 4, 8, 1]), 4.0)
assert_equal(mean([10, 10, 1]), 7.0)
assert_equal(mean([6, 3, 1, 11]), 5.25)
assert_equal(mean([12, 24, 48]), 28.0)
assert_equal(mean([-2, -9, 6, 1]), -1.0)
assert_equal(mean([]), None)


def square(numbers: [int]) -> [int]:
    
    '''
    This function sqaures all the numbers in the original list,
    and puts the new values in a new list.
    
    Args:
    numbers [int]: A list of integers is taken by this function.
    
    Returns:
    ([int]): A list of integers is returned by this function.
    '''
    
    new_numbers = []
    for number in numbers:
        new_numbers.append(number**2)
    return(new_numbers)

assert_equal(square([2, 4, 5, 1]), [4, 16, 25, 1])
assert_equal(square([-2, 7, 3]), [4, 49, 9])
assert_equal(square([12, 8, 9, 10, 11]), [144, 64, 81, 100, 121])
assert_equal(square([-3, -4, -5]), [9, 16, 25])
assert_equal(square([100]), [10000])


def diff(numbers: [int], subtrahend: int) -> [int]:
    
    '''
    This function subtractes each number in the list by the subtrahend
    and puts the new values in a new list.
    
    Args:
    numbers [int]: A list of integers is taken by this function.
    subtrahend [int]: A integer is taken by this function.
    
    Returns:
    ([int]): A list of integers is returned by this function.
    '''
    
    new_numbers = []
    for number in numbers:
        new_numbers.append(number - subtrahend)
    return (new_numbers)

assert_equal(diff([3, 6, 9, 1, 11, 17], 5), [-2, 1, 4, -4, 6, 12])
assert_equal(diff([-2, 7, 4, 1, 9], -1), [-1, 8, 5, 2, 10])
assert_equal(diff([13, 14, 15], 10), [3, 4, 5])
assert_equal(diff([1000000], 1000000), [0])
assert_equal(diff([45, 35, 25, 15, 5], 5), [40, 30, 20, 10, 0])


def standard_deviation(numbers: [int]) -> float:
    
    '''
    This function calculates the standard deviation of the
    numbers in the list.
    
    Args:
    numbers [int]: A list of integers is taken by this function.
    
    Returns:
    (float): A float value is returned by this function.
    '''
    
    new_numbers = []
    if count(numbers) < 2:
        return (None)
    total = diff(numbers, mean(numbers))
    new_numbers = square(total)
    total = summate(new_numbers)
    total = total / (count(numbers) - 1)
    total = total**(1/2)
    return (total)
    
        
assert_equal(standard_deviation([3, 2, 1]), 1.0)
assert_equal(standard_deviation([3, 3, 3]), 0.0)


def main(question: str, results: [int]) -> str:
    
    '''
    This function returns the question and answers from the survey
    and includes all the statistics based on that data.
    
    Args:
    question (str): The survey question that was asked.
    results ([int]): The answers that were given from people.
    
    Returns:
    (str): All the analystics from the survey. 
    '''
    
    print("We asked", count(results), "people the following question.")
    print(' "'+question+'"')
    print("Here are the statistical results:")
    print("\tSum:", summate(results))
    print("\tMean:", mean(results))
    print("\tStandard Deviation:", standard_deviation(results))
    
QUESTION = "How many pets do you have currently?"

ANSWERS = [0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 10]

PLEDGE = """I swear that I actually asked this question of at least 16 people and
          recorded their data without modifying the results.
          I understand that falsifying data in this course is really lame."""
          
ANALYSIS = "Sum: 33 /n Mean: 2.0625 /n Standard Deviation: 2.489143092177172"

main(QUESTION, ANSWERS)
