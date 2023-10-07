from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Homepage"),
    path("about/", views.about, name="About me"),
    path("plans/", views.plans, name="Plans"),
    path("payme/", views.payme, name="Pay me"),
    path("contact/", views.contact, name="Contact"),
]
