from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('home', views.index, name='index'),
    path('save_rsvp', views.save_rsvp, name='save_rsvp'),
]