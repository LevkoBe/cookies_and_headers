from django.http import HttpResponse


def set_header_helper(name, value):
    response = HttpResponse(f"Header set: <b>{name} = {value}</b>")
    response[name] = value
    return response

def get_header_helper(request, name):
    value = request.headers.get(name)
    if isinstance(value, str):
        return request.headers.get(name)
    return f"404 Error: %s not found" % name