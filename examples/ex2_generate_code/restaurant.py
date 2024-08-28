# load food.json into a dataclass
import json
from dataclasses import dataclass
from typing import List
from decimal import Decimal


@dataclass
class Food:
    name: str
    price: Decimal
    kcal: int
    is_vegan: bool


class Restaurant:
    def __init__(self, file_path):
        self.food = self.__load_food(file_path)

    def get_food(self) -> List[Food]:
        return self.food

    def __load_food(self, file_path):
        with open(file_path) as f:
            data = json.load(f)
        return [Food(**food) for food in data["food"]]

    def filter_vegan(self) -> List[Food]:
        return [food for food in self.food if food.is_vegan]

    def filter_non_vegan(self) -> List[Food]:
        return [food for food in self.food if not food.is_vegan]

    def filter_high_calories(self, threshold: int) -> List[Food]:
        return [food for food in self.food if food.kcal > threshold]


restaurant = Restaurant("food.json")
food = restaurant.get_food()
vegan = restaurant.filter_vegan()
non_vegan = restaurant.filter_non_vegan()
high_calories = restaurant.filter_high_calories(500)

print(food)
print("----------")
print(vegan)
print("----------")
print(non_vegan)
print("----------")
print(high_calories)
