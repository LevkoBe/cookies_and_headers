
from django.contrib import admin
from django.urls import include, path
from web_project.views import main_page

urlpatterns = [
    path('', main_page, name="main_page"),
    path('hw7/', include("hw7CookiesHeaders.urls")),
    path('admin/', admin.site.urls),
]
