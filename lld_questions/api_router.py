import threading 
from flask import Flask,jsonify,request


app=Flask(__name__)
inventory={
    "product_1":{"nane":"sandeep","age":278},
    "product_2":{"nane":"ajay","age":6378},

}

lock=threading.Lock()
@app.route('/products/<product_id>',methods=["GET"])
def get_product(product_id):
    if product_id in inventory:
        return jsonify(inventory[product_id])
    return jsonify({"error":"product not fond"}),400


@app.route("/products/<product_id>/stocks",methods=["UPDATE"])
def update(product_id):
    data=request.get_json()
    quantity_change=data["change"]
    if product_id in inventory and isinstance(quantity_change):
        with lock:
            inventory[product_id]["age"]+=quantity_change
            return jsonify({"message":"successful"})
    else:
        return jsonify({"error":"product not found"}),400
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)  # Run on all interfaces, port 5001
