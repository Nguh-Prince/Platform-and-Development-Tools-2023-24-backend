import json

def parse_request_data(request):
    data = request.data.decode()

    return json.loads(data)

def parse_response_data(data):
    """
    Convert model instance to appropriate data type for the response
    """
    dictionary = None

    if isinstance(data, dict):
        dictionary = data
    else:
        dictionary = data.toJSON()

    return json.dumps(dictionary)