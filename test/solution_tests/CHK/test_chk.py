from solutions.CHK import checkout_solution


class TestHello():
    def test_checkout1(self):
        assert checkout_solution.checkout("ABCDE") == 155

    def test_checkout2(self):
        assert checkout_solution.checkout("AAAAA") == 200

    def test_checkout3(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_checkout4(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_checkout5(self):
        assert checkout_solution.checkout("BB") == 45

    def test_checkout6(self):
        assert checkout_solution.checkout("EEBBBA") == 175