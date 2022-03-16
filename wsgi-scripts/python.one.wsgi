class ReverseWare:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response, *args, **kwargs):
        wrapped_app_response = self.wrapped_app(environ, start_response)
        return [data[::-1] for data in wrapped_app_response]
"""
class Application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        body = b'Hello world!\n'
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        self.start_response(status, headers)
        yield body

#application = Application
application = ReverseWare(Application)
"""

class Application(object):
    def __call__(self, environ, start_response):
        status = '200 OK'
        output = b'Hello No World!'

        response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        return [output]

#application = Application()
application = ReverseWare(Application())
"""
def application(environ, start_response):
    status = '200 OK'
    output = b'Simplest way'

    response_headers = [('Content-type', 'text/plain'),
                    ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
"""