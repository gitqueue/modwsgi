import os
import string

def application(environ, start_response):
    status = '200 OK'
    
    response_headers = [('Content-type', 'text/plain'),]
    start_response(status, response_headers)
    
    filelike = open('/tmp/filetest-a.txt', 'w+')
    filelike.write(string.ascii_lowercase)
    filelike.flush()
    filelike.seek(0, os.SEEK_SET)

    file_wrapper = environ['wsgi.file_wrapper'](filelike)

    filelike.close()

    return file_wrapper
