__author__ = 'sarath'

# student_array = [4, 1, 2, 3, 1, 4, 9, 11]
student_array = [6, 5, 4, 3, 2, 1]

# Initialize Cookie array with all zeros.
chocolate_array = [0] * len(student_array)

# Finding all possible non decreasing marks/scores


def non_increasing_sequence(start_off=0):
    print(start_off)
    index_initial = 0
    index_final = 0
    for i in range(start_off, len(student_array) - 1):
        next1 = i + 1
        if student_array[i] > student_array[next1]:
            index_initial = next1
            break
    for i in range(index_initial, len(student_array) - 1):
        next1 = i + 1
        if student_array[i] > student_array[next1]:
            index_final = next1
            break
        if next1 == len(student_array) - 1:
            index_final = next1 + 1
    print(index_initial, index_final)
    for i in range(index_initial, index_final):
        print(str(student_array[i]) + ", ")
    if index_initial == index_final:
        print("no more increasing arrays")
    return index_final


sequence = non_increasing_sequence()
print("next")
non_increasing_sequence(sequence - 1)