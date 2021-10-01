from django.urls import path
from . import views
urlpatterns=[
    path('',views.games_index ,name='games_index')
]