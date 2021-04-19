from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import http.client, json, requests
from .forms import AccountAuthenticationForm, RegistrationForm
from .models import Account, Movie


# Create your views here.

my_api_key = '9e8c5a314d6ac88caafdf94f375f64c3'
base_url = 'https://api.themoviedb.org/3/'

def home(request):
    trend = f'{base_url}trending/all/day?api_key={my_api_key}'
    response = requests.get(trend)
    l = response.json()['results']
    '''if request.method == "POST":
        if "ajax" in request.POST:
            movie_name = request.POST.get("movie_name")
            url = f'{base_url}search/movie/?api_key={my_api_key}&language=en-US&query={movie_name}&page=1'
            response = requests.get(url)
            l = response.json()['results']
            hr = JsonResponse(l, safe=False)
            return render(request, 'movies.html', {'hr': hr})
            return hr'''
    return render(request, 'home.html', {'trending_movies': l})

def search_results(request):
    user = request.user
    if request.method == "POST":
        movie_id = request.POST.get("name")
        m = Movie.objects.filter(movie_id=movie_id)
        if m:
            m[0].user.add(user)
        else:
            movie = Movie(movie_id=movie_id)
            movie.save()
            movie.user.add(user)
        return JsonResponse({"msg":"Saved.", })
    search = request.GET.get('search')
    url = f'{base_url}search/movie/?api_key={my_api_key}&language=en-US&query={search}&page=1'
    response = requests.get(url)
    l = response.json()['results']
    return render(request, 'movies.html', {'results': l})

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()
        context['login_form'] = form

    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("home")
        else:
            context['registration_form'] = form
            return render(request, 'register.html', context)

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)
