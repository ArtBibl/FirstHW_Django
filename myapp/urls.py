from django.urls import path
from .views import main, articles, archive, uniq_articles, user_numb

urlpatterns = [
    path('', main),
    # http://127.0.0.1:8000/articles/
    path('archive/', archive),
    # http://127.0.0.1:8000/articles/archive/
    path('<int:article_number>/', uniq_articles),
    # http://127.0.0.1:8000/articles/797/
    path('<int:article_number>/archive/', archive),
    # http://127.0.0.1:8000/articles/797/archive/
    path('<int:article_number>/<slug:slug_text>', articles, name='article'),
    path('<int:user_number>/', user_numb),
]
