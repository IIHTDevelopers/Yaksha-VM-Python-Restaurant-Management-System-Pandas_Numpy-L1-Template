import sys
import unittest
import os

# Adjusting the import path for TestUtils and RestaurantManager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from restaurant_manager1 import *


class TestRestaurantManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = RestaurantManager("Gourmet Hub")
        cls.test_obj = TestUtils()

    def setUp(self):
        """Reset the manager state before each test."""
        self.manager.orders = []

    def test_menu_item_count(self):
        """Test if the menu has the correct number of items."""
        try:
            expected_count = 5
            actual_count = len(self.manager.menu)
            self.assertEqual(actual_count, expected_count)
            self.test_obj.yakshaAssert("test_menu_item_count", True, "functional")
            print("test_menu_item_count = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_menu_item_count", False, "exception")
            print("test_menu_item_count = Failed due to Exception:", str(e))

    def test_order_recording(self):
        """Test order recording functionality."""
        try:
            self.manager.take_order("Alice", ["Pizza", "Salad"])
            self.manager.take_order("Bob", ["Burger", "Pasta", "Chicken Fried Rice"])
            self.manager.take_order("Charlie", ["Pizza", "Chicken Fried Rice", "Burger"])

            expected_count = 3  # Ensuring only these 3 orders are present
            actual_count = len(self.manager.orders)
            self.assertEqual(actual_count, expected_count)

            self.test_obj.yakshaAssert("test_order_recording", True, "functional")
            print("test_order_recording = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_order_recording", False, "exception")
            print("test_order_recording = Failed due to Exception:", str(e))

    def test_order_saving_loading(self):
        """Test if orders are saved and loaded correctly."""
        try:
            self.manager.take_order("Alice", ["Pizza", "Salad"])
            self.manager.save_orders_to_file("orders.txt")

            # Clear orders before loading
            self.manager.orders = []
            self.manager.load_orders_from_file("orders.txt")

            self.assertEqual(len(self.manager.orders), 1)
            self.assertEqual(self.manager.orders[0]['Customer'], "Alice")

            self.test_obj.yakshaAssert("test_order_saving_loading", True, "functional")
            print("test_order_saving_loading = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_order_saving_loading", False, "exception")
            print("test_order_saving_loading = Failed due to Exception:", str(e))

    def test_order_summary(self):
        """Test calculation of order statistics."""
        try:
            self.manager.take_order("Alice", ["Pizza", "Salad"])
            self.manager.take_order("Bob", ["Burger", "Pasta", "Chicken Fried Rice"])
            self.manager.take_order("Charlie", ["Pizza", "Chicken Fried Rice", "Burger"])

            summary = self.manager.analyze_orders()
            self.assertIsNotNone(summary, "analyze_orders() should return a summary")

            self.test_obj.yakshaAssert("test_order_summary", True, "functional")
            print("test_order_summary = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_order_summary", False, "exception")
            print("test_order_summary = Failed due to Exception:", str(e))

    def test_most_popular_item(self):
        """Test if the most popular item is correctly identified."""
        try:
            self.manager.take_order("Alice", ["Pizza", "Salad"])
            self.manager.take_order("Bob", ["Burger", "Pasta", "Chicken Fried Rice"])
            self.manager.take_order("Charlie", ["Pizza", "Chicken Fried Rice", "Burger"])

            popular_item = self.manager.get_most_popular_item()
            expected_item = "Pizza"  # Pizza is ordered twice

            self.assertEqual(popular_item, expected_item)

            self.test_obj.yakshaAssert("test_most_popular_item", True, "functional")
            print("test_most_popular_item = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_most_popular_item", False, "exception")
            print("test_most_popular_item = Failed due to Exception:", str(e))

    def test_top_spending_customer(self):
        """Test if the top spending customer is correctly identified."""
        try:
            self.manager.take_order("Alice", ["Pizza", "Salad"])
            self.manager.take_order("Bob", ["Burger", "Pasta", "Chicken Fried Rice"])
            self.manager.take_order("Charlie", ["Pizza", "Chicken Fried Rice", "Burger"])

            top_customer = self.manager.get_top_spending_customer()
            expected_customer = "Charlie"  # Charlie spent the most ($36.97)

            self.assertEqual(top_customer, expected_customer)

            self.test_obj.yakshaAssert("test_top_spending_customer", True, "functional")
            print("test_top_spending_customer = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_top_spending_customer", False, "exception")
            print("test_top_spending_customer = Failed due to Exception:", str(e))

    def test_get_non_veg_items(self):
        """Test that only non-veg items are returned."""
        try:
            # Reset menu and add test items
            expected_non_veg =["Chicken Fried Rice"]
            actual_non_veg = self.manager.get_non_veg_items()

            self.assertEqual(sorted(actual_non_veg), sorted(expected_non_veg))

            self.test_obj.yakshaAssert("test_get_non_veg_items", True, "functional")
            print("test_get_non_veg_items = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_get_non_veg_items", False, "exception")
            print("test_get_non_veg_items = Failed due to Exception:", str(e))

if __name__ == '__main__':
    unittest.main(verbosity=2)
