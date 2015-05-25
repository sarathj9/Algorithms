import collections
import sys
import json

__author__ = 'sarath'


class MinDistancePath():
    ladders = {}
    end_point = 21
    start_point = 1
    ladder_start_points = []
    ladder_end_points = []
    ladder_paths = collections.defaultdict(list)

    def get_hops(self, hops_diff):
        return (hops_diff / 6) + 1

    def get_next_ladder_start_point(self, current_ladder_start_point):
        try:
            index = self.ladder_start_points.index(current_ladder_start_point)
            return max(self.ladder_start_points[:index])
        except ValueError as e:
            print(e)
            return self.start_point

    def get_next_ladder_end_point(self, current_ladder_end_point):
        try:
            index = self.ladder_end_points.index(current_ladder_end_point)
            return min(self.ladder_end_points[index + 1:])
        except ValueError as e:
            print(e)
            return self.end_point

    def original_hops(self):
        # finding hops from the ladders --original hops
        for ladder_start_point in self.ladder_start_points:
            ladder_end_point = self.ladders[ladder_start_point]
            self.ladder_paths[ladder_start_point] = [(ladder_end_point, 1)]
        print('original ', json.dumps(self.ladder_paths))

    def min_path_to_start_point(self):
        # finding minimum paths from each ladder start point
        for ladder_start_point in self.ladder_start_points:
            if ladder_start_point > self.start_point and ladder_start_point not in self.ladder_end_points:
                point1 = self.get_next_ladder_start_point(ladder_start_point)
                self.ladder_paths[point1].append((ladder_start_point, self.get_hops(ladder_start_point - point1)))
        print('after touching start points', json.dumps(self.ladder_paths))

    def min_path_to_end_point(self):
        # finding minimum paths from each ladder end point
        for ladder_end_point in self.ladder_end_points:
            if ladder_end_point < self.end_point and ladder_end_point not in self.ladder_start_points:
                point2 = self.get_next_ladder_end_point(ladder_end_point)
                self.ladder_paths[ladder_end_point].append((point2, self.get_hops(point2 - ladder_end_point)))
        print('after touching end point', json.dumps(self.ladder_paths))

    def find_all_distances(self):
        distances = collections.defaultdict(list)
        neighbour_stack = [(self.start_point, 0)]
        weight = 0
        path = []
        saved_path = [self.start_point]
        saved_weight = 0
        while neighbour_stack:
            next_neighbour = neighbour_stack.pop()
            weight += next_neighbour[1]
            path.append(next_neighbour[0])
            if next_neighbour[0] != self.end_point:
                multi_paths = len(self.ladder_paths[next_neighbour[0]])
                if multi_paths > 1:
                    saved_path = list(path)
                    saved_weight = weight
                for n in [neighbours1 for neighbours1 in self.ladder_paths[next_neighbour[0]]]:
                    neighbour_stack.append(n)
            else:
                paths = []
                if weight in distances:
                    paths = distances[weight]
                paths.append(path)
                distances[weight] = paths
                path = saved_path
                saved_path = [self.start_point]
                weight = saved_weight
                saved_weight = 0
        return distances

    def find_min_distance(self, csv_file):
        with open(csv_file, 'r') as ladder_info:
            for line in ladder_info:
                ladder_info = line.strip().split(",")
                self.ladders[int(ladder_info[1])] = int(ladder_info[2])
        self.ladder_start_points = sorted(set(self.ladders.keys()))
        self.ladder_end_points = sorted(set(self.ladders.values()))
        print('ladder_start_points', self.ladder_start_points)
        print('ladder_end_points', self.ladder_end_points)

        self.original_hops()
        self.min_path_to_start_point()
        self.min_path_to_end_point()

        distances = self.find_all_distances()
        min_distance = min(distances.keys())
        print("min distance path(s)", distances[min_distance], " with distance", min_distance)