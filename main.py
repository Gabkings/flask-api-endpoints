from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

users = [
    {"id": 1, "name": "Masnun","email": "masnun@gmail.com"},
    {"id": 2, "name": "Gitonga","email": "gitonga@gmail.com"},
    {"id": 3, "name": "Gabriel","email": "gabriel@gmail.com"}
]

orders = [
    {"id":1,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":2,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":3,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":4,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":5,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":6,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"}
]


def get_user_by_id(user_id):
    for user in users:
        if user.get("id") == int(user_id):
            return user

def get_order_by_id(order_id):
    for order in orders:
        if order.get("id") == int(order_id):
            return order


subscriber_request_parser = RequestParser(bundle_errors=True)
order_request_parser = RequestParser(bundle_errors= True)
#users validation stars here
subscriber_request_parser.add_argument("name", type=str, required=True, help="Name has to be valid string")
subscriber_request_parser.add_argument("email", required=True)
subscriber_request_parser.add_argument("id", type=int, required=True, help="Please enter valid integer as ID")
#orders validation starts here 
order_request_parser.add_argument("name", type=str, required=True, help="Name has to be valid string")
order_request_parser.add_argument("status", type=str, required=True, help="Name has to be valid string")
order_request_parser.add_argument("id", type=int, required=True, help="Please enter valid integer as ID")
order_request_parser.add_argument("cost", type=int, required=True, help="Please enter valid integer as ID")
order_request_parser.add_argument("No of items ordered", type=int, required=True, help="Please enter valid integer as ID")


customer_request_parser = RequestParser(bundle_errors=True)
customer_request_parser.add_argument(
    "name", type=str, required=True, help="Name has to be valid string")
customer_request_parser.add_argument("email", required=True)
customer_request_parser.add_argument(
    "id", type=int, required=True, help="Please enter valid integer as ID")
#class to get all the customer orders and place a new order
class OrderCollection(Resource):
    def get(self):
        return orders

    def post(self):
        args = order_request_parser.parse_args()
        orders.append(args)
        return {"msg": "Order was added successfully", "order_data": args} 
#Class to enable access of indivial orders
class Order(Resource):
    def get(self, id):
        order = get_order_by_id(id)
        if not order:
            return {"error": "Order not found"}

        return order 

    def put(self, id):
        args = customer_request_parser.parse_args()
        Order = get_order_by_id(id)
        if Order:
            orders.remove(user)
            orders.append(args)

        return args


class CustomerCollection(Resource):
    def get(self):
        return users

    def post(self):
        args = customer_request_parser.parse_args()
        users.append(args)
        return {"msg": "Subscriber added", "subscriber_data": args}


class Customer(Resource):
    def get(self, id):
        user = get_user_by_id(id)
        if not user:
            return {"error": "User not found"}

        return user

    def put(self, id):
        args = customer_request_parser.parse_args()
        user = get_user_by_id(id)
        if user:
            users.remove(user)
            users.append(args)

        return args

    def delete(self, id):
        user = get_user_by_id(id)
        if user:
            users.remove(user)

        return {"message": "Deleted"}


api.add_resource(CustomerCollection, '/users')
api.add_resource(Customer, '/users/<int:id>')
api.add_resource(OrderCollection, '/orders')
api.add_resource(Order, '/orders/<int:id>')

if __name__ == '__main__':
    app.run()
