from django.http import HttpResponse
from hw7CookiesHeaders.helpers.cookiesHelper import set_cookie_helper, get_cookie_helper
from hw7CookiesHeaders.helpers.headersHelper import set_header_helper, get_header_helper


def home(request):
    return HttpResponse("Hello, Django!")

def set_cookie(request):
    if request.method == 'GET':
        try:
            cookie_to_set = request.GET.dict()
            name = list(cookie_to_set.keys())[0]
            value = list(cookie_to_set.values())[0]
            httpOnly = False
            if "httpOnly" in cookie_to_set:
                httpOnly = request.GET.get("httpOnly")
            return set_cookie_helper(name, value, httpOnly)
        except:
            return HttpResponse("404 error: Failed to set the cookie")

def get_cookie(request, name):
    if request.method == 'GET':
        try:
            return HttpResponse(get_cookie_helper(request, name))
        except:
            return HttpResponse("404 error: Failed to get the cookie")
        
def set_header(request):
    if request.method == 'GET':
        try:
            header_to_set = request.GET.dict()
            name = list(header_to_set.keys())[0]
            value = list(header_to_set.values())[0]
            return set_header_helper(name, value)
        except:
            return HttpResponse("404 error: Failed to set the header")

def get_header(request, name):
    if request.method == 'GET':
        try:
            return HttpResponse(get_header_helper(request, name))
        except:
            return HttpResponse("404 error: Failed to get the header")