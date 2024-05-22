from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Movies, Actress
# from .forms import ActressForm


# Create your views here.

def index(request):
    return render(request, "movies/index.html", {
    
    })

def actress_list(request):
    return render(request, "movies/actress_list.html", {
        "actresses": Actress.objects.all(),
        "count": Actress.objects.all().count()
    })

def actress_detail(request, actress_id):
    try:
        actress = Actress.objects.get(pk=actress_id)
    except actress.DoesNotExist:
        raise Http404("actress not found.")
    return render(request, "movies/actress_detail.html", {
        "actress": actress,
        "movies": actress.movies.all()  # show all movies that the actress is in
    })


def movies_list(request):
    return render(request, "movies/movies_list.html", {
        "movies": Movies.objects.all(),  # get the all data from the table Actress
        "count": Movies.objects.all().count()
    })

def movie_detail(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)

    return render(request, "movies/movie_detail.html", {
        "movie": movie,
        "actresses": movie.actress.all()  # show all actresses that the movie is in
    })

def movie_delete(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    movie.delete()
    return HttpResponseRedirect('../../')

def actress_delete(request, actress_id):
    actress = Actress.objects.get(id=actress_id)
    actress.delete()
    return HttpResponseRedirect('../../')

# def actress_add(request):
#     form = ActressForm()
#     context = {'form': form}
#     return render(request, 'movies/form.html', context)

# def actress_edit(request, actress_id):
#     try:
#         actress = Actress.objects.get(pk=actress_id)
#     except actress.DoesNotExist:
#         raise Http404("actress not found.")
#     return render(request, "movies/actress_edit.html", {
#         "actress": actress,
#         # "movies": actress.movies.all()  # show all movies that the actress is in
#     })

# from .forms import InputForm 

# def actress_add(request): 
#     if request.method == "POST": 
#         form = InputForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             enName = form.cleaned_data["enName"]
#             birth = form.cleaned_data["birth"]
#             heitht = form.cleaned_data["height"]
#             debut = form.cleaned_data["debut"]
#             info = form.cleaned_data["info"]

#             return HttpResponseRedirect("/OK/")
#         else:
#             form = InputForm()
    
#     return render(request, "movies/form.html", {"form": form}) 

   

# Added for search

from django.http import HttpResponse
from django.db.models import Q
from django import forms

def movie_search(request):   
    try:
        query = request.GET.get("name")
        query2 = request.GET.get("title")
    except query.DoesNotExist:
        raise Http404("query not found.")   
    
    if query:
        query = request.GET.get("name")
        object_list = Actress.objects.filter(
            Q(name__icontains=query) | Q(enName__icontains=query)
        ).order_by('enName')   # use the minus sign (NOT), order in reverse

        return render(request, "movies/search_results.html", {
            "actresses": object_list,
        })
    
    elif query2:
        query2 = request.GET.get("title")
        object_list = Movies.objects.filter(
            Q(title__icontains=query2) 
        ).order_by('title')   # use the minus sign (NOT), order in reverse

        return render(request, "movies/search_results.html", {
            "movies": object_list,
        })

    else:
        html = "<html><body><h1>na da.</h1></body></html>" 
        return HttpResponse(html)

# added for search

from django.views.generic import TemplateView, ListView
from django.db.models import Q

class SearchResultsView(ListView):
    model = Actress
    template_name = 'search_results.html'
    
    def get_queryset(self):  
        query = self.request.GET.get("q")
        object_list = Actress.objects.filter(
            Q(name__icontains=query) | Q(enName__icontains=query)
        )
        return object_list



# Added for the test

from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s.</h1></body></html>" % now
    return HttpResponse(html)


# Decorator to require that a view only accepts particular request methods. Usage:

from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def my_view(request):
        # I can assume now that only GET or POST requests make it this far
        # ...
        pass

# Note that request methods should be in uppercase.
