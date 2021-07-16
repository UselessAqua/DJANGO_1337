from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Blog, Recording

def index(request):
    latest_blogs_list = Blog.objects.order_by('-theme')[:10]
    output = ', '.join([b.theme for b in latest_blogs_list])
    return HttpResponse(output)


# def (request):

#вместо detail - blog_info
#create, delete, update

def blog_info(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    latest_recordings_list = blog.recording_set.all()
    output = ', '.join([r.header for r in latest_recordings_list])
    return HttpResponse(output)
    #return render(request, 'blogs/blog.html', {'blog': blog})

#def



# Create your views here.
