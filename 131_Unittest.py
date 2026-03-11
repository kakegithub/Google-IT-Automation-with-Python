from typing import List

"""Simple module modeling a cake factory for demonstration and unit tests.
The CakeFactory class lets you create a cake with a type and size, add toppings,
check the ingredients list, and compute the price.  Example usage at the
bottom shows how the class might be exercised interactively or during tests.
"""


class CakeFactory:
    """Represent a customizable cake and calculate its price and ingredients.

    Attributes:
        cake_type (str): type of cake, e.g. "chocolate" or other.
        size (str): size of the cake: "small", "medium", or "large".
        toppings (List[str]): added toppings that affect ingredients and price.
        price (float): current computed price of the cake.
    """

    def __init__(self, cake_type: str, size: str):
        """Initialize a new cake with given type and size.

        The price is set according to a simple scheme:
        - chocolate cakes have a base price of 10, others cost 8.
        - medium cakes add 2, large cakes add 4 (small adds nothing).
        """
        # store user-provided attributes
        self.cake_type = cake_type
        self.size = size
        self.toppings = []  # start with no toppings

        # Price based on cake type and size
        self.price = 10 if self.cake_type == "chocolate" else 8
        self.price += 2 if self.size == "medium" else 4 if self.size == "large" else 0

    def add_topping(self, topping: str):
        """Attach a new topping and increment the cake's price.

        Args:
            topping (str): name of the topping to add (e.g. "sprinkles").
        """
        self.toppings.append(topping)
        # Adding 1 to the price for each topping
        self.price += 1

    def check_ingredients(self) -> List[str]:
        """Return a list of all ingredients needed for this cake.

        The base ingredients flour, sugar and eggs are always present.  Add
        cocoa for chocolate cakes or vanilla extract for others.  Any toppings
        previously added are included as well.
        """
        ingredients = ['flour', 'sugar', 'eggs']
        # choose flavouring based on cake type
        ingredients.append(
            'cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
        # toppings contribute to ingredients as well
        ingredients += self.toppings
        return ingredients

    def check_price(self) -> float:
        """Return the current price of the cake.

        Price is maintained incrementally as toppings are added, so this method
        simply returns the stored value.
        """
        return self.price


# Example of creating a cake and adding toppings
# This block demonstrates how the class could be used in a script or
# unit tests.  When imported as a module the following lines would execute
# at import time, so they are typically guarded or moved into a test file.
if __name__ == "__main__":
    cake = CakeFactory("chocolate", "medium")
    cake.add_topping("sprinkles")
    cake.add_topping("cherries")
    cake_ingredients = cake.check_ingredients()
    cake_price = cake.check_price()

    # print or inspect the results when running the file directly
    print(cake_ingredients, cake_price)
