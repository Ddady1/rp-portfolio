# serach/urls.py

from django.urls import path
from search import views


urlpatterns = [
    path('search/', views.search_main, name='search-main'),
    path('results/', views.search_results, name='search-results'),
]