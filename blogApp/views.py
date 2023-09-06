from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Blog_title
# Create your views here.

def blog_page(request):
    tasks4=Blog_title.objects.all()
    #tasks5 = Blog_post.objects.all()
    return render(request, 'blog.html', {'tasks4': tasks4})
#def my_python_function(request,my_value):
#    return render(request, 'blog_post_content.html', {'my_value': my_value})

def my_function(request):
    if request.method == 'POST':
        my_value = request.POST.get('my_value')
        # Do something with my_value
        ##result = my_python_function(request,my_value)
        ##return HttpResponse(f'Result: {result}')
        return render(request, 'blog_post_content.html', {'my_value': my_value})
    else:
        # Handle GET request or initial form rendering
        return render(request, 'blog_post_content.html')

