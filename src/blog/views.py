from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost


def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail_page.html"
    context = {"obj": obj}
    return render(request, template_name, context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = "blog_post_list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)

def blog_post_create_view(request):
    template_name = "blog_post_create.html"
    context = {"form": None}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail.html"
    context = {"obj": obj}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_update.html"
    context = {"obj": obj, "form": None}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_update.html"
    context = {"obj": obj}
    return render(request, template_name, context)


