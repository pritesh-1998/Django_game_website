from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Movie
from django.shortcuts import render
# Create your views here.

def index(request):
    movies=Movie.objects.all()
    # output=','.join([m.title for m in movies_data])
    # # filtering data
    # Movie.objects.filter(release=1998)
    # # getting data
    # return HttpResponse(output)
    return render(request,'index.html',{"movies":movies})

def details(request,movie_id):
    # try:
    #     movie=Movie.objects.get(id=movie_id)
    #     return render(request,'details.html',{'movie':movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
    movie=get_object_or_404(Movie,id=movie_id)
    return render(request,'details.html',{'movie':movie})
