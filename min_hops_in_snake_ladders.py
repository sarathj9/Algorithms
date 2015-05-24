import collections
import sys

__author__ = 'sarath'

ladders = {}
end_point = 21
start_point = 1
snake_and_ladders = [0] * 21

for i in range(start_point, end_point + 1):
    snake_and_ladders[i - 1] = i

with open(sys.argv[1], 'r') as csv_file:
    for line in csv_file:
        ladder_info = line.strip().split(",")
        ladders[int(ladder_info[1])] = int(ladder_info[2])

print(snake_and_ladders)
print(ladders)

ladder_start_points = sorted(set(ladders.keys()))
ladder_end_points = sorted(set(ladders.values()))

print('ladder_start_points', ladder_start_points)
print('ladder_end_points', ladder_end_points)


def get_hops(hops_diff):
    # if hops_diff < 7:
    # return hops_diff
    return (hops_diff / 6) + 1


def get_next_ladder_start_point(current_ladder_start_point):
    try:
        index = ladder_start_points.index(current_ladder_start_point)
        return max(ladder_start_points[:index])
    except ValueError as e:
        print(e)
        return start_point


def get_next_ladder_end_point(current_ladder_end_point):
    try:
        index = ladder_end_points.index(current_ladder_end_point)
        return min(ladder_end_points[index+1:])
    except ValueError as e:
        print(e)
        return end_point


ladder_paths = collections.defaultdict(list)

for ladder_start_point in ladder_start_points:
    ladder_end_point = ladders[ladder_start_point]
    ladder_paths[ladder_start_point] = [(ladder_end_point, 1)]
print('original ', ladder_paths)


# if max_end_point != no_of_tiles:
# ladder_paths[max_end_point] = [(no_of_tiles, get_hops(no_of_tiles - max_end_point))]

for ladder_start_point in ladder_start_points:
    if ladder_start_point > start_point and ladder_start_point not in ladder_end_points:
        point1 = get_next_ladder_start_point(ladder_start_point)
        ladder_paths[point1].append((ladder_start_point, get_hops(ladder_start_point - point1)))
print('after touching start points', ladder_paths)

for ladder_end_point in ladder_end_points:
    if ladder_end_point < end_point and ladder_end_point not in ladder_start_points:
        print('ladder end point', ladder_end_point)
        point2 = get_next_ladder_end_point(ladder_end_point)
        ladder_paths[ladder_end_point].append((point2, get_hops(point2 - ladder_end_point)))
print('after touching end point', ladder_paths)


neighbours = collections.defaultdict(list)

# ladder_paths = {1: [(5, 1), (7, 1)], 5: [(13, 1)], 7: [(19, 1)], 13: [(19, 1)], 19: [(21, 2)]}
# ladder_paths = {1: [(8, 2), (2, 1), (7, 2), (5, 1), (6, 1), (9, 1)], 8: [(20, 4)], 2: [(7, 1)], 7: [(12, 1)],
#                5: [(12, 1)], 6: [(12, 1)], 9: [(15, 1)], 20: [(21, 1)], 12: [(17, 1), (18, 2)], 15: [(18, 1)],
#                17: [(21, 1)], 18: [(21, 1)]}


# neighbour_stack = [neighbours1[0] for neighbours1 in ladder_paths[start_point]]
neighbour_stack = [(start_point, 0)]
weight = 0

print("ladder paths", ladder_paths)
path = []
saved_path = [start_point]
saved_weight = 0
while neighbour_stack:
    # print("neighbour stack", neighbour_stack)
    next_neighbour = neighbour_stack.pop()
    weight += next_neighbour[1]
    path.append(next_neighbour[0])
    # print(next_neighbour)
    if next_neighbour[0] != end_point:
        multi_paths = len(ladder_paths[next_neighbour[0]])
        if multi_paths > 1:
            saved_path = list(path)
            saved_weight = weight
            # print("saved path", saved_path)
        for n in [neighbours1 for neighbours1 in ladder_paths[next_neighbour[0]]]:
            neighbour_stack.append(n)
    else:
        print("all paths", path, weight)
        path = saved_path
        saved_path = [start_point]
        # print("fresh path, saved path", path, saved_path)
        weight = saved_weight
        saved_weight = 0



