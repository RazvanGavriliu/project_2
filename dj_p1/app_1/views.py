from django.shortcuts import render
from django.http import HttpResponse

from .models import Person
# Create your views here.


def person_list(request):
    if request.method == 'GET':
        persons_obj = Person.objects.all()

    return render(request, 'app_1/list_persons.html', {'persons': persons_obj})
