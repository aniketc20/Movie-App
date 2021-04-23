"""Movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from App.views import (
    home,
    search_results,
    login_view,
    registration_view,
    logout_view,
    my_movies
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('searchbar/', search_results, name='searchbar'),
    path('login/', login_view, name='login_view'),
    path('register/', registration_view, name='registration_view'),
    path('logout/', logout_view, name="logout"),
    path('favourites/', my_movies, name="favourites"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
