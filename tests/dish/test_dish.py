from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    # Helpers
    strError = "Dish price must be greater then zero."
    # Teste TypeError
    with pytest.raises(TypeError, match="Dish price must be float."):
        dish = Dish('Pão', '2.00')
        return dish
    # Teste ValueError
    with pytest.raises(ValueError, match=strError):
        dish = Dish('Pão', 0)
        return dish
    # Teste Dish Name
    name = 'Pão'
    price = 2.00
    dish1 = Dish(name, price)
    dish2 = Dish(name, price)
    dish3 = Dish('Café', 1.00)
    assert dish1.name == name
    # Teste __repr__
    assert dish1.__repr__() == f"Dish('{name}', R${price:.2f})"
    # Teste __eq__ is equal
    assert dish1.__eq__(dish2) is True
    # Teste __eq__ is different
    assert dish1.__eq__(dish3) is False
    # Teste add Ingredient
    ingredient = Ingredient('ovo')
    dish1.add_ingredient_dependency(ingredient, 2)
    assert dish1.get_ingredients() == {Ingredient('ovo')}
    # Teste Hash is equal
    assert dish1.__hash__() == dish2.__hash__()
    # Teste Hash is different
    assert dish1.__hash__() != dish3.__hash__()
    # Teste Restriction
    restriction = "{<Restriction.ANIMAL_DERIVED: 'ANIMAL_DERIVED'>}"
    assert str(dish1.get_restrictions()) == restriction
