__author__ = 'sarath'


class CookieDistribution(object):
    seq_boundaries = []
    student_array = []
    cookie_array = []

    def check_cookie(self):
        align_bool = True
        for boundary in range(len(self.seq_boundaries)):
            next2 = self.seq_boundaries[boundary] + 1
            if self.student_array[self.seq_boundaries[boundary]] > self.student_array[next2]:
                cookie_balance = self.cookie_array[self.seq_boundaries[boundary]] > self.cookie_array[next2]
                print(self.student_array[self.seq_boundaries[boundary]], self.student_array[next2],
                      self.cookie_array[self.seq_boundaries[boundary]], self.cookie_array[next2],
                      cookie_balance)
                align_bool = align_bool and cookie_balance
        print("done", align_bool)
        return align_bool

    def balance_cookies(self):
        for i in range(len(self.seq_boundaries)):
            next1 = self.seq_boundaries[i] + 1
            if self.student_array[self.seq_boundaries[i]] > self.student_array[next1] and not (
                    self.cookie_array[self.seq_boundaries[i]] > self.cookie_array[next1]):
                self.cookie_array[self.seq_boundaries[i]] += 1


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
        self.cookie_array = [0] * len(self.student_array)
        self.seq_boundaries = []
        n = 0
        while n < len(self.student_array):
            scores_range = self.non_increasing_sequence(n)
            self.seq_boundaries.append(scores_range[1] - 1)
            min_cookie = 1
            # Assigning incremental cookies for increasing sequences
            for cookie_index in range(scores_range[0], scores_range[1]):
                self.cookie_array[cookie_index] = min_cookie
                min_cookie += 1

            last_index = self.non_increasing_sequence(n)[1]
            n = last_index

        # deleting the last element from the boundary check
        self.seq_boundaries.pop()
        print(self.student_array)
        print(self.cookie_array)
        print(self.seq_boundaries)
        # Check cookies at the boundaries, If not balanced, balance at the corresponding positions
        while self.check_cookie() is False:
            self.balance_cookies()

        cookies_distributed = 0
        for cookie in self.cookie_array:
            cookies_distributed += cookie
        print("student array, cookie distribution, Minimum cookies distributed", self.student_array,
              self.cookie_array, cookies_distributed)
