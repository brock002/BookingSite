from django.urls import path
from . import views

app_name = 'movie_app'

urlpatterns = [
    path('NotEnough/', views.NotEnough.as_view(), name="NotEnough"),
    path('shows/', views.MovieListView, name = 'current_shows'),
    path('shows/<int:pk>/', views.show_times, name='movie_shows'),
    path('shows/<int:pk>/book', views.show_seats, name='seats'),
    path('shows/<int:pk>/payments', views.payments, name = 'payments'),
    path('my_tickets/', views.booked_tickets, name='my_tickets'),
    path("login/", views.Loginview, name='login'),
]