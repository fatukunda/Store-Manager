from flask import jsonify
# Shared methods
def search(search_item, collection):
    search_list = []
    for item in collection:
        [search_list.append(item) for key in item if item[key] == search_item]
    return jsonify(search_list)


def get_collection(collection):
    if len(collection) > 0:
        return jsonify(collection)