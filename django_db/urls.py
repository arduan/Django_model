
from django.contrib import admin
from django.urls import path

from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('admin/', admin.site.urls),
]
