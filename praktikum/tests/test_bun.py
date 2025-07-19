from praktikum.bun import Bun

class TestBun:
    def test_bun_get_name(self):
        bun = Bun("Black Bun", 100)
        assert bun.get_name() == "Black Bun"

    def test_bun_get_price(self):
        bun = Bun("White Bun", 50)
        assert bun.get_price() == 50