from mock_data import catalog
import json
from flask import Flask, abort

app = Flask("server")

def find_prod():
    text = "l"

    #step 1 - for loop and print titles
    count = 0
    for prod in catalog:
        title = prod["title"]
        # if title.find(text) >=0:   (same as below)
        if text.lower() in title.lower():  #<--case sensitive unless changed to lower/upper
            print(f"{title} ${prod['price']}")
   
def unique_categories():
    categories=["print_collections", "posters"]
    for prod in catalog:
        category = prod["category"]
    
    #if category does not exist in the list, push it
        if not category in categories:
            categories.append(category)
    
    print(categories)

def special_categ():
    results = []
    for prod in catalog:
        cat = prod["category"]
        if not cat in results:
            results.append(cat)
    print(results)

@app.get("/api/categories")
def inique_categories():
    categories = []
    for prod in catalog:
        cat = prod["category"]
        if not cat in categories:
            categories.append(cat)
    return json.dumps(categories)



find_prod()
unique_categories()
special_categ()