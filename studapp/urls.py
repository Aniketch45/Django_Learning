from django.urls import path     #importing path
from studapp import views
urlpatterns = [
    path('',views.index, name='index'),
    path('home/',views.home, name='greet'),
    path('studapp/', views.greet, name='greet'),
    path('custom/', views.custom, name='custom'),
]
