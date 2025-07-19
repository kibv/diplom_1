from praktikum.database import Database

class TestDatabase:
    def test_database_init(self):
        db = Database()
        assert len(db.available_buns()) == 3
        assert db.available_buns()[0].get_name() == "black bun"
        assert len(db.available_ingredients()) == 6
        assert db.available_ingredients()[0].get_name() == "hot sauce"

    def test_get_bun_by_name(self):
        db = Database()
        bun = next((b for b in db.available_buns() if b.get_name() == "black bun"), None)
        assert bun is not None
        assert bun.get_name() == "black bun"
        assert bun.get_price() == 100

    def test_get_bun_by_name_not_found(self):
        db = Database()
        bun = next((b for b in db.available_buns() if b.get_name() == "nonexistent bun"), None)
        assert bun is None

    def test_get_ingredient_by_name(self):
        db = Database()
        ingredient = next((i for i in db.available_ingredients() if i.get_name() == "hot sauce"), None)
        assert ingredient is not None
        assert ingredient.get_name() == "hot sauce"
        assert ingredient.get_price() == 100

    def test_get_ingredient_by_name_not_found(self):
        db = Database()
        ingredient = next((i for i in db.available_ingredients() if i.get_name() == "nonexistent ingredient"), None)
        assert ingredient is None
