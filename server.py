import json
from math import prod
from flask import Flask, abort, request
from mock_data import catalog
from config import db
from bson import ObjectId
from flask_cors import CORS

app = Flask("Server")
CORS(app) 

@app.route("/")
def home():
    return "Greetings, welcome to the website "

@app.route("/me")
def about_me():
    return "Colin Ochs"

###################################################################
#################      API Endpoints      #########################
######################   Return JSON  ############################
###################################################################



@app.route("/api/catalog", methods=["get"])
def get_catalog():
    
    products = []
    cursor = db.products.find({}) #cursor is a collection

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        products.append(prod)

    return json.dumps(products)

@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json() #return data (payload) from request
    
    db.products.insert_one(product)
    print(product)

    #fix _id
    product["_id"] = str(product["_id"])
 
    # crash
    return json.dumps(product)

# GET /api/catalog/count  ->  how many products exist in the catalog

@app.route("/api/catalog/count")
def product_count():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count += 1

     # cnt = len(list(cursor))

    return json.dumps(count)

# /api/catalog/total  ->  total of products in the catalog

@app.route("/api/catalog/total")
def total_of_catalog():
    
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total += prod["price"] 

    return json.dumps(total)

# get /api/product/wasdfalglkj3456g


@app.route("/api/product/<id>")
def get_by_id(id):
    #find the product with _id is equal to id
    
    prod = db.products.find_one({ "_id": ObjectId(id) })
   
    if not prod:
          ## if not found return 404 
     return abort(404, "no such product can be located")

    prod["_id"] = str(prod["_id"])
    return json.dumps(prod)
      
  



# Get /api/product/cheapest
# should return product with lowest price
# if the price of your prod is lower than the price of your solution variable
#     set your solutions variable equal to your prod

# return solution

@app.route("/api/product/cheapest")
def cheapest_product():
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]: 
            solution=prod
    return json.dumps(solution)


#create a variable(solution) with on of the elements from the list
# create a for loop to travel catalog
@app.get("/api/categories")
def unique_categories():
    categories = []
    for prod in catalog:
        category = prod["category"]
        if not category in categories:
            categories.append(category)
    return json.dumps(categories)


# Ticket 2345
# Create and endpoint that allow the client to get all the products
# for an specified category 
#\
@app.get("/api/catalog/<category>")
def prods_by_category(category):
  
    products = []
    cursor = db.products.find({"category" : category})
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        products.append(prod)

    return json.dumps(products)


@app.route("/api/someNumbers", methods=["get"])
def some_numbers():
    #return a list of random nums from 1 to 50
    numbers = []
    
    for num in range(0,51,5):
        #(start,stop,increments)
    
        numbers.append(num)
    return json.dumps(numbers)

##########################################
############# GET COUPON CODE ENDPOINTS #####
##########################################
#1-get all coupons
#2-save coupons
#3-get a coupon by code


allCoupons = []

@app.route("/api/couponCode", methods = ["GET"])
def get_coupons():

    coupons = []
    cursor = db.couponCodes.find({}) #cursor is a collection
    for code in cursor:
        code["_id"] = str(code["_id"])
        coupons.append(code)

    return json.dumps(coupons)



@app.route("/api/couponCode", methods=["POST"])

def save_coupon():
  coupon = request.get_json()

#must contain code, discount
#code should have at least 5 chars
#discount should not be lower 5 than and not greater than 50
  if not "code" in coupon or not "discount" in coupon:
      return abort(400, "no siree bob, must have code and discount")
  
  if len(coupon["code"]) < 5:
      return abort(400, "coupon must contain minimum character set")
  
  if (coupon["discount"]) < 5 or (coupon["discount"]) > 50:
      return abort(400, "nice try sneaky sneakerson...")

  db.couponCodes.insert_one(coupon)

  coupon["_id"] = str(coupon["_id"])
  
  return json.dumps(coupon)
  
@app.route("/api/couponCode/<code>")
def get_coupon_by_code(code):
  
    coupon = db.couponCodes.find_one({"code": code})
    if not coupon:

        return abort(404, "Invalid Code, Try again...")

    coupon["_id"] = str(coupon["_id"])
   
    return json.dumps(coupon)


##########################################
############# USER ENDPOINTS #####
##########################################

allUsers =[]

@app.route("/api/users", methods=["GET"])
def get_users():

    all_users = []
    cursor = db.users.find({})
    for user in cursor:
        user["_id"] = str(user["_id"])
        all_users.append(user)

    return json.dumps(all_users)

@app.route("/api/users", methods=["POST"])

def save_user():
  user = request.get_json()

  if not "username" in user or not "password" in user or not "email" in user:
      return abort(400, "Object must contain username, email and password")

    #check that the values are not empty
  if len(user["username"]) < 1 or len(user["password"]) < 1 or len(user["email"]) <1:
      return abort(400, "nope, try again... must contain all values...")

  db.users.insert_one(user)
  
  user["_id"] = str(user["_id"])
  return json.dumps(user)


@app.route("/api/users/<email>")
def find_user_by_email(email):
  
    user = db.users.find_one({"email": email})
    if not user:

        return abort(404, "Invalid User Email, Try again...")

    user["_id"] = str(user["_id"])
   
    return json.dumps(user)


@app.route("/api/login", methods=["POST"])
def validate_user_data():
    data = request.get_json()  #  <----dict with user and password
 
    #if no user in data, return a 400 error
    if not "user" in data:
        return abort(400, "user is required for login")
    if not "password" in data:
        return abort(400, "password is required for login")    

    user = db.users.find_one({"username": data["user"], "password": data["password"]})
    if not user:
        abort(401, "Invalid Credentials")

    user["_id"] = str(user["_id"])
    user.pop("password") #remove the key and value from the dict
    return json.dumps(user)


app.run(debug=True)