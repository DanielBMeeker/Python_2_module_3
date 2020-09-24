"""
Program: NumPy_array_math.py
Author: Daniel Meeker
Date: 9/17/2020

This program demonstrates using NumPy in Python.
"""
import numpy as np

if __name__ == '__main__':
    array_1 = np.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
    array_2 = np.array([[1, 2, 5], [8, 0, 12], [11, 3, 22]])
    array_1_even = array_1 % 2 == 0
    array_1_slice = array_1[0:2, 0:2]
    array_sum = np.add(array_1, array_2)
    array_multiply = np.multiply(array_1, array_2)
    # Print array_1 to the console
    print(array_1)
    # Print array_1's shape
    print(array_1.shape)
    # Print a 2x2 slice starting at 0,0 and going to 1,1
    print(array_1_slice)
    # Output a boolean on whether an element is even or odd
    print(array_1_even)
    # Add the two arrays together elementwise
    print(array_sum)
    # Multiply the arrays together elementwise
    print(array_multiply)
    # Print the sum of all elements in array_2
    print(array_2.sum())
    # Print the product of all elements in array_2
    print(array_2.prod())
    # Print the max value of all elements in array_2
    print(array_2.max())
    # Print the min value of all elements in array_2
    print(array_2.min())
