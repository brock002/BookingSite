from django.contrib import admin
from .models import Movie, Hall, Show, Bought_ticket

# Register your models here.

admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Bought_ticket)