import json

from flask import Flask, abort, request
from mock_data import catalog
from config import db
from bson import ObjectId


app = Flask("Server")


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
def catalog_total():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total+=prod["price"]
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
        cat = prod["category"]
        if not cat in categories:
            categories.append(cat)
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
#create the GET /api/couponCode

@app.route("/api/couponCode", methods = ["GET"])
def get_coupons():

    codes = []
    cursor = db.coupons.find({}) #cursor is a collection

    for code in cursor:
        code["_id"] = str(code["_id"])
        allCoupons.append(code)

    return json.dumps(allCoupons)


#create the POST  /api/couponCode
#get the coupon from the request and 
#adding an _id
#add it to all coupons
#return the coupon as json
#app.post("/api/couponCode") same as below

@app.route("/api/couponCode", methods=["POST"])

def save_coupon():
  coupon = request.get_json()
  db.coupon.insert_one(coupon)
  coupon["_id"] = str(coupon["_id"])

  return json.dumps(coupon)
  
@app.get("/api/couponCode/<code>")
def get_coupon_by_code(code):
  
    coupon = db.coupons.find_one({"code" : code})
    if not coupon:
        return abort(404, coupon code)
    coupon["_id"] = str(coupon["_id"])
   
    return json.dumps(coupon)


app.run(debug=True)