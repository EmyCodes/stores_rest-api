#!/usr/bin/python3

from flask import Flask, request
from flask_smorest import abort
from uuid import uuid4
from db import stores, items

"""
This is my first API building Project
using Flask
"""
app = Flask(__name__)


@app.post("/store")
def create_store():
    """This endpoint POST new store with a unique id"""
    store_data = request.get_json()
    #Error handling
    if (
        "name" not in store_data
    ):
        abort(400, message="Bad Request! Ensure 'name', 'price',\
              'store_id' are in the JSON Payload")
        
    # Check if the key exists
    for store in stores.values():
        if (
            store_data["name"] == store ["name"] and
            store_data["store_id"] == store[store_id]
        ):
            abort(400, message="Store Already Exist")
    '''
    if store_data["store_id"] not in stores:
    # if store_data["store_id"] != stores[store_id]:    
        abort(400, message="Store Not Found")
    # Else: Update database with the Processed Logic'''
    store_id = uuid4().hex
    new_store = {**store_data, "id": store_id}
    # new_store = {**request_store, id}
    stores[store_id] = new_store
    return new_store, 201


@app.get("/store")
def get_all_stores():
    """This endpoint GET ALL stores"""
    return {"stores": list(stores.values())}



@app.get("/store/<string:store_id>")
def get_one_store(store_id):
    """This endpoint GET a specific store by store_id"""
    try:
        return stores[store_id]
    except KeyError:
        abort (400, Message="Store Not Found")

@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    store_data = request.get_json()
    try:
        del stores[store_id]
        return {"Message": "Store successfully Deleted"}
    except KeyError:
        abort(400, message="Store Not Found!")


@app.put("/store/<string:store_id>")
def update_store(store_id):
    store_data = request.get_json()
    try:
        stores[store_id] |= store_data
        return dict(stores[store_id])
    except KeyError:
        abort(400, message="Store Not Found!")

@app.post("/item")
def create_item():
    """This endpoint CREATE new store"""
    item_data = request.get_json()

    #Error handling
    if (
        "name" not in item_data or
        "price" not in item_data or
        "store_id" not in item_data
    ):
        abort(400, message="Bad Request! Ensure 'name', 'price',\
              'store_id' are in the JSON Payload")
        
    # Check if the key exists
    for item in items.values():
        if (
            item_data["name"] == item["name"] and
            item_data["store_id"] == item["store_id"]
        ):

            abort(400, message="Store Already Exist")
    
    if item_data["store_id"] not in stores:
    # if store_data["store_id"] != stores[store_id]:    
        abort(400, message="Store Not Found")
    # Else: Update database with the Processed Logic
    # if item_data[store_id] not in stores:
    #     return f"Message: {name} not found", 404
    item_id = uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201


@app.get("/item")
def get_all_items():
    """This endpoint GET ALL new items"""
    return {"items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_one_item(item_id):
    """This endpoint GET a specific item by item_id"""
    # if items["item_id"] not in items:
    try:
        return items[item_id]
    except KeyError:
        abort (400, Message="Item Not Found")


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    item_data = request.get_json()
    if (
        "name" not in item_data and
        "price" not in item_data
    ):
        abort(400, message="Bad Request. Ensure you include 'name' and 'price' in JSON Payload")
    try:
        del items[item_id]
        return {"Message": "Item deleted!"}
    except:
        abort(400, message="Item Not Found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if (
        "name" not in item_data or
        "price" not in item_data
    ):
        abort(400, message="Bad Request. Ensure you include 'name' and 'price' in JSON Payload")
    
    try:
        # items[item_id] = item_data
        items[item_id] |= item_data
        print({"Message": "Item Updated Successfully!"})
        return items[item_id]
    except KeyError:
        abort(400, message="Item Not Found!")