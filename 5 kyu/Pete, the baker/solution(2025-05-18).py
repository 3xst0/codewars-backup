def cakes(recipe, available):
    for ingredient in recipe.keys():
        if ingredient not in available.keys():
            return 0
    return min([available.get(ingredient) // recipe.get(ingredient) for ingredient in available.keys() if recipe.get(ingredient)])