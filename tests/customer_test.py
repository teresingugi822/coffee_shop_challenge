import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Customer.all_customers.clear()
        Order.all_orders.clear()
        self.customer = Customer("Teresia")
        self.coffee = Coffee("Latte")

    def test_name_getter(self):
        self.assertEqual(self.customer.name, "Teresia")

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

if __name__ == "__main__":
    unittest.main()
