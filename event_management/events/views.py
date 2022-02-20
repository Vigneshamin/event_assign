from django.shortcuts import render, redirect, get_object_or_404
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from datetime import datetime
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            cus = Customer.objects.get(name=username)
            cus.email = form.cleaned_data.get('email')
            cus.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'events/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.info(request, "Username OR password is incorrect")
    context = {}
    return render(request, 'events/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    event = Event.objects.all()
    bookings = Bookings.objects.all()
    customers = Customer.objects.all()
    context = {'events':event, 'customers':customers}
    return render(request, 'events/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    if request.method == 'POST':
        customerdata = request.user.customer
        Ev = Event.objects.get(name=request.POST.get('ename'))
        if int(request.POST.get('tickets')) <= Ev.remticket and int(request.POST.get('tickets'))!=0 and Ev.status =="Active":
            Ev.remticket = Ev.remticket - int(request.POST.get('tickets'))
            Ev.save()
            bookevent = Bookings.objects.create(customer=customerdata,
                                           event=Event.objects.get(name=request.POST.get('ename')),
                                           date_created=datetime.now(),
                                           no_ticket=int(request.POST.get('tickets')),)
            msg = "Booked"
        else:
            msg = "Tickets cannot be Booked"
    else:
        msg=""
    event = Event.objects.all()
    customer = request.user.customer
    c = Customer.objects.get(id=customer.id)
    booking = c.bookings_set.all()
    id = customer.id
    context = {'events':event , 'bookings':booking, 'msg':msg}
    return render(request, 'events/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def deleteBooking(request, id):
    booking = Bookings.objects.get(id=id)
    if request.method == 'POST':
        Ev = Event.objects.get(name=booking.event.name)
        Ev.remticket = Ev.remticket + int(booking.no_ticket)
        Ev.save()
        booking.delete()
        return redirect('/')
    context = {'item':booking}
    return render(request, 'events/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateEvent(request, id):
    context={}
    obj = get_object_or_404(Event, id=id)
    form = EventupdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    return render(request, "events/update.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteEvent(request, id):
    context={}
    event = Event.objects.get(id=id)
    nm = event.name
    event.status='Cancelled'
    event.save()
    Book = Bookings.objects.filter(event=id)
    for i in Book:
        i.status='Cancelled'
        i.save()
    return HttpResponseRedirect("/")


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createevent(request):
    context = {}
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form'] = form
    return render(request, "events/create_event.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def viewprofile(request,id):
    cust = Customer.objects.get(id=id)
    booking = cust.bookings_set.all()

    context = {'bookings':booking, "name":cust.name, "email":cust.email}
    return render(request, "events/profile.html", context)






