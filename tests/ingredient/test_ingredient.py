from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1 Teste
def test_ingredient():
    name = 'farinha'
    otherName = 'frango'
    ingredient1 = Ingredient(name)
    ingredient2 = Ingredient(name)
    ingredient3 = Ingredient(otherName)
    # Teste Name
    assert ingredient1.name == name
    # Teste __repr__
    assert ingredient1.__repr__() == f"Ingredient('{name}')"
    # Teste __eq__
    assert ingredient1.__eq__(ingredient2) is True
    # Teste __hash__ is equal
    assert ingredient1.__hash__() == ingredient2.__hash__()
    # Teste __hash__ is different
    assert ingredient1.__hash__() != ingredient3.__hash__()
    # Teste Restrictions
    assert str(ingredient1.restrictions) == "{<Restriction.GLUTEN: 'GLUTEN'>}"
