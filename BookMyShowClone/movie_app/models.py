from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return str(self.username)

class Movie(models.Model):
    poster = models.ImageField(null=True, upload_to='movie_posters')
    thumbnail = models.ImageField(null=True, upload_to='movie_thumbnails')
    name = models.CharField(max_length=50, unique = True)
    released_date = models.DateField()
    language = models.CharField(max_length=20, default='English')
    length = models.TimeField(default = '02:00:00')

    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=50, unique = True)
    location = models.CharField(max_length=80)
    vip_no = models.PositiveIntegerField(null = True)
    gold_no = models.PositiveIntegerField(null = True)
    platinum_no = models.PositiveIntegerField(null = True)
    silver_no = models.PositiveIntegerField(null = True)
    vip_price = models.FloatField(null = True)
    gold_price = models.FloatField(null = True)
    platinum_price = models.FloatField(null = True)
    silver_price = models.FloatField(null = True)

    def __str__(self):
        return self.name

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null = True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null = True)
    show_time = models.DateTimeField(null = True)
    vip_left = models.PositiveIntegerField(null = True)
    gold_left = models.PositiveIntegerField(null = True)
    silver_left = models.PositiveIntegerField(null = True)
    platinum_left = models.PositiveIntegerField(null = True)

    def __str__(self):
        return str(self.movie.name) + " at " + str(self.hall.name)

class Bought_ticket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    total_amount = models.FloatField(null = True)
    ticket_type = models.CharField(null=True, max_length=10)
    no_of_tickets = models.PositiveIntegerField(default=1)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username) + " booked tickets for " + str(self.show.movie.name) + " Paid: " + str(self.paid)
