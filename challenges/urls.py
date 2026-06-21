from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("<int:month>",views.number_challenge),
    path("<str:month>",views.challenge,name="monthly_challenges"),
]