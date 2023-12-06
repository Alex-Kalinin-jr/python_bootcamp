from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

def application(environ, start_response):

    MAP = {
        'Unit A': 'lvl 1', 'Unit B': 'lvl 2',
        'Unit C': 'lvl 3', 'Unit D': 'lvl 3',
        'Unit E': 'lvl 3', 'Unit F': 'lvl 3',
        'Unit G': 'lvl 4', 'Unit H': 'lvl 4',
        'Unit I': 'lvl 4', 'Unit J': 'lvl 4',
        'Unit K': 'lvl 5'
    }

    STATUSES = {
        '200': '200 OK',
        '404': '404 Not Found',
        '405': '405 Method Not Allowed'
    }

    request_method = environ['REQUEST_METHOD']
    request_body = parse_qs(environ['QUERY_STRING'])


    if request_method == 'GET':
        if 'species' in request_body and request_body['species'][0] in MAP:
            status = STATUSES['200']
            response_body = f"'credentials': {MAP[request_body['species'][0]]}"
        else:
            status = STATUSES['404']
            response_body = f"'{request_body['species'][0]}': not found"
    else:
        status = STATUSES['405']
        response_body: str = f'{request_method}: Method Not Allowed'

    content_length = len(response_body)

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(content_length))
    ]

    start_response(status, response_headers)

    return [response_body.encode('utf-8')]

httpd = make_server('localhost', 8888, application)
httpd.serve_forever()
