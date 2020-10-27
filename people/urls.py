"""People URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonLoginView.as_view(), name='login_register'),
    path('person_create', views.PersonCreateView.as_view(), name='register'),
    path('person_update/<int:pk>', views.PersonUpdateView.as_view(), name='update'),
    path('person_show_modify/<str:person_email>', views.person_show_modify, name='show_or_modify'),
]
