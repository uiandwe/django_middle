__author__ = 'uiandwe'


class SimpleMiddleware(object):
    def __init__(self):
        pass
        # One-time configuration and initialization.

    def process_request(self, request):
        return

    def process_view(self, request, view_func, view_args, view_kwargs):

        print(request, view_args, view_func, view_kwargs)

        respose = None
        return respose


    def process_template_response(self, request, response):
        print(request, response)
        return response


    def process_response(self, request, response):
        print(request, response)
        return response