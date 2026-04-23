from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

##table of orders 
class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    
    customer_name = db.Column(db.String,nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    alteration_type = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(100))
    descriptions = db.Column(db.String(500))

    status = db.Column(db.String(50), default="pending")
    #measurements
    chest = db.Column(db.Float, nullable=False)
    waist = db.Column(db.Float, nullable=False)
    hips = db.Column(db.Float, nullable=False)
    inseam = db.Column(db.Float, nullable = False)
    
   
    def __repr__(self):
        return f"{self.order_id} - {self.customer_name} - {self.item}"



@app.route('/')
def index():
    return 'Order page'

#create order(customer submits form)
@app.route('/orders', methods=['POST'])
def add_order():
    order = Order(customer_name=request.json['customer_name'],phone=request.json['phone'],item=request.json['item'],alteration_type=request.json['alteration_type'],material=request.json.get('material'),descriptions=request.json.get('descriptions'),chest=request.json['chest'],waist=request.json['waist'],hips=request.json['hips'],inseam=request.json['inseam'])
    db.session.add(order)
    db.session.commit()
    return {'Order submitted': order.order_id}


#get all orders
@app.route('/orders')
def get_orders():
    orders = Order.query.all()

    output = []
    for order in orders:
        order_data = {'id': order.order_id,'customer_name': order.customer_name,'phone': order.phone,'item': order.item,'alteration_type': order.alteration_type,'status':order.status}

        output.append(order_data)
    return {"orders": output}

#get one order by id
@app.route('/orders/<order_id>')
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return {'id': order.order_id,'customer_name': order.customer_name,'phone': order.phone,'item': order.item,'alteration_type': order.alteration_type,'status':order.status}


#deletes order by id
@app.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        return {"error": "not found"}
    db.session.delete(order)
    db.session.commit


# ACCEPT order
@app.route('/orders/<int:order_id>/accept', methods=['PUT'])
def accept_order(order_id):
    order = Order.query.get_or_404(order_id)

    order.status = "accepted"
    db.session.commit()

    return {"message": "Order accepted"}


# DENY order
@app.route('/orders/<int:order_id>/deny', methods=['PUT'])
def deny_order(order_id):
    order = Order.query.get_or_404(order_id)

    order.status = "denied"
    db.session.commit()

    return {"message": "Order denied"}


# UPDATE status (progress updates)
@app.route('/orders/<int:order_id>/status', methods=['PUT'])
def update_status(order_id):
    order = Order.query.get_or_404(order_id)

    new_status = request.json.get('status')
    order.status = new_status

    db.session.commit()

    return {"message": "Status updated"}


