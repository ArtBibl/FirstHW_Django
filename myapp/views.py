from django.http import HttpResponse


def main(request):
    return HttpResponse("<h2>Hey! It's my main view!!<h2>")


def users(request):
    return HttpResponse("<h2>http://127.0.0.1:8000/users/<h2>")


def user_numb(request, user_number):
    return HttpResponse(f'<h2> User numb: {user_number} <h2>')


def articles(request):
    return HttpResponse("<h2>http://127.0.0.1:8000/articles/<h2>")


def archive(request):
    return HttpResponse(f"<h2>http://127.0.0.1:8000/articles/archive/<h2>")


def archive2(request, article_number):
    return HttpResponse(f"<h2>http://127.0.0.1:8000/articles/{article_number}/archive/<h2>")


def uniq_articles(request, article_number):
    return HttpResponse('<h2>http://127.0.0.1:8000/articles/ + 'f'{article_number}''<h2>')


def uniq_articles2(request, article_number, slug_text):
    return HttpResponse(f'<h2>http://127.0.0.1:8000/articles/{article_number}/{slug_text}<h2>')


def regex(request):
    return HttpResponse("<h2>It's regexp<h2>")


def regex_phone(request, text):
    return HttpResponse(f"it's regex with phone number: {text}")
