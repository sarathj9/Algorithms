from __builtin__ import xrange

__author__ = 'sarath'


# check boundaries as others will be good.
def check_chocolates():
    align_bool = True
    for boundary in range(len(incr_boundaries)):
        next2 = incr_boundaries[boundary] + 1
        if student_array[incr_boundaries[boundary]] > student_array[next2]:
            cookie_balance = chocolate_array[incr_boundaries[boundary]] > chocolate_array[next2]
            print(student_array[incr_boundaries[boundary]], student_array[next2],
                  chocolate_array[incr_boundaries[boundary]], chocolate_array[next2],
                  cookie_balance)
            align_bool = align_bool and cookie_balance
    print("done", align_bool)
    return align_bool


def align_cookies():
    for i in range(len(incr_boundaries)):
        next1 = incr_boundaries[i] + 1
        if student_array[incr_boundaries[i]] > student_array[next1] and not (
                chocolate_array[incr_boundaries[i]] > chocolate_array[next1]):
            chocolate_array[incr_boundaries[i]] += 1


# Finding all possible non decreasing marks/scores
def non_increasing_sequence(start_off=0):
    index_initial = start_off
    index_final = start_off

    for i in range(index_initial, len(student_array) - 1):
        next1 = i + 1
        if student_array[i] < student_array[next1]:
            index_final = next1
        else:
            break
    return index_initial, index_final + 1

# student_array = [6, 5, 4, 3, 2, 1]
student_array = [1, 2, 3, 4, 5, 6]
student_array = [4, 1, 2, 3, 1, 4, 9, 11]
# student_array = [15, 20, 5, 21, 50, 20, 11, 6, 10, 19, 11, 8, 9, 12]
student_array = [1, 2, 3, 7, 6, 5, 4]
# student_array = [5, 10, 15, 11, 9, 8, 13, 25, 40, 50, 35, 12, 7]
# Initialize Cookie array with all zeros.
chocolate_array = [0] * len(student_array)
incr_boundaries = []
n = 0
while n < len(student_array):
    scores_range = non_increasing_sequence(n)
    size = scores_range[1] - scores_range[0]
    incr_boundaries.append(scores_range[1] - 1)
    min_cookie = 1
    for cookie_index in range(scores_range[0], scores_range[1]):
        print(cookie_index)
        chocolate_array[cookie_index] = min_cookie
        min_cookie += 1

    last_index = non_increasing_sequence(n)[1]
    n = last_index
    print("next")

# deleting the last element from the boundary check

incr_boundaries.pop()

print(student_array)
print(chocolate_array)
print(incr_boundaries)

while check_chocolates() is False:
    align_cookies()
    print(chocolate_array)

exit()
