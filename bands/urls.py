from django.urls import path, include
from . import views

from rest_framework import routers
from bands.api import viewsets as bandviewsets
from rest_framework.documentation import include_docs_urls

route = routers.DefaultRouter()
route.register(r'band', bandviewsets.BandViewSet, basename="Bands")


urlpatterns = [
    path("", views.render_bands, name="render_bands"),
    path("band_admin", views.index, name="index"),
    path("band_admin/add", views.add_band, name="add_band"),
    path("band_admin/get", views.get_bands, name="get_bands"),
    path("band_admin/delete", views.delete_bands, name="delete_bands"),
    path("band_admin/edit", views.edit_bands, name="edit_bands"),
    path("band_admin/edit_band", views.edit_band, name="edit_band"),
    path("agendar", views.schedule_band, name="schedule_band"),
    path("api-bands/", include(route.urls)),
    path('api-bands/docs/', include_docs_urls(title='API Documentation')),
]