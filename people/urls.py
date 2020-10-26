"""People URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonCreateView.as_view(), name='home'),
    path('person_update_form.html', views.PersonUpdateView.as_view()),
]
