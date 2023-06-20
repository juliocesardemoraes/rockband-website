from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Band
import datetime

def render_bands(request):
    """
    Renders the landing page with a list of all bands.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: The rendered landing page with the list of bands.
    """
    bands = Band.objects.all()
    url = request.build_absolute_uri('/')
    return render(request, "landing_page.html", {'bands': bands, 'url': url})


def index(request):
    """
    Renders the band creation page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: The rendered band creation page.
    """
    bands = Band.objects.all()
    url = request.build_absolute_uri('/band_admin/add')
    return render(request, "create_band.html", {'bands': bands, 'url': url})

def edit_bands(request):
    """
    Renders the band editing page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: The rendered band editing page.
    """
    id = request.GET.get('q', '')
    band = Band.objects.get(id=id)
    url = request.build_absolute_uri('/band_admin/edit_band')
    return render(request, "edit_band.html", {'band': band, 'edit': True, 'url': url, 'id': id})

def edit_band(request):
    """
    Edits a specific band based on the provided request data.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: Redirects to the band administration page.
    """
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
    """
    Creates a new band based on the provided request data.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: Redirects to the band administration page.
    """
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    price = request.POST.get('price')
    image_link = request.POST.get('image_link')
    band = Band(name=name, email=email, phone=phone, price=price, image_link=image_link)
    band.save()
    return redirect("/band_admin")

def get_bands(request):
    """
    Retrieves all bands from the database.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - QuerySet: All bands in the database.
    """
    bands = Band.objects.all()
    return bands

def delete_bands(request):
    """
    Deletes a specific band based on the provided band ID.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: Redirects to the band administration page.
    """
    id = request.GET.get('q', '')
    Band.objects.filter(id=id).delete()
    return redirect("/band_admin")

def schedule_band(request):
    """
    Renders the page to schedule a band for a specific date.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: The rendered schedule page for the band.
    """
    id = request.GET.get('q', '')
    band = Band.objects.get(id=id)
    date_now = datetime.datetime.now()
    date_formatted = date_now.strftime("%x")
    url = request.build_absolute_uri('/')
    date_formatted_new = date_now.strftime("%Y") + '-' + date_now.strftime("%m") + '-' + date_now.strftime("%d")

    return render(request, "schedule_show.html", {'band': band, 'url': url, 'date': date_formatted_new})
