from django.urls import path

from . import views

urlpatterns = [
    path('<int:route_id>', views.route, name='route'),
    path('', views.search, name='search'),
    path('/routes', views.index, name='index'),
]
