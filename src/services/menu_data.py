# Req 3
import csv
from models.ingredient import Ingredient
from models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.readingFile(source_path)

    def readingFile(self, source_path):
        menu = {}
        with open(source_path, encoding="utf-8") as file:
            header, *data = csv.reader(file)
            for name, price, ingredient, num in data:
                try:
                    if menu[name]:
                        menu[name].add_ingredient_dependency(
                            Ingredient(ingredient), int(num)
                        )
                except KeyError:
                    menu[name] = Dish(name, float(price))
                    menu[name].add_ingredient_dependency(
                        Ingredient(ingredient), int(num)
                    )
        self.settingDishes(menu)

    def settingDishes(self, menu):
        for dish in menu:
            self.dishes.add(menu[dish])


x = MenuData('data/menu_base_data.csv')
