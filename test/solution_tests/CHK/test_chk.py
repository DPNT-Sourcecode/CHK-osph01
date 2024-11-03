from solutions.CHK import checkout_solution


class TestHello():
    def test_checkout1(self):
        assert checkout_solution.checkout("ABCDEF") == 165

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

    def test_checkout7(self):
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20

    def test_checkout8(self):
        assert checkout_solution.checkout("KK") == 150

    def test_checkout9(self):
        assert checkout_solution.checkout("PPPPP") == 200
        assert checkout_solution.checkout("PPPPPP") == 250

    def test_checkout10(self):
        assert checkout_solution.checkout("QQQ") == 80
        assert checkout_solution.checkout("QQQQ") == 110

    def test_checkout11(self):
        assert checkout_solution.checkout("QQQQRRR") == 230

    def test_checkout12(self):
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("UUUUU") == 160

    def test_checkout13(self):
        assert checkout_solution.checkout("VVVV") == 180
        assert checkout_solution.checkout("VVV") == 130
        assert checkout_solution.checkout("VV") == 90