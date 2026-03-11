"""Unit tests for the CakeFactory class defined in 131_Unittest.py.

The tests verify that cakes are created with the correct attributes, that
toppings affect the ingredients and price, and that price calculations are
accurate.  Running this file directly will execute the test suite.
"""

import unittest

# Load CakeFactory class from the exercise file by filename.  Because the
# source file name begins with a digit ("131_Unittest.py"), it cannot be
# imported with the normal `import` statement (module names must start with
# a letter).  We therefore use importlib.util to load the module from path
# and extract the class object.
import importlib.util
import os

_this_dir = os.path.dirname(__file__)
_cake_path = os.path.join(_this_dir, "131_Unittest.py")
_spec = importlib.util.spec_from_file_location("cake_module", _cake_path)
_cake_module = importlib.util.module_from_spec(_spec)  # type: ignore
_spec.loader.exec_module(_cake_module)  # type: ignore
CakeFactory = _cake_module.CakeFactory

# import the class we're testing - module name numeric prefix requires
# using importlib or __import__ if necessary.  Here we assume the file is
# on the PYTHONPATH and can be imported normally as a module name.


class TestCakeFactory(unittest.TestCase):
    """TestCase subclass containing unit tests for CakeFactory."""

    def test_create_cake(self):
        # A cake created with specific type and size should have those
        # attributes and an appropriate base price.
        cake = CakeFactory("vanilla", "small")
        self.assertEqual(cake.cake_type, "vanilla")
        self.assertEqual(cake.size, "small")
        self.assertEqual(cake.price, 8)  # Vanilla cake, small size

    def test_add_topping(self):
        # Adding a topping should record it in the toppings list.
        cake = CakeFactory("chocolate", "large")
        cake.add_topping("sprinkles")
        self.assertIn("sprinkles", cake.toppings)

    def test_check_ingredients(self):
        # Ingredients list should include base ingredients, correct flavoring,
        # and any toppings that were added.  Vanilla extract must not appear
        # for a chocolate cake.
        cake = CakeFactory("chocolate", "medium")
        cake.add_topping("cherries")
        ingredients = cake.check_ingredients()
        self.assertIn("cocoa", ingredients)
        self.assertIn("cherries", ingredients)
        self.assertNotIn("vanilla extract", ingredients)

    # Fixing the test_check_price method
    def test_check_price(self):
        # Price should reflect base price plus increments for size and
        # each topping added.
        cake = CakeFactory("vanilla", "large")
        cake.add_topping("sprinkles")
        cake.add_topping("cherries")
        price = cake.check_price()
        self.assertEqual(price, 14)  # Vanilla cake, large size + 2 toppings


# Running the unittests when the module is executed directly
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))