import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_invalid_index(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1

    def test_move_ingredient_invalid_index(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
            burger.move_ingredient(10, 0)

    def test_move_ingredient_empty_list(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 0)

    @pytest.mark.parametrize("bun_price, ingredients_prices, expected_price", [
        (100, [50, 50], 300),
        (50, [20, 30, 40], 190),
        (0, [], 0),
    ])
    def test_get_price(self, bun_price, ingredients_prices, expected_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredients_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_price

    def test_get_price_no_bun(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)
        with pytest.raises(AttributeError):
            burger.get_price()

    @pytest.mark.parametrize("bun_name, ingredient_data, expected_receipt", [
        ("Black Bun", [(INGREDIENT_TYPE_SAUCE, "Ketchup", 50)], "(==== Black Bun ====)\n= sauce Ketchup =\n(==== Black Bun ====)\n\nPrice: 150"),
        ("White Bun", [(INGREDIENT_TYPE_FILLING, "Cheese", 25), (INGREDIENT_TYPE_SAUCE, "Mayo", 25)], "(==== White Bun ====)\n= filling Cheese =\n= sauce Mayo =\n(==== White Bun ====)\n\nPrice: 150"),
    ])
    def test_get_receipt(self, bun_name, ingredient_data, expected_receipt):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)
        for ing_type, name, price in ingredient_data:
            mock_ingredient = Mock()
            mock_ingredient.get_name.return_value = name
            mock_ingredient.get_price.return_value = price
            mock_ingredient.get_type.return_value = ing_type
            burger.add_ingredient(mock_ingredient)
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_no_bun(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "Ketchup"
        mock_ingredient.get_price.return_value = 50
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock_ingredient)
        with pytest.raises(AttributeError):
            burger.get_receipt()