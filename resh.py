#номер 1.1
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit


    @property
    def quantity(self):
        return self._quantily

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("каче-во не м.б меньше или равна нулю")
        self._quantity = float(value)
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"


    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
        



    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return (self.name == other.name and self.unit == other.unit)
    


#номер 1.2
class Recipe:
    def __init__(self, title, ingredients = None):
        self.title = title
        self.ingredients = ingredients
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients


    def add_ingredient(self, ingredient: Ingredient):
        for i in self.ingredients:
            if i.name == ingredient.name and i.unit == ingredient.unit:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("ratio не может быть отриц")
        new_recipe = Recipe(self.title)
        for ingredient in self.ingredients:
            new_ingredient = Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)
            new_recipe.add_ingredient(new_ingredient)
        return new_recipe   


    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        ingredients_str = "\n".join(str(ingredient) for ingredient in self.ingredients)
        return f"{self.title}:\n{ingredients_str}"
    



#номер 1.4
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float):
        return DietaryRecipe(self.title, self.diet_type, super().scale(ratio).ingredients)

    def __str__(self):
        return f'[{self.diet_type}]' + super().__str__()
    



#номер 1.3
class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self,recipe, portions):
        if portions <= 0:
            raise ValueError('порция не может быть меньше или равно нулю')
        
