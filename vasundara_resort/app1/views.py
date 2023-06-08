from django.shortcuts import render,redirect
from  .models import *
import datetime

# Create your views here.

def index_view(request):
    return render(request, 'app1/index.html')

def booking_view(request):
    if request.method == 'POST':
        print(request.POST)
        u_name = request.POST.get('nm')
        u_email = request.POST.get('email')
        u_mobile = request.POST.get('mobile')
        u_rooms = request.POST.get('rooms')
        u_persons  = request.POST.get('persons')
        u_checkin = request.POST.get('checkin')
        u_checkout = request.POST.get('checkout')

        tm = datetime.datetime.now()

        obj = Booking_info(name=u_name,email=u_email, mobile = u_mobile,rooms=u_rooms, persons=u_persons , checkin=u_checkin, checkout=u_checkout,timestamp=tm)

        obj.save()

        return redirect('/display/')
        

    return render(request, 'app1/booking.html')


def display_view(request):
    data = Booking_info.objects.all()

    context = {
        'data' : data
    }
    return render(request, 'app1/display.html',context)


def update_view(request, u_id):
    obj = Booking_info.objects.get(id = u_id)

    if request.method == 'POST':
        u_name = request.POST.get('nm')
        u_email = request.POST.get('email')
        u_mobile = request.POST.get('mobile')
        u_rooms = request.POST.get('rooms')
        u_persons  = request.POST.get('persons')
        u_checkin = request.POST.get('checkin')
        u_checkout = request.POST.get('checkout')

        obj.name = u_name
        obj.email = u_email
        obj.mobile = u_mobile
        obj.rooms = u_rooms
        obj.persons = u_persons
        obj.checkin = u_checkin
        obj.checkout = u_checkout
        obj.save()

        return redirect('/display/')


    context = {
        'data' : obj
    }
    return render(request, 'app1/update.html',context)


def delete_view(request, u_id):
    obj = Booking_info.objects.get(id = u_id)

    if request.method=='POST':
            obj.delete()
            return redirect('/display/')

    context = {
        'data' : obj
    }
    
    return render(request, 'app1/delete.html',context)

def galary_view(request):
     return render(request, 'app1/galary.html')

def rooms_view(request):
     return render(request, 'app1/rooms.html')

def about_view(request):
     return render(request, 'app1/aboutus.html')

def contact_view(request):
     return render(request, 'app1/contact.html')

