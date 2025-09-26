from flask import Flask, jsonify, request
from http import HTTPStatus

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

if __name__ == "__main__":
    app.run(debug=True)