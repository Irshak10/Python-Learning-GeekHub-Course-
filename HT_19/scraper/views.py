from django.shortcuts import render
from scraper.tasks import scraper_1
from django.contrib import messages


def view(request):
    template = 'scraper/home.html'
    scraper_1(request)
    messages.success(request, 'New products are generated and moved to admin panel')

    return render(request, template)
