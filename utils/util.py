from flask import Response
import json

def json_response(data, status=200):
    json_str = json.dumps(data, ensure_ascii=False)
    return Response(json_str, content_type='application/json; charset=utf-8', status=status)
