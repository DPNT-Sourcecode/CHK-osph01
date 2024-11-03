from solutions.CHK import checkout_solution


class TestHello():
    def test_checkout1(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("G") == 20
        assert checkout_solution.checkout("H") == 10
        assert checkout_solution.checkout("I") == 35
        assert checkout_solution.checkout("J") == 60
        assert checkout_solution.checkout("K") == 70
        assert checkout_solution.checkout("L") == 90
        assert checkout_solution.checkout("M") == 15
        assert checkout_solution.checkout("N") == 40
        assert checkout_solution.checkout("O") == 10
        assert checkout_solution.checkout("P") == 50
        assert checkout_solution.checkout("Q") == 30
        assert checkout_solution.checkout("R") == 50
        assert checkout_solution.checkout("S") == 20
        assert checkout_solution.checkout("T") == 20
        assert checkout_solution.checkout("U") == 40
        assert checkout_solution.checkout("V") == 50
        assert checkout_solution.checkout("W") == 20
        assert checkout_solution.checkout("X") == 17
        assert checkout_solution.checkout("Y") == 20
        assert checkout_solution.checkout("Z") == 21

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
        assert checkout_solution.checkout("KK") == 120
        assert checkout_solution.checkout("KKKKK") == 310

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

    def test_checkout14(self):
        assert checkout_solution.checkout("SSS") == 45
        assert checkout_solution.checkout("TTT") == 45
        assert checkout_solution.checkout("XXX") == 45
        assert checkout_solution.checkout("YYY") == 45
        assert checkout_solution.checkout("ZZZ") == 45
        assert checkout_solution.checkout("ZYX") == 45
        assert checkout_solution.checkout("TSZ") == 45
        assert checkout_solution.checkout("YXS") == 45

    def test_checkout15(self):
        assert checkout_solution.checkout("STYXZ") == 82


