from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Count
from django.contrib.auth import get_user_model

from .models import Advertisement
from .forms import AdvertisementForms

from django.core.handlers.wsgi import WSGIRequest

User = get_user_model()

def index(request):
    if request.GET.get('query'):
        title = request.GET.get('query')
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()

    context = {
        "advertisements": advertisements,
    }

    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count("advertisement")
    ).order_by("-adv_count")
    context = {
        "users": users
    }

    return render(request, 'app_advertisements/top-sellers.html', context)

def post_adv(request: WSGIRequest ):

    if request.method == "POST":
        form = AdvertisementForms(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect(
                reverse("main")
            )
    else:
        form = AdvertisementForms()
    context = {
        "form": form,
    }
    return render(request, 'app_advertisements/advertisement-post.html', context)

def adv_detail(request, pk):
    advertisements = Advertisement.objects.get(id=pk)
    context = {
        'adv': advertisements
    }
    return render(request, "app_advertisements/advertisement.html", context)
