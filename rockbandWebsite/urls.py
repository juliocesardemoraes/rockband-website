from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("bands/", include("bands.urls")),
    path("admin/", admin.site.urls),
]