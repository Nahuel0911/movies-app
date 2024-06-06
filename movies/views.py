from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies' : ['World War Z', 'The Walking Dead', '28 Days Later']
    }
    return render(request, 'movies/index.html', context)

def aboutMe(request):
    return render(request, 'movies/about.html', {})