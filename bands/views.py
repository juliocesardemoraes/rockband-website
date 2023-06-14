from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Band
import datetime

def render_bands(request):
    bands = Band.objects.all()
    url = request.build_absolute_uri('/')
    return render(request, "landing_page.html",{'bands': bands, 'url': url})


def index(request):
    bands = Band.objects.all()
    url = request.build_absolute_uri('/band_admin/add')
    return render(request, "create_band.html",{'bands': bands, 'url': url})

def edit_bands(request):
    id = request.GET.get('q', '')
    band = Band.objects.get(id=id)
    url = request.build_absolute_uri('/band_admin/edit_band')
    return render(request, "edit_band.html",{'band': band, 'edit': True, 'url': url, 'id': id})

def edit_band(request):
    id = request.GET.get('q', '')
    band_to_be_updated = get_object_or_404(Band, pk=id)

    band_to_be_updated.name = request.POST.get('name')
    band_to_be_updated.email = request.POST.get('email')
    band_to_be_updated.phone = request.POST.get('phone')
    band_to_be_updated.price = request.POST.get('price')
    band_to_be_updated.image_link = request.POST.get('image_link')

    band_to_be_updated.save(update_fields=["name", "email", "phone", "price", "image_link"])
    
    return redirect("/band_admin")

def add_band(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    price = request.POST.get('price')
    image_link = request.POST.get('image_link')
    band = Band(name=name, email=email, phone=phone, price=price, image_link=image_link)
    band.save()
    return redirect("/band_admin")

def get_bands(request):
    bands = Band.objects.all()
    print(bands)
    return bands

def delete_bands(request):
    id = request.GET.get('q', '')
    Band.objects.filter(id=id).delete()
    return redirect("/band_admin")

def schedule_band(request):
    id = request.GET.get('q', '')
    band = Band.objects.get(id=id)
    date_now =  datetime.datetime.now()
    date_formatted = date_now.strftime("%x")
    print(date_formatted)
    url = request.build_absolute_uri('/')
    ### "2018-07-22" ###
    date_formatted_new = date_now.strftime("%Y") + '-' + date_now.strftime("%m") + '-' + date_now.strftime("%d")

    return render(request, "schedule_show.html",{'band': band, 'url': url,  'date': date_formatted_new})

