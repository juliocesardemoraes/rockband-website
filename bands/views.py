from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Band


def index(request):
    bands = Band.objects.all()
    print(bands)
    return render(request, "base.html",{'bands': bands})

def add_band(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    price = request.POST.get('price')
    image_link = request.POST.get('image_link')
    band = Band(name=name, email=email, phone=phone, price=price, image_link=image_link)
    band.save()
    print('Banda: ', band)
    return redirect("/bands")

def get_bands(request):
    bands = Band.objects.all()
    print(bands)
    return bands
    # band_list = []
    # for band in bands:
    #     band_list.append(band)
    # return band_list

def delete_bands(request):
    id = request.GET.get('q', '')
    Band.objects.filter(id=id).delete()
    return redirect("/bands")
