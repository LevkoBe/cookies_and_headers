from django.urls import path
from hw7CookiesHeaders import views

urlpatterns = [
    # http://127.0.0.1:8000/hw7/
    path("", views.home, name="home"),
    # http://127.0.0.1:8000/hw7/cookies/set
    # http://127.0.0.1:8000/hw7/cookies/set?cookie=123
    # http://127.0.0.1:8000/hw7/cookies/set?nm=foo&httpOnly=true
    path("cookies/set", views.set_cookie, name="set_cookie"),
    # http://127.0.0.1:8000/hw7/cookies/get/foo
    # http://127.0.0.1:8000/hw7/cookies/get/bar
    path("cookies/get/<str:name>", views.get_cookie, name="get_cookie"),
    # http://127.0.0.1:8000/hw7/headers/set
    # http://127.0.0.1:8000/hw7/headers/set?header=234
    # http://127.0.0.1:8000/hw7/headers/set?nm=foo
    path("headers/set", views.set_header, name="set_header"),
    # http://127.0.0.1:8000/hw7/headers/get/host
    # http://127.0.0.1:8000/hw7/headers/get/tost
    path("headers/get/<str:name>", views.get_header, name="get_header"),
]