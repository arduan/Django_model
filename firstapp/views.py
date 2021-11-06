from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
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

# Изменения данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == 'POST':
            client = Person()
            client.name = request.POST.get('name')
            client.age = request.POST.get('age')
            client.save()
            return  HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Клиент не найден</h2>')

# Удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Клиент не найден</h2>')