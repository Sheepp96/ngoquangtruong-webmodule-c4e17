from flask import Flask, render_template
from mongoengine import *
from models.customer import Customer
import mlab

app = Flask(__name__)

mlab.connect()

@app.route('/customer')
def customer():
    all_customer = Customer.objects[:10](gender = 1, contacted = False)
    return render_template('customer.html', all_customer = all_customer)

@app.route('/')
def index():
    return render_template('index1.html')

if __name__ == '__main__':
  app.run(debug=True)
