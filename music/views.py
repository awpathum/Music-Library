from django.http import HttpResponse


def index(resquest):
    return HttpResponse('<h1> This is the music app homepage</h1>')