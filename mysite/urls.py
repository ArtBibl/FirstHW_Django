from django.urls import path, include, re_path
from myapp.views import main, users, regex, regex_phone

urlpatterns = [
    path('', main),  # http://127.0.0.1:8000/,
    path('articles/', include('myapp.urls')),
    path('users/', include('myapp.urls'), users),
    re_path('^.{4}[1-9a-f\-].{6}$', regex),  # http://127.0.0.1:8000/34f1-1ac498
    re_path(r'^(?P<text>050\d{7}$)', regex_phone),  # http://127.0.0.1:8000/0501234567
]
