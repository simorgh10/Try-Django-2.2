from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import BlogPost


def blog_post_detail_page(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() >= 1:
        obj = queryset.first()
    else:
        raise Http404
    template_name = "blog_post_detail_page.html"
    context = {"obj": obj}
    return render(request, template_name, context)