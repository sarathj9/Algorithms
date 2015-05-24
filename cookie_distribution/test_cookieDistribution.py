from unittest import TestCase
from cookie_distribution.CookieDistribution import CookieDistribution

__author__ = 'sarath'


class TestCookieDistribution(TestCase):
    distribution = CookieDistribution()

    def test_find_min_cookies_1(self):
        new_array = [1, 2, 3, 4, 5, 6]
        self.distribution.find_min_cookies(new_array)

    def test_find_min_cookies_2(self):
        new_array = [4, 1, 2, 3, 1, 4, 9, 11]
        self.distribution.find_min_cookies(new_array)

    def test_find_min_cookies_3(self):
        new_array = [15, 20, 5, 21, 50, 20, 11, 6, 10, 19, 11, 8, 9, 12]
        self.distribution.find_min_cookies(new_array)

    def test_find_min_cookies_4(self):
        new_array = [1, 2, 3, 7, 6, 5, 4]
        self.distribution.find_min_cookies(new_array)

    def test_find_min_cookies_5(self):
        new_array = [5, 10, 15, 11, 9, 8, 13, 25, 40, 50, 35, 12, 7]
        self.distribution.find_min_cookies(new_array)

