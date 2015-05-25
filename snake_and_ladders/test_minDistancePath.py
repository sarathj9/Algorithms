from unittest import TestCase
from snake_and_ladders.MinDistancePath import MinDistancePath

__author__ = 'sarath'


class TestMinDistancePath(TestCase):
    min_distance_finder = MinDistancePath()

    def test_find_min_distance(self):
        self.min_distance_finder.find_min_distance("ladders/ladders_info.csv")

    def test_find_min_distance1(self):
        self.min_distance_finder.find_min_distance("ladders/ladders_info2.csv")

    def test_find_min_distance2(self):
        self.min_distance_finder.find_min_distance("ladders/ladders_info3.csv")
