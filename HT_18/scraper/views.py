from django.shortcuts import render

import requests
import re
from bs4 import BeautifulSoup
import time
import csv


def view(request):
    template = 'scraper/home.html'
    category = request.POST['category']
    quantity = request.POST['quantity']
    # TODO: add scrapper
    return render(request, template)

