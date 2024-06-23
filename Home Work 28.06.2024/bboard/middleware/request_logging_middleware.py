
import logging

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(filename='requests.log', level=logging.DEBUG) 

    def __call__(self, request):
        logging.debug(f'Method: {request.method}')
        logging.debug(f'Path: {request.path}')
        logging.debug(f'GET params: {request.GET}')
        logging.debug(f'POST params: {request.POST}')
        logging.debug(f'User: {request.user}')

        response = self.get_response(request)
        return response
