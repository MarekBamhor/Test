from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Homepage"),
    path("about/", views.about, name="About me"),
    path("plans/", views.plans, name="Plans"),
    path("famtree/", views.famtree, name="Family tree app"),
    path("contact/", views.contact, name="Contact"),
]
