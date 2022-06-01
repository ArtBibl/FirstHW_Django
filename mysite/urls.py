from django.urls import path, include, re_path
from myapp.views import main, users, user_numb, regex, regex_phone

urlpatterns = [
    path('', main),  # http://127.0.0.1:8000/,
    path('articles/', include('myapp.urls')),  # http://127.0.0.1:8000/articles/
    path('users/', users),  # http://127.0.0.1:8000/users/
    path('users/<int:user_number>/', user_numb),  # http://127.0.0.1:8000/users/234/
    re_path('^.{4}[1-9a-f\-].{6}$', regex),  # http://127.0.0.1:8000/34f1-1ac498
    re_path(r'^(?P<text>050\d{7}$)', regex_phone),  # http://127.0.0.1:8000/0501234567
]
