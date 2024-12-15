from django.contrib import admin
from .models import Lecture, Speaker, Place

admin.site.register(Lecture)
admin.site.register(Speaker)
admin.site.register(Place)