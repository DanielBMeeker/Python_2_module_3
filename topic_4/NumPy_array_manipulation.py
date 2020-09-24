"""
Program: NumPy_array_manipulation.py
Author: Daniel Meeker
Date: 9/17/2020

This program demonstrates using numpy for array manipulations.
"""
import numpy as np

if __name__ == '__main__':
    array = np.array([[1, 2, 5], [8, 0, -7], [7, 3, 9]])
    print(array)
    # transpose and print to console
    array = array.transpose()
    print(array)
    # swap the axes and print
    array = array.swapaxes(0, 1)
    print(array)
    # Flip the array across the horizontal axis
    array = np.fliplr(array)
    print(array)
    # Add a row at the bottom
    array = np.insert(array, 3, values=[3, 4, 5], axis=0)
    print(array)
    # Add a column at the end
    array = np.insert(array, 3, values=[7, 8, 9, 0], axis=1)
    print(array)
    # delete the column at the end
    array = np.delete(array, 3, axis=1)
    print(array)
    # reshape the array to 2 columns with 6 rows
    array = array.reshape((6, 2))
    print(array)
    # split the array into 3 2x2 arrays and print the middle array
    array = np.vsplit(array, (2, 4))
    print(array[1])
    # flatten the third array and print it to the console
    array = array[2].flatten()
    print(array)

