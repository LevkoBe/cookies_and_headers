from django.http import HttpResponse


def set_cookie_helper(name, value, httpOnly=False):
    response = HttpResponse(f"Cookie set: <b>{name} = {value}</b>")
    response.set_cookie(name, value, max_age=3600000, httponly=httpOnly)
    return response

def get_cookie_helper(request, name):
    value = request.COOKIES.get(name)
    if isinstance(value, str):
        return f"Cookie {name} has value {request.COOKIES.get(name)}"
    return f"404 Error: Cookie <b>{name}</b> not found"