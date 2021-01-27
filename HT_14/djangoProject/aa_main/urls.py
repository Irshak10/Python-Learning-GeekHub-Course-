"""aa_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from crud.views import main_menu, single_product, leave_comment, creating_product

urlpatterns = [
    path('', main_menu, name='main_menu'),
    path('creating_product/', creating_product, name='creating_product'),
    path('<int:single_id>/', single_product, name='single_product'),
    path('<int:single_id>/leave_comment', leave_comment, name='leave_comment'),
    path('admin/', admin.site.urls),
]
