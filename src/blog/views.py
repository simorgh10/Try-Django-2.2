from django.shortcuts import render

# Create your views here.
from .models import BlogPost


def blog_post_detail_page(request, post_id):
    template_name = "blog_post_detail_page.html"
    obj = BlogPost.objects.get(id=post_id)
    context = {"obj": obj}
    return render(request, template_name, context)