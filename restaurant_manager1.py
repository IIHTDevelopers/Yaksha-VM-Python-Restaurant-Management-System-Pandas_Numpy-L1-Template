import numpy as np
import pandas as pd
import os


# Section 1: Python Basics - Data Types, Operators, Control Flow
class RestaurantManager:
    def __init__(self, name):
        self.name = name
        self.menu = {
            "Pizza": 12.99,
            "Burger": 9.99,
            "Pasta": 10.99,
            "Salad": 7.99,
            "Chicken Fried Rice": 13.99  # New Non-Veg Item
        }
        self.orders = []

        # Dictionary to track non-veg items
        self.non_veg_items = {
            "Chicken Fried Rice": True
        }

    # Section 2: Functions, Modules, Packages
    def display_menu(self):
        print(f"\n{self.name} Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def take_order(self, customer_name, order_items):
        total = 0
        for item in order_items:
            if item in self.menu:
                total += self.menu[item]
            else:
                print(f"{item} is not available in the menu.")

        order = {"Customer": customer_name, "Items": order_items, "Total": total}
        self.orders.append(order)
        print(f"Order for {customer_name} recorded. Total: ${total:.2f}")

    def view_orders(self):
        print("\nCurrent Orders:")
        for order in self.orders:
            print(order)

    # Section 3: Data Structures - Lists, Tuples, Dictionaries, Sets
    def available_items(self):
        return list(self.menu.keys())

    def add_item_to_menu(self, item, price, is_non_veg=False):
        if item in self.menu:
            print(f"{item} is already in the menu.")
        else:
            self.menu[item] = price
            if is_non_veg:
                self.non_veg_items[item] = True
            print(f"{item} added to the menu at ${price}")

    def get_non_veg_items(self):
        """Returns a list of all non-veg items in the menu."""
        non_veg_list = [item for item in self.menu if item in self.non_veg_items]
        print("\nNon-Veg Items:")
        for item in non_veg_list:
            print(f"{item}: ${self.menu[item]}")
        return non_veg_list

    # Section 4: File I/O, Exception Handling
    def save_orders_to_file(self, filename="orders.txt"):
        try:
            with open(filename, "w") as file:
                for order in self.orders:
                    file.write(str(order) + "\n")
            print(f"Orders saved to {filename}")
        except Exception as e:
            print(f"Error saving orders: {e}")

    def load_orders_from_file(self, filename="orders.txt"):
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    self.orders = [eval(line.strip()) for line in file]
                print("Orders loaded successfully.")
            else:
                print("No existing orders found.")
        except Exception as e:
            print(f"Error loading orders: {e}")

    # Section 5: Python for Data Science - NumPy, Pandas
    def analyze_orders(self):
        if not self.orders:
            print("No orders to analyze.")
            return None  # Explicitly return None if there are no orders

        df = pd.DataFrame(self.orders)
        print("\nOrder Summary:")
        print(df)

        # Using NumPy to calculate statistics
        total_revenue = np.sum(df["Total"].values)
        avg_order_value = np.mean(df["Total"].values)
        min_order_value = np.min(df["Total"].values)
        max_order_value = np.max(df["Total"].values)

        summary = {
            "Total Revenue": round(total_revenue, 2),
            "Average Order Value": round(avg_order_value, 2),
            "Min Order Value": round(min_order_value, 2),
            "Max Order Value": round(max_order_value, 2),
        }

        print(f"\nTotal Revenue: ${summary['Total Revenue']}")
        print(f"Average Order Value: ${summary['Average Order Value']}")
        print(f"Min Order Value: ${summary['Min Order Value']}")
        print(f"Max Order Value: ${summary['Max Order Value']}")

        return summary  # Return the dictionary instead of None

    def get_most_popular_item(self):
        """Finds and returns the most frequently ordered item."""
        if not self.orders:
            print("No orders placed yet.")
            return None

        item_count = {}
        for order in self.orders:
            for item in order["Items"]:
                item_count[item] = item_count.get(item, 0) + 1

        if item_count:
            most_popular = max(item_count, key=item_count.get)
            print(f"\nMost Popular Item: {most_popular} ({item_count[most_popular]} orders)")
            return most_popular
        else:
            print("No items ordered yet.")
            return None

    def get_top_spending_customer(self):
        """Finds and returns the customer who has spent the most."""
        if not self.orders:
            print("No orders have been placed yet.")
            return None

        customer_spending = {}
        for order in self.orders:
            customer = order["Customer"]
            customer_spending[customer] = customer_spending.get(customer, 0) + order["Total"]

        if customer_spending:
            top_customer = max(customer_spending, key=customer_spending.get)
            print(f"\nTop Spending Customer: {top_customer} (${customer_spending[top_customer]:.2f})")
            return top_customer
        else:
            print("No customers have spent anything yet.")
            return None


# Running the Restaurant Manager
if __name__ == "__main__":
    manager = RestaurantManager("Gourmet Hub")
    manager.display_menu()

    # Taking Orders
    manager.take_order("Alice", ["Pizza", "Salad"])
    manager.take_order("Bob", ["Burger", "Pasta", "Chicken Fried Rice"])
    manager.take_order("Charlie", ["Pizza", "Chicken Fried Rice", "Burger"])

    # Viewing Orders
    manager.view_orders()

    # Saving and Loading Orders
    manager.save_orders_to_file()
    manager.load_orders_from_file()

    # Analyzing Orders
    manager.analyze_orders()

    # Getting the most popular item
    manager.get_most_popular_item()

    # Getting the top spending customer
    manager.get_top_spending_customer()

    # Getting all non-veg items
    manager.get_non_veg_items()
