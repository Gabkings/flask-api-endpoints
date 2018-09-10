from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

users = [
    { "id": 1,"name": "Masnun", "email": "masnun@gmail.com"},
    { "id": 2,"name": "Joseph", "email": "joseph@gmail.com"}
    { "id": 1,"name": "Gabriel", "email": "gabriel@gmail.com"}
    { "id": 1,"name": "Gitonga", "email": "gitonga@gmail.com"}
    { "id": 1,"name": "Melvin", "email": "melvin@gmail.com"}
]


class CustomerCollection(Resource):
    def get(self):
        return {"msg": "All Customers "}

    def post(self):
        return {"msg": "We will create new Customers here"}


class Customer(Resource):
    def get(self, id):
        return {"msg": "Details about user id {}".format(id)}

    def put(self, id):
        return {"msg": "Update user id {}".format(id)}

    def delete(self, id):
        return {"msg": "Delete user id {}".format(id)}


api.add_resource(CustomerCollection, '/Customers')
api.add_resource(Customer, '/Customers/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
