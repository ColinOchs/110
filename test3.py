from mock_data import catalog
import json
from flask import Flask, abort

app = Flask("Server")

@app.route("/api/catalog", methods=["get"])
def get_catalog():
    return json.dumps(catalog)

def lower_than(price):
    pass
    # print how many product exist 
    # with a price lower that price var
 


def greater_than(price):
    pass




lower_than(10)
pass
        
lower_than(30)
pass
lower_than(50)
pass
lower_than(100)
pass

greater_than(10)
pass
greater_than(30)
pass
greater_than(50)
pass
greater_than(100)
pass

app.run(debug=True)