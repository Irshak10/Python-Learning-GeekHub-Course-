from django.contrib import admin

from crud.models import Crud, Comment


admin.site.register(Crud)
admin.site.register(Comment)