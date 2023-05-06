from ingredient import Ingredient

ingredients = []

def add_ingredients(name, calories, protein, fat, carbs, fiber, ingredient_type) -> None:
    ingredients.append(Ingredient((name, calories, protein, fat, carbs, fiber, ingredient_type)))


def find_all():
    return ingredients.copy()

def find_by_name_like(name: str):
    copy = find_all()
    result = []

    for ingredient in copy:
    return (lambda ingredient: name.casefold() in ingredient.name.casefold(), copy)