from flask import jsonify, Response
# Shared methods
def search(search_item, collection):
    search_list = []
    for item in collection:
        [search_list.append(item) for key in item if item[key] == search_item]
    if not search_list:
        return Response('Item not found', status=404)
    else:
        return jsonify(search_list)

def get_collection(collection):
    if not collection:
        return Response('No such collection found', status=404)
    else:
        return jsonify(collection)
    # if len(collection) > 0:
    #     return jsonify(collection)

