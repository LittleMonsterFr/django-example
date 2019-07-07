from django.urls import path

from . import views

app_name = 'places'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_place, name='add_place'),
    path('<int:place_id>/', views.detail, name='detail'),
    path('<int:place_id>/delete', views.delete_place, name='delete_place'),
]
