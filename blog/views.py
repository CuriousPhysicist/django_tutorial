from django.shortcuts import render

posts = [
    {
        'author': 'CuriousPhysicist',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 25, 2020',
    },
    {
        'author': 'CuriousPhysicist',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 30, 2020',
    }
]

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })

