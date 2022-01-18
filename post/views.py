
from audioop import reverse
from django.shortcuts import render , get_object_or_404, redirect , reverse
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from .models import Post
from .forms import CommentForm
from django.db.models import Count , Q


# Create your views here.


def search(request):
    post_list = Post.objects.all()
    post = request.GET.get('q')
    if post:
        post_list = post_list.filter(
            Q(title__icontains = post) | 
            Q(overview__icontains = post)
        ).distinct()
    
    context = {'post_list': post_list}
    return render(request , 'search_results.html', context)


def get_category_count():
    post_list = Post.objects.values('category__title').annotate(Count('category__title'))
    return post_list


def blog(request):

    category_count = get_category_count()
    post_list = Post.objects.all()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    paginator = Paginator(post_list , 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        post_list  = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(2)
    except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
    
    context = {
        
        'post_list': post_list,
        'most_recent':most_recent,
        'page_request_var':page_request_var,
        'category_count':category_count,

    }
    return render(request , 'blog.html' , context)



def post(request , pk):

    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post , pk=pk)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post:post_detail' , kwargs = {
             
              'pk' : post.pk
            }))

    return render(request , 'post.html', {

        'form': form,
        'post': post,
        'most_recent':most_recent,
        'category_count':category_count,
       

    })