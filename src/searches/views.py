from django.shortcuts import render

# Create your views here.
from .models import SearchQuery
from blog.models import BlogPost


def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query": query}
    if query:
        SearchQuery.objects.create(user=user, query=query)
        qs = BlogPost.objects.published().search(query)
        if request.user.is_authenticated:
            my_qs = BlogPost.objects.filter(user=request.user).search(query)
            qs = (qs | my_qs).distinct()
        context["blog_list"] = qs
    return render(request, "searches/view.html", context)
