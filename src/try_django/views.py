from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    return render(request, "home.html", {"title": "Hello there ...", "my_list": [1, 2, 3, 4]})

def about_page(request):
    return render(request, "about.html", {"title": "About Us"})

def contact_page(request):
    print(request.path, request.method, request.user, request.POST)
    return render(request, "contact.html", {"title": "Contact Us"})

def example_page(request):
    context = {"title": "example"}
    template_name = "contact.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
