import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Customer.all_customers.clear()
        Order.all_orders.clear()
        self.customer1 = Customer("Teresia")
        self.customer2 = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_name_getter(self):
        self.assertEqual(self.coffee.name, "Espresso")

    def test_immutable_name(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Cappuccino"

    def test_num_orders(self):
        self.customer1.create_order(self.coffee, 4.5)
        self.customer2.create_order(self.coffee, 6.0)
        self.assertEqual(self.coffee.num_orders(), 2)

    def test_average_price(self):
        self.customer1.create_order(self.coffee, 4.0)
        self.customer2.create_order(self.coffee, 6.0)
        self.assertEqual(self.coffee.average_price(), 5.0)

    def test_customers_unique(self):
        self.customer1.create_order(self.coffee, 5.0)
        self.customer1.create_order(self.coffee, 6.0)
        customers = self.coffee.customers()
        self.assertEqual(len(customers), 1)
        self.assertIn(self.customer1, customers)

if __name__ == '__main__':
    unittest.main()
