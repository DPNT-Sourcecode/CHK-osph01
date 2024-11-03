from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.sum(1, 2) == 3

    def test_sum2(self):
        assert sum_solution.sum(0, 0) == 0
        assert sum_solution.sum(100, 100) == 200

    def test_sum3(self):
        assert sum_solution.sum(100, 0) == 100
        assert sum_solution.sum(0, 100) == 100
