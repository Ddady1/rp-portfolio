# books/urls.py


from django.urls import path
from books import views


urlpatterns = [
    path('', views.book_index, name='book_index'),
    #path('<int:pk>/', views.book_detail, name='book_detail'),
]