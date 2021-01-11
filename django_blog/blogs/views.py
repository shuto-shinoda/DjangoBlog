from django.shortcuts import render
from .models import Blog
from django.db.models import Q

def index(request):
   query = request.GET.get('q')
   if query:
       blog = Blog.objects.all().order_by('-created_at')
       blog = blog.filter(
       Q(title__icontains=query)|
       Q(user__username__icontains=query)
       ).distinct()
   else:
       blog = Post.objects.all().order_by('-created_at')  
   return render(request, 'blogs/index.html', {'blog': blog, 'query': query,})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})
