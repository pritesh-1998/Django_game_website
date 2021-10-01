from django.shortcuts import render
from django.http import HttpResponse
from.models import games
# Create your views here.
def games_index(request):
    games1=games.objects.all()
    links={
        "number":games1
    }
    return render(request,'index2.html',links)
