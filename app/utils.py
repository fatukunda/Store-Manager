from flask import jsonify
# Shared methods
""" Search for a product or sale given an id"""
def search(search_item, collection):
    search_list = []
    for item in collection:
        [search_list.append(item) for key in item if item[key] == search_item]
    return jsonify(search_list)

""" Get a collection of products or sales"""
def get_collection(collection):
    return jsonify(collection)

