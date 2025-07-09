from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    #run our query by using post.objects.all() but we want to filter some things out..
    #anything that does not have a publish date will get filtered out
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #if we want to pass a query result to the html file, we will bind a python variable with a variable the html can us
    return render(request, 'blog/post_list.html', {'posts': posts})