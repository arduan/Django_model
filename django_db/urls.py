
from django.contrib import admin
from django.urls import path

from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create),
    path('admin/', admin.site.urls),
]
