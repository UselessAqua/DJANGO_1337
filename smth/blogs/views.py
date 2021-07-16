from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Blog


def index(request):
    return HttpResponse("Main page")
#вместо detail - blog_info
#create, insert, update

def blog_info(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/blog.html', {'blog': blog})

#def



# Create your views here.
