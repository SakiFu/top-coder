"""
TopCoder Security Agency (TSA, established today) has just invented a new encryption system! 
This encryption system takes as its input a list of numbers to encrypt.
You work at TSA and your task is to implement a very important part of the encryption process. 
You are allowed to pick one number in the input list and increment its value by 1. 
This should be done in such way that the product of all numbers in the llist after this change becomes as large as possible.
GIven the list, return the maximum product you can obtain. It is guaranteed that the return value will not exceed 2**62

Example:
numbers = [1,2,3]
Output: 12
"""


def cryptography(numbers):
    short_list = numbers[:]
    short_list.remove(min(short_list))
    short_sum = reduce(lambda x, y: x* y, short_list)
    return reduce(lambda x, y: x* y, numbers) + short_sum