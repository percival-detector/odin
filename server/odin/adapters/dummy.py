import logging
from odin.adapters.adapter import ApiAdapter, ApiAdapterResponse, request_types, response_types

class DummyAdapter(ApiAdapter):

    def __init__(self):

        super(DummyAdapter, self).__init__()
        logging.debug('DummyAdapter loaded')

    def get(self, path, request):

        response = 'DummyAdapter: GET on path {}'.format(path)
        status_code = 200

        logging.debug(response)

        return ApiAdapterResponse(response, status_code=status_code)

    @request_types('application/json')
    @response_types('application/json', default='application/json')
    def put(self, path, request):

        response = 'DummyAdapter: PUT on path {}'.format(path)
        status_code = 200

        logging.debug(response)

        return ApiAdapterResponse(response, status_code=status_code)

    def delete(self, path, request):

        response = 'DummyAdapter: DELETE on path {}'.format(path)
        status_code = 200

        logging.debug(response)

        return ApiAdapterResponse(response, status_code=status_code)
