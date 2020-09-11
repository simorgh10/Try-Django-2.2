from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    qs = BlogPost.objects.published()[:5]
    template_name = "home.html"
    blog_list = {"title": "Welcome to Try Django", "blog_list": qs}
    return render(request, "home.html", blog_list)

def about_page(request):
    return render(request, "about.html", {"title": "About Us"})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "Contact Us", "form": form}
    return render(request, "contact.html", context)

def example_page(request):
    context = {"title": "example"}
    template_name = "contact.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
