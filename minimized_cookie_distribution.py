from __builtin__ import xrange

__author__ = 'sarath'

# Finding all possible non decreasing marks/scores


def non_increasing_sequence(start_off=0):
    print(start_off)
    index_initial = start_off
    index_final = start_off

    for i in range(index_initial, len(student_array) - 1):
        next1 = i + 1
        if student_array[i] < student_array[next1]:
            index_final = next1
        else:
            break

    print(index_initial, index_final+1)
    for i in range(index_initial, index_final+1):
        print(str(student_array[i]) + ", ")
    if index_initial == index_final:
        print("no more increasing arrays")
    return index_final+1

student_array = [6, 5, 4, 3, 2, 1]
student_array = [1, 2, 3, 4, 5, 6]
student_array = [4, 1, 2, 3, 1, 4, 9, 11]
student_array = [15, 20, 5, 21, 50, 20, 11, 6, 10, 19, 11, 8, 9, 12]
student_array = [1, 2, 3, 7, 6, 5, 4]

# Initialize Cookie array with all zeros.
chocolate_array = [0] * len(student_array)

n = 0
while n < len(student_array):
    last_index = non_increasing_sequence(n)
    n = last_index
    print("next")
