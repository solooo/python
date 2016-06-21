# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web</h1>']

from wsgiref.simple_server import make_server
httpd = make_server('', 8000, application)
print('serving HTTP on port 8000...')
httpd.serve_forever()

                
