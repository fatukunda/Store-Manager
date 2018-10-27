from flask import jsonify
""" Shared methods"""

""" Search for an Item from a list given the id and the list"""
def search(search_item, collection):
    for item in collection:
        return [item for key in item if item[key] == search_item]
    
""" Delete a given item from a given list"""
def delete(item_to_delete, collection):
    item = search(item_to_delete, collection)
    collection.remove(item[0])
    return jsonify(item[0])

""" Edit a given Item"""
def edit(item_to_edit, collection, edited_item):
    item = search(item_to_edit, collection)
    item = item[0]
    for key in edited_item:
        if edited_item[key] != item[key]:
            item[key] == edited_item[key]
    return item
