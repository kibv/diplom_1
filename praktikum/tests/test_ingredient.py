from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
class TestIngredient:
    def test_ingredient_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 20)
        assert ingredient.get_name() == "Ketchup"

    def test_ingredient_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Cheese", 30)
        assert ingredient.get_price() == 30

    def test_ingredient_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Mayo", 25)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
