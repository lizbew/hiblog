from django.shortcuts import render
from django.http import HttpResponse

from .models import BlogPost

def index(request):
    #return HttpResponse("Hello world")
    latest_post_list = BlogPost.objects.order_by('-pub_date')[:5]

    context = {
    	'post_list': latest_post_list
    }

    return render(request, 'index.html', context)
