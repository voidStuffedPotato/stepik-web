def app(env, start_response):
    status = "200 OK"
    data = (str(env['QUERY_STRING'])
            .replace('&', '\n')
            .encode('ascii')) + b'\n'
    headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, headers)
    return [data]
