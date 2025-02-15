import unittest
import os
import pandas as pd
import numpy as np
from restaurant_manager import *
from test.TestUtils import TestUtils

import unittest
from restaurant_manager import RestaurantManager  # Assuming your class is in restaurant_manager.py



class TestRestaurantManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = RestaurantManager("Gourmet Hub")
        cls.test_obj = TestUtils()

    def test_menu_item_count(self):
        try:
            expected_count = 5
            actual_count = len(self.manager.menu)
            if actual_count == expected_count:
                self.test_obj.yakshaAssert("test_menu_item_count", True, "functional")
                print("test_menu_item_count = Passed")
            else:
                self.test_obj.yakshaAssert("test_menu_item_count", False, "functional")
                print("test_menu_item_count = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_menu_item_count", False, "exception")
            print("test_menu_item_count = Failed due to Exception", str(e))

    def test_current_order_count(self):
        try:
            self.manager.take_order("Alice", ["Pizza", "Salad"])
            self.manager.take_order("Bob", ["Burger", "Pasta", "Chicken Fried Rice"])
            self.manager.take_order("Charlie", ["Pizza", "Chicken Fried Rice", "Burger"])
            expected_count = 3
            actual_count = len(self.manager.orders)
            if actual_count == expected_count:
                self.test_obj.yakshaAssert("test_current_order_count", True, "functional")
                print("test_current_order_count = Passed")
            else:
                self.test_obj.yakshaAssert("test_current_order_count", False, "functional")
                print("test_current_order_count = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_current_order_count", False, "exception")
            print("test_current_order_count = Failed due to Exception", str(e))

    def test_top_spending_customer(self):
        try:
            expected_customer = "Charlie"
            actual_customer = self.manager.get_top_spending_customer()
            if actual_customer == expected_customer:
                self.test_obj.yakshaAssert("test_top_spending_customer", True, "functional")
                print("test_top_spending_customer = Passed")
            else:
                self.test_obj.yakshaAssert("test_top_spending_customer", False, "functional")
                print("test_top_spending_customer = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_top_spending_customer", False, "exception")
            print("test_top_spending_customer = Failed due to Exception", str(e))

    def test_total_revenue(self):
        try:
            expected_revenue = 92.92
            total_revenue = sum(order["Total"] for order in self.manager.orders)
            if round(total_revenue, 2) == expected_revenue:
                self.test_obj.yakshaAssert("test_total_revenue", True, "functional")
                print("test_total_revenue = Passed")
            else:
                self.test_obj.yakshaAssert("test_total_revenue", False, "functional")
                print("test_total_revenue = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_total_revenue", False, "exception")
            print("test_total_revenue = Failed due to Exception", str(e))

    def test_most_popular_item(self):
        try:
            expected_item = "Pizza"
            actual_item = self.manager.get_most_popular_item()
            if actual_item == expected_item:
                self.test_obj.yakshaAssert("test_most_popular_item", True, "functional")
                print("test_most_popular_item = Passed")
            else:
                self.test_obj.yakshaAssert("test_most_popular_item", False, "functional")
                print("test_most_popular_item = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_most_popular_item", False, "exception")
            print("test_most_popular_item = Failed due to Exception", str(e))

    def test_non_veg_items(self):
        try:
            expected_items = ["Chicken Fried Rice"]
            actual_items = self.manager.get_non_veg_items()
            if actual_items == expected_items:
                self.test_obj.yakshaAssert("test_non_veg_items", True, "functional")
                print("test_non_veg_items = Passed")
            else:
                self.test_obj.yakshaAssert("test_non_veg_items", False, "functional")
                print("test_non_veg_items = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_non_veg_items", False, "exception")
            print("test_non_veg_items = Failed due to Exception", str(e))




if __name__ == "__main__":
    unittest.main()
