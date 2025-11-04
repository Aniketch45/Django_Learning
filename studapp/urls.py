from django.urls import path     #importing path
from studapp import views
urlpatterns = [
    path('studapp/', views.greet, name='greet'),
    path('custom/', views.custom, name='custom')
]
