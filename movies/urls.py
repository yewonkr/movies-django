from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("actress_list", views.actress_list, name="actress_list"),
    path("actress_detail/<int:actress_id>", views.actress_detail, name="actress_detail"),
    # path("actress_add/", views.actress_add, name="actress_add"),
    # path("actress_edit/<int:actress_id>", views.actress_edit, name="actress_edit"),

    path("movies_list/", views.movies_list, name="movies_list"),
    path("movie_detail/<int:movie_id>", views.movie_detail, name="movie_detail"),

    path("movie_delete/<int:movie_id>", views.movie_delete, name="movie_delete"),
    path("actress_delete/<int:actress_id>", views.actress_delete, name="actress_delete"),

    path('movie_search', views.movie_search, name='movie_search'),
]    

# added for search

from . views import SearchResultsView

urlpatterns += [
    path("search/", SearchResultsView.as_view(), name="search"),
]

#  Added for the test

urlpatterns += [
    path("time/", views.current_datetime, name="time"),
]
