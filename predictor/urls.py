from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),          # Homepage
    path("predict/", views.predict_image, name="predict"),  # <-- add this!
]
