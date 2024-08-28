from dataclasses import dataclass
from typing import List

@dataclass
class Food:
    name: str
    price: float
    description: str

@dataclass
class Restaurant:
    name: str
    location: str
    menu: List[Food]

    def add_food(self, food: Food):
        self.menu.append(food)

    def remove_food(self, food: Food):
        self.menu.remove(food)
