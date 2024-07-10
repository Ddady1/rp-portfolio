#  personal_portfolio/urls.py


"""
URL configuration for personal_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('projects/', include('projects.urls')),
    path('books/', include('books.urls')),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:band_id>/change', views.band_edit, name='band-edit'),
    path('about-us/', views.about),
    path('songs/', views.songs_list, name='songs-list'),
    path('songs/<int:song_id>/', views.song_detail, name='song-detail'),
    path('songs/add/', views.song_create, name='song-create'),
    path('songs/<int:song_id>/change', views.song_edit, name='song-edit'),
    path('contact-us/', views.contact, name='contact'),
    path('email-sent/', views.email_sent, name='sent-e'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
