from solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello("iwoca") == "Hello, iwoca!"

    def test_hello(self):
        assert hello_solution.hello("") == "Hello, !"

    def test_hello(self):
        assert hello_solution.hello("Hello \{\} hello") == "Hello, Hello \{\} hello!"