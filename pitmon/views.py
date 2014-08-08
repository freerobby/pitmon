from __future__ import unicode_literals
from django.http import HttpResponse


def home(request):
    return HttpResponse("OK", content_type='text/html')
