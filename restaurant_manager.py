import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Set
import json
from datetime import datetime

class RestaurantManager:
    def __init__(self):
        # Data Types Demo - Using different Python data types
        self.restaurant_name: str = "Python Bites"
        self.is_open: bool = True
        self.rating: float = 4.5
        self.total_orders: int = 0
        
        # Data Structures Demo
        self.menu: Dict[str, float] = {
            "Burger": 10.99,
            "Pizza": 12.99,
            "Salad": 8.99,
            "Pasta": 11.99,
            "Ice Cream": 5.99
        }
        
        self.orders: List[Dict] = []
        self.vip_customers: Set[str] = set()
        self.daily_specials: Tuple[str] = ("Burger", "Pizza")
        
    def add_order(self, customer_name: str, items: List[str]) -> float:
        """
        Function to add a new order
        Demonstrates: Functions, Exception Handling, Operators
        """
        try:
            if not items:
                raise ValueError("Order cannot be empty")
            
            # Control Flow Demo
            total = 0.0
            order_items = []
            
            for item in items:
                if item not in self.menu:
                    raise KeyError(f"Item not found in menu: {item}")
                
                price = self.menu[item]
                # Operators Demo
                if item in self.daily_specials:
                    price *= 0.9  # 10% discount
                
                total += price
                order_items.append({"item": item, "price": price})
            
            # Create order object
            order = {
                "order_id": self.total_orders + 1,
                "customer": customer_name,
                "items": order_items,
                "total": total,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.orders.append(order)
            self.total_orders += 1
            
            # File I/O Demo
            self._save_order_to_file(order)
            
            return total
            
        except Exception as e:
            raise Exception(f"Error processing order: {str(e)}")
    
    def _save_order_to_file(self, order: Dict) -> None:
        """
        Private method to save order to file
        Demonstrates: File I/O
        """
        try:
            with open("orders.json", "a") as f:
                json.dump(order, f)
                f.write("\n")
        except IOError as e:
            raise IOError(f"Error saving order to file: {str(e)}")
    
    def get_sales_analysis(self) -> pd.DataFrame:
        """
        Method to analyze sales using Pandas
        Demonstrates: Pandas usage
        """
        try:
            # Convert orders to DataFrame
            orders_df = pd.DataFrame(self.orders)
            
            # Explode the items column to get individual items
            items_df = orders_df.explode('items')
            
            # Convert items dictionary to separate columns
            items_df = pd.concat([
                items_df.drop(['items'], axis=1),
                pd.json_normalize(items_df['items'])
            ], axis=1)
            
            return items_df
            
        except Exception as e:
            raise Exception(f"Error analyzing sales: {str(e)}")
    
    def get_daily_revenue_stats(self) -> Dict:
        """
        Method to get daily revenue statistics using NumPy
        Demonstrates: NumPy usage
        """
        try:
            daily_revenues = [order['total'] for order in self.orders]
            
            if not daily_revenues:
                return {
                    "total": 0,
                    "average": 0,
                    "min": 0,
                    "max": 0
                }
            
            # Using NumPy for calculations
            revenue_array = np.array(daily_revenues)
            
            return {
                "total": np.sum(revenue_array),
                "average": np.mean(revenue_array),
                "min": np.min(revenue_array),
                "max": np.max(revenue_array)
            }
            
        except Exception as e:
            raise Exception(f"Error calculating revenue stats: {str(e)}")
    
    def validate_customer(self, customer_name: str) -> bool:
        """
        Method to validate customer name
        Demonstrates: String operations, Control Flow
        """
        if not isinstance(customer_name, str):
            raise TypeError("Customer name must be a string")
        
        if len(customer_name.strip()) == 0:
            raise ValueError("Customer name cannot be empty")
        
        return True
