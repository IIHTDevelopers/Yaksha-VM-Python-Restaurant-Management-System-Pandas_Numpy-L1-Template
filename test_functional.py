import unittest
from template import *
from TestUtils import TestUtils

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        self.restaurant = RestaurantManager()
        self.test_utils = TestUtils()

    def test_add_valid_order(self):
        """Test adding a valid order with discount"""
        try:
            total = self.restaurant.add_order("John", ["Burger", "Pizza"])
            expected = 21.58  # (10.99 + 12.99) * 0.9 (discount)
            result = abs(total - expected) < 0.01
            self.test_utils.yakshaAssert("test_add_valid_order", result, "functional")
            print("test_add_valid_order = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_add_valid_order", False, "functional")
            print("test_add_valid_order = Failed")

    def test_menu_items_count(self):
        """Test correct number of menu items"""
        try:
            result = len(self.restaurant.menu) == 5
            self.test_utils.yakshaAssert("test_menu_items_count", result, "functional")
            print("test_menu_items_count = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_menu_items_count", False, "functional")
            print("test_menu_items_count = Failed")

    def test_daily_specials_discount(self):
        """Test daily specials discount calculation"""
        try:
            total = self.restaurant.add_order("Alice", ["Burger"])
            expected = 9.89  # 10.99 * 0.9
            result = abs(total - expected) < 0.01
            self.test_utils.yakshaAssert("test_daily_specials_discount", result, "functional")
            print("test_daily_specials_discount = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_daily_specials_discount", False, "functional")
            print("test_daily_specials_discount = Failed")

    def test_order_count_increment(self):
        """Test order counter incrementation"""
        try:
            initial_count = self.restaurant.total_orders
            self.restaurant.add_order("Bob", ["Salad"])
            result = self.restaurant.total_orders == initial_count + 1
            self.test_utils.yakshaAssert("test_order_count_increment", result, "functional")
            print("test_order_count_increment = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_order_count_increment", False, "functional")
            print("test_order_count_increment = Failed")

    def test_validate_customer_name(self):
        """Test customer name validation"""
        try:
            result = self.restaurant.validate_customer("Charlie")
            self.test_utils.yakshaAssert("test_validate_customer_name", result, "functional")
            print("test_validate_customer_name = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_validate_customer_name", False, "functional")
            print("test_validate_customer_name = Failed")

    def test_revenue_stats_empty(self):
        """Test revenue stats with no orders"""
        try:
            stats = self.restaurant.get_daily_revenue_stats()
            result = all(v == 0 for v in stats.values())
            self.test_utils.yakshaAssert("test_revenue_stats_empty", result, "functional")
            print("test_revenue_stats_empty = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_revenue_stats_empty", False, "functional")
            print("test_revenue_stats_empty = Failed")

    def test_sales_analysis_structure(self):
        """Test sales analysis DataFrame structure"""
        try:
            self.restaurant.add_order("David", ["Pizza"])
            df = self.restaurant.get_sales_analysis()
            result = all(col in df.columns for col in ['order_id', 'customer', 'item', 'price'])
            self.test_utils.yakshaAssert("test_sales_analysis_structure", result, "functional")
            print("test_sales_analysis_structure = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_sales_analysis_structure", False, "functional")
            print("test_sales_analysis_structure = Failed")

if __name__ == '__main__':
    unittest.main()
