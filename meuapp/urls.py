from django.urls import path
from . import views


app_name = 'meuapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]