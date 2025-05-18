from flask import Flask, render_template
from customer import Customer
from coffee import Coffee

app = Flask(__name__)

# Sample data
c1 = Customer("Teresia")
c2 = Customer("Alice")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# You can add orders as needed here

@app.route('/')
def index():
    # Send data to template
    customers = [c1, c2]
    coffees = [coffee1, coffee2]
    return render_template('index.html', customers=customers, coffees=coffees)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

