from flask import Flask, jsonify, request
from http import HTTPStatus


# -------- Session #1 --------
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask framework!"


# http://127.0.0.1:5000/cohort-60
@app.route("/cohort-60", methods=["GET"])
def hello_world():
    print("Cohort 60 endpoint accessed")
    return "Hello Cohort#60"


# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
    information = {"email": "mkratz@sdgku.edu", "phone": "702-370-4492"}
    return information


@app.route("/course", methods=["GET"])
def course_information():
    return {
        "title": "Introductory Web API Flask",
        "duration": "4 sessions",
        "level": "Beginner"
    }


@app.route("/user", methods=["GET"])
def user_information():
    return {
        "name": "Michael",
        "role": "full stack developer",
        "is_active": True,
        "favorite_technologies": ["Python", "React", "Node.js"]
    }


student_names = ["Reggie", "Tim", "Michael", "Zane", "Jake", "Jose"]

@app.route("/student", methods=["GET"])
def get_students():
    print("Students endpoint accessed")
    return student_names


@app.route("/student", methods=["POST"])
def add_student():
    student_names.append("Leo")
    return student_names


# -------- Assignment #1 --------


products = [
  {"id": 1, "name": "Cake", "price": 25},
  {"id": 2, "name": "Ice-cream", "price": 5},
  {"id": 3, "name": "Cookie", "price": 3},
  {"id": 4, "name": "Chocolate", "price": 10}
]


@app.route("/api/products", methods={"GET"})
def get_products():
    return products


@app.route("/api/products/count")
def products_count():
    count = len(products)
    return count


# -------- Assignment #2 --------
@app.route("/api/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    print(new_product)
    products.append(new_product)
    return jsonify(new_product), HTTPStatus.CREATED


@app.route("/api/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), HTTPStatus.OK
        print(f"product: {product}")
    return jsonify({"message": "Product not found"}), HTTPStatus.NOT_FOUND


@app.route("/api/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    for index, product in enumerate(products):
        if product["id"] == id:
            products.pop(index)
            return jsonify({"message": "Product deleted successfully"}), HTTPStatus.NO_CONTENT #204
    return "testing"

# -------- Session #2 --------
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "FALL25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

# Read all coupons

@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return jsonify(coupons), HTTPStatus.OK


# CREATE, add a new coupon
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    print(new_coupon)
    coupons.append(new_coupon)
    return jsonify(new_coupon), HTTPStatus.CREATED


# Path parameter
@app.route("/great/<string:name>", methods=["GET"])
def great(name):
    return f"hello {name}", HTTPStatus.OK


# GET - get a coupon by id
@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify(coupon), HTTPStatus.OK
        print(f"coupon: {coupon}")
    return jsonify({"message": "Coupon not found"}), HTTPStatus.NOT_FOUND


# UPDATE -

# DELETE - delete a coupon
@app.route("/api/coupons/<int:id>", methods=["DELETE"])
def delete_coupon(id):
    for index, coupon in enumerate(coupons):
        if coupon["_id"] == id:
            coupons.pop(index)
            return jsonify({"message": "Coupon deleted successfully"}), HTTPStatus.NO_CONTENT #204
    return "testing"


if __name__ == "__main__":
    app.run(debug=True)