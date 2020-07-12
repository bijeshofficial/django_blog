from django.shortcuts import render

posts = [
    {
        'author':'Bijesh',
        'title':'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'July 12, 2020'
    },
    {
        'author':'Rupesh',
        'title':'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'July 13, 2020'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


