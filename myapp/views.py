from django.http import HttpResponse


def main(request):  # http://127.0.0.1:8000/,
    return HttpResponse("<h2>Hey! It's my main view!!<h2>")


def articles(request):  # http://127.0.0.1:8000/articles/
    return HttpResponse("<h2>http://127.0.0.1:8000/articles/<h2>")


def archive(request):  # http://127.0.0.1:8000/articles/archive/
    return HttpResponse("<h2>http://127.0.0.1:8000/articles/archive/<h2>")


def users(request):  # http://127.0.0.1:8000/users/
    return HttpResponse("<h2>http://127.0.0.1:8000/users/<h2>")


def uniq_articles(request, article_number):
    return HttpResponse('<h2>http://127.0.0.1:8000/articles/ + 'f'{article_number}''<h2>')


def user_numb(request, user_number):
    return HttpResponse(f'<h2> User numb {user_number} <h2>')

# def articles(request, article_id, name=''):
#     return HttpResponse(
#         "This is an article #{}. {}"
#             .format(article_id, "Name of this article is {}"
#                     .format(name) if name else "This is unnamed article"))


def regex(request):
    return HttpResponse("<h2>It's regexp<h2>")


def regex_phone(request, text):  # http://127.0.0.1:8000/0501234567
    return HttpResponse(f"it's regex with phone number: {text}")
