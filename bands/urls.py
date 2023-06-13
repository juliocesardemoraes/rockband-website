from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_band, name="add_band"),
    path("get", views.get_bands, name="get_bands"),
    path("delete", views.delete_bands, name="delete_bands"),
    path("edit", views.edit_bands, name="edit_bands"),
    path("edit_band", views.edit_band, name="edit_band"),
]