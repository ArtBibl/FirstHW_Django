from django.urls import path
from .views import articles, archive, archive2, uniq_articles, uniq_articles2

urlpatterns = [
    path('', articles),  # http://127.0.0.1:8000/articles/
    path('archive/', archive),  # http://127.0.0.1:8000/articles/archive/
    path('<int:article_number>/', uniq_articles),  # http://127.0.0.1:8000/articles/797/
    path('<int:article_number>/archive/', archive2),  # http://127.0.0.1:8000/articles/797/archive/
    path('<int:article_number>/<slug:slug_text>', uniq_articles2),  # http://127.0.0.1:8000/articles/133/dfsg
]
