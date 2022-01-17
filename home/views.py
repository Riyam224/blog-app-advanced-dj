import email
from django.shortcuts import render

# Create your views here.
from post.models import Post
from marketing.models import Signup

def index(request):
    object_list = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[:2]


    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {

        'object_list': object_list,
        'latest': latest
    }
    
    return render(request , 'index.html', context)


