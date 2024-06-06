# books/urls.py


from django.urls import path
from books import views


urlpatterns = [
    path('books/', views.book_index, name='book_index'),
    path('', views.home_html, name='home_html'),
    #path('<int:pk>/', views.book_detail, name='book_detail'),
]