import unittest
from template import *
from TestUtils import TestUtils

class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.restaurant = RestaurantManager()
        self.test_utils = TestUtils()

    def test_large_order_processing(self):
        """Test processing an order with maximum menu items"""
        try:
            # Order every item from the menu
            all_items = list(self.restaurant.menu.keys())
            total = self.restaurant.add_order("John", all_items)
            # Calculate expected total (with discounts for daily specials)
            expected_total = sum(
                price * 0.9 if item in self.restaurant.daily_specials else price 
                for item, price in self.restaurant.menu.items()
            )
            result = abs(total - expected_total) < 0.01
            self.test_utils.yakshaAssert("test_large_order_processing", result, "boundary")
            print("test_large_order_processing = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_large_order_processing", False, "boundary")
            print("test_large_order_processing = Failed")

    def test_minimum_order_processing(self):
        """Test processing an order with minimum allowed items (one item)"""
        try:
            total = self.restaurant.add_order("Alice", ["Salad"])
            expected = 8.99  # Price of salad (no discount as it's not a daily special)
            result = abs(total - expected) < 0.01
            self.test_utils.yakshaAssert("test_minimum_order_processing", result, "boundary")
            print("test_minimum_order_processing = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_minimum_order_processing", False, "boundary")
            print("test_minimum_order_processing = Failed")

if __name__ == '__main__':
    unittest.main()
