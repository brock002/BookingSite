from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, ListView, TemplateView
from . import forms, models
from django.http import HttpResponse, HttpResponseRedirect

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "movie_app/signup.html"


class NotEnough(TemplateView):
    template_name = "movie_app/not_enough.html"


def Loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse("movie_app:current_shows"))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        #Nothing has been provided for username or password.
        return render(request, 'movie_app/login.html', {})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('thanks'))

@login_required
def MovieListView(request):
    movie_list = models.Movie.objects.all()
    return render(request, 'movie_app/movies_showing.html', {'movie_list':movie_list, 'i':0, 'breaks':(0, 3, 6, 9)})

@login_required
def show_times(request, pk):
    movie = get_object_or_404(models.Movie, pk=pk)
    halls = models.Hall.objects.all()
    shows_one = movie.show_set.filter(hall = halls[0])
    if shows_one.exists() == False:
        shows_one = None
    shows_two = movie.show_set.filter(hall = halls[1])
    if shows_two.exists() == False:
        shows_two = None
    shows_three = movie.show_set.filter(hall = halls[2])
    if shows_three.exists() == False:
        shows_three = None
    return render(request, 'movie_app/movie_detail.html', {'shows_one':shows_one, 
                                                           'shows_two':shows_two, 
                                                           'shows_three':shows_three, 
                                                           'movie':movie})

@login_required
def show_seats(request, pk):
    show = get_object_or_404(models.Show, pk=pk)
    if request.method == "POST":
        ticket_type = request.POST.get("type_radio")
        ticket_no = request.POST.get("no_of_ticket")
        if ticket_type=="VIP":
            if int(ticket_no)>show.vip_left:
                return HttpResponseRedirect(reverse("movie_app:NotEnough"))
            ticket_price = show.hall.vip_price
        elif ticket_type=="Platinum":
            if int(ticket_no)>show.platinum_left:
                return HttpResponseRedirect(reverse("movie_app:NotEnough"))
            ticket_price = show.hall.platinum_price
        elif ticket_type=="Gold":
            if int(ticket_no)>show.gold_left:
                return HttpResponseRedirect(reverse("movie_app:NotEnough"))
            ticket_price = show.hall.gold_price
        elif ticket_type=="Silver":
            if int(ticket_no)>show.silver_left:
                return HttpResponseRedirect(reverse("movie_app:NotEnough"))
            ticket_price = show.hall.silver_price
        total = float(ticket_price) * int(ticket_no)
        user = get_user_model().objects.get(id=request.user.id)
        b = models.Bought_ticket.objects.create(user = user, show = show, total_amount = total,ticket_type = ticket_type, no_of_tickets = ticket_no)
        b.save()
        return render(request, "movie_app/show_seats.html", {'show':show,'total':total, 'ticket_no': ticket_no, 'ticket_price': ticket_price})

    return render(request, 'movie_app/show_seats.html', {'show':show})

@login_required
def payments(request, pk):
    tickets = models.Bought_ticket.objects.order_by("-pk")[0]
    if request.method == "POST":
        payment_method = request.POST.get("payment_method")
        tickets.paid = True
        if tickets.ticket_type == "VIP":
            tickets.show.vip_left = tickets.show.vip_left - tickets.no_of_tickets
        elif tickets.ticket_type == "Platinum":
            tickets.show.platinum_left -= tickets.no_of_tickets
        elif tickets.ticket_type == "Gold":
            tickets.show.gold_left -= tickets.no_of_tickets
        elif tickets.ticket_type == "Silver":
            tickets.show.silver_left -= tickets.no_of_tickets
        tickets.show.save()
        tickets.save()
        return render(request, 'movie_app/payments.html', {'tickets':tickets, 'payment_method':payment_method})
    return render(request, 'movie_app/payments.html', {'tickets':tickets})

@login_required
def booked_tickets(request):
    user = get_user_model().objects.get(id = request.user.id)
    tickets = user.bought_ticket_set.all()
    if(len(tickets)==0):
        return render(request, "movie_app/my_tickets.html")
    return render(request, "movie_app/my_tickets.html", {'tickets':tickets})

