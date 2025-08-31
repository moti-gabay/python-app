from flask import Response
import json

def json_response(data, status=200):
    json_str = json.dumps(data, ensure_ascii=False)
    return Response(json_str, content_type='application/json; charset=utf-8', status=status)
# utils/util.py

def mongo_doc_to_dict(doc):
    """ Convert a MongoDB document to a Python dict """
    result = {k: v for k, v in doc.items()}
    result['id'] = str(result.pop('_id')) if '_id' in result else None
    return result
