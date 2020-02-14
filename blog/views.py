from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Corey_ms',
        'title': 'BlogPost1',
        'content': 'First post content',
        'date_posted': '2019'
    },

    {
        'author': 'Przem',
        'title': 'BlogPost2',
        'content': 'Second post content',
        'date_posted': '2019'
    },

    {
        'author': 'Jane',
        'title': 'BlogPost3',
        'content': 'Third post content',
        'date_posted': '2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
