from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Band


def index(request):
    bands = Band.objects.all()
    url = request.build_absolute_uri('/bands/add')
    return render(request, "create_band.html",{'bands': bands, 'url': url})

def edit_bands(request):
    id = request.GET.get('q', '')
    band = Band.objects.get(id=id)
    url = request.build_absolute_uri('/bands/edit_band')
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
    
    return redirect("/bands")

def add_band(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    price = request.POST.get('price')
    image_link = request.POST.get('image_link')
    band = Band(name=name, email=email, phone=phone, price=price, image_link=image_link)
    band.save()
    return redirect("/bands")

def get_bands(request):
    bands = Band.objects.all()
    print(bands)
    return bands

def delete_bands(request):
    id = request.GET.get('q', '')
    Band.objects.filter(id=id).delete()
    return redirect("/bands")
