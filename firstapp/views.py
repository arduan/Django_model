from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


def create(request):
    if request.method == 'POST':
        client = Person()
        client.name = request.POST.get('name')
        client.age = request.POST.get('age')
        client.save()
    return HttpResponseRedirect('/')