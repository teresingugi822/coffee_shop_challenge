import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Customer.all_customers.clear()
        Order.all_orders.clear()
        self.customer = Customer("Teresia")
        self.coffee = Coffee("Americano")
        self.order = Order(self.customer, self.coffee, 4.5)

    def test_order_customer_and_coffee(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.coffee, self.coffee)

    def test_order_price(self):
        self.assertEqual(self.order.price, 4.5)

    def test_invalid_price_too_low(self):
        with self.assertRaises(Exception):
            Order(self.customer, self.coffee, 0.5)

    def test_invalid_price_too_high(self):
        with self.assertRaises(Exception):
            Order(self.customer, self.coffee, 12.0)

    def test_invalid_customer(self):
        with self.assertRaises(Exception):
            Order("NotACustomer", self.coffee, 4.0)

    def test_invalid_coffee(self):
        with self.assertRaises(Exception):
            Order(self.customer, "NotACoffee", 4.0)

if __name__ == "__main__":
    unittest.main()
