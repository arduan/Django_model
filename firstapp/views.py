from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person


# Получение данных из БД и загрузка index.html
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})

# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        client = Person()
        client.name = request.POST.get('name')
        client.age = request.POST.get('age')
        client.save()
    return HttpResponseRedirect('/')