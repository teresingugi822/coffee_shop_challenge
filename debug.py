from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 4.5)
c1.create_order(coffee2, 5.0)
c2.create_order(coffee1, 6.0)

html_content = f"""
<html>
<head><title>Coffee Shop Debug</title></head>
<body>
<h1>Customer & Order Summary</h1>
<ul>
    <li>{c1.name} ordered {[coffee.name for coffee in c1.coffees()]}</li>
    <li>{c2.name} ordered {[coffee.name for coffee in c2.coffees()]}</li>
</ul>

<h2>Latte Stats</h2>
<ul>
    <li>Number of Orders: {coffee1.num_orders()}</li>
    <li>Average Price: {coffee1.average_price()}</li>
    <li>Customers: {[cust.name for cust in coffee1.customers()]}</li>
</ul>
</body>
</html>
"""

with open("report.html", "w") as file:
    file.write(html_content)

print("Open 'report.html' in your browser to view the report.")
