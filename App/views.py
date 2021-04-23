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
    video = requests.get('https://www.youtube.com/watch?v=6ZfuNTqbHE8')
    trend = f'{base_url}trending/all/day?api_key={my_api_key}'
    response = requests.get(trend)
    l = response.json()['results']
    for i in l:
        id = i['id']
        movie_cast_url = f'{base_url}/movie/{id}/credits?api_key={my_api_key}&language=en-US'
        response = requests.get(movie_cast_url)
        if response.status_code==200 and i['media_type']=='movie':
            movie_cast = response.json()['cast']
            count = 0
            actors = []
            for j in movie_cast:
                if count==4:
                    break
                actors.append(j['name'])
                count = count+1
            i['cast']=actors
        movie_cast_url = f'{base_url}tv/{id}/season/1/credits?api_key={my_api_key}&language=en-US'
        response = requests.get(movie_cast_url)
        if response.status_code==200 and i['media_type']=='tv':
            movie_cast = response.json()['cast']
            count = 0
            actors = []
            for j in movie_cast:
                if count==4:
                    break
                actors.append(j['original_name'])
                count = count+1
            i['cast']=actors
    return render(request, 'home.html', {'trending_movies': l})

def search_results(request):
    user = request.user
    fav_mov_list = Movie.objects.all()
    if request.method == "POST":
        if 'ajax' in request.POST:
            movie_id = request.POST.get("name")
            m = Movie.objects.filter(movie_id=movie_id)
            if m:
                m[0].user.add(user)
            else:
                movie = Movie(movie_id=movie_id)
                movie.save()
                movie.user.add(user)
            return JsonResponse({"msg":movie_id, })
        if 'remove' in request.POST:
            movie_id = request.POST.get("name")
            m = Movie.objects.filter(movie_id=movie_id)
            m[0].user.remove(user)
            return JsonResponse({"msg":movie_id, })
    search = request.GET.get('search')
    url = f'{base_url}search/movie/?api_key={my_api_key}&language=en-US&query={search}&page=1'
    response = requests.get(url)
    l = response.json()['results']
    for i in l:
        movie_cast_url = f'{base_url}/movie/{i["id"]}/credits?api_key={my_api_key}&language=en-US&query={search}&page=1'
        response = requests.get(movie_cast_url)
        movie_cast = response.json()['cast']
        count = 0
        actors = []
        for j in movie_cast:
            if count==10:
                break
            actors.append(str(j['profile_path']))
            actors.append(str(j['name']))
            count = count+1
        i['cast']=actors
    return render(request, 'movies.html', {'results': l, 'fav_mov_list': fav_mov_list})

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

def my_movies(request):
    m = Movie.objects.filter(user=request.user)
    fav_mov_list = []
    if request.method == "POST":
        if 'remove' in request.POST:
            movie_id = request.POST.get("name")
            m = Movie.objects.filter(movie_id=movie_id)
            m[0].user.remove(request.user)
            return JsonResponse({"msg":movie_id, })
    for i in m:
        url = f'{base_url}movie/{i.movie_id}?api_key={my_api_key}&language=en-US'
        response = requests.get(url)
        l = response.json()
        movie_cast_url = f'{base_url}/movie/{i.movie_id}/credits?api_key={my_api_key}&language=en-US'
        response = requests.get(movie_cast_url)
        movie_cast = response.json()['cast']
        count = 0
        actors = []
        for j in movie_cast:
            if count==10:
                break
            actors.append(j['profile_path'])
            actors.append(j['name'])
            count = count+1
        l['cast']=actors
        fav_mov_list.append(l)
    return render(request, 'fav_mov_list.html', {'fav_mov_list': fav_mov_list})
