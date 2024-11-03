from solutions.CHK import checkout_solution


class TestHello():
    def test_checkout1(self):
        assert checkout_solution.checkout("ABCD") == 115
