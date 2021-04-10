from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import http.client, json, requests
from bson import ObjectId

# Create your views here.

my_api_key = '9e8c5a314d6ac88caafdf94f375f64c3'
base_url = 'https://api.themoviedb.org/3/'

def home(request):
    if request.method == "POST":
        if "ajax" in request.POST:
            movie_name = request.POST.get("movie_name")
            url = f'{base_url}search/movie/?api_key={my_api_key}&language=en-US&query={movie_name}&page=1'
            response = requests.get(url)
            l = response.json()['results']
            return JsonResponse(l, safe=False)
    return render(request, 'home.html', {})
