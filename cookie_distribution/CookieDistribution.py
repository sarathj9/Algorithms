__author__ = 'sarath'


class CookieDistribution(object):
    incr_boundaries = []
    student_array = []
    chocolate_array = []

    def check_chocolates(self):
        align_bool = True
        for boundary in range(len(self.incr_boundaries)):
            next2 = self.incr_boundaries[boundary] + 1
            if self.student_array[self.incr_boundaries[boundary]] > self.student_array[next2]:
                cookie_balance = self.chocolate_array[self.incr_boundaries[boundary]] > self.chocolate_array[next2]
                print(self.student_array[self.incr_boundaries[boundary]], self.student_array[next2],
                      self.chocolate_array[self.incr_boundaries[boundary]], self.chocolate_array[next2],
                      cookie_balance)
                align_bool = align_bool and cookie_balance
        print("done", align_bool)
        return align_bool

    def align_cookies(self):
        for i in range(len(self.incr_boundaries)):
            next1 = self.incr_boundaries[i] + 1
            if self.student_array[self.incr_boundaries[i]] > self.student_array[next1] and not (
                    self.chocolate_array[self.incr_boundaries[i]] > self.chocolate_array[next1]):
                self.chocolate_array[self.incr_boundaries[i]] += 1


# Finding all possible non decreasing marks/scores
    def non_increasing_sequence(self, start_off=0):
        index_initial = start_off
        index_final = start_off

        for i in range(index_initial, len(self.student_array) - 1):
            next1 = i + 1
            if self.student_array[i] < self.student_array[next1]:
                index_final = next1
            else:
                break
        return index_initial, index_final + 1

    def find_min_cookies(self, new_array):
        self.student_array = list(new_array)
        self.chocolate_array = [0] * len(self.student_array)
        self.incr_boundaries = []
        n = 0
        while n < len(self.student_array):
            scores_range = self.non_increasing_sequence(n)
            self.incr_boundaries.append(scores_range[1] - 1)
            min_cookie = 1
            for cookie_index in range(scores_range[0], scores_range[1]):
                print(cookie_index)
                self.chocolate_array[cookie_index] = min_cookie
                min_cookie += 1

            last_index = self.non_increasing_sequence(n)[1]
            n = last_index
            print("next")

        # deleting the last element from the boundary check
        self.incr_boundaries.pop()
        print(self.student_array)
        print(self.chocolate_array)
        print(self.incr_boundaries)
        while self.check_chocolates() is False:
            self.align_cookies()
            print(self.chocolate_array)
