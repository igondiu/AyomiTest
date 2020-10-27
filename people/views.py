from django.urls import reverse
from django.views.generic import CreateView
from .models import Person
from django.views.generic import UpdateView
from people.forms import PersonForm
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'people/person_update_form.html'


class PersonCreateView(CreateView):
    model = Person
    fields = ('last_name', 'first_name', 'email', 'job_title', 'bio')

    def get_success_url(self):
        return reverse('show_or_modify', kwargs={'person_email': self.object.email})


class PersonLoginView(CreateView):
    model = Person
    fields = ('email',)
    template_name = 'people/login.html'

    def get_success_url(self):
        return reverse('show_or_modify', kwargs={'person_email': self.object.email})


def person_show_modify(request, person_email):
    try:
        the_person = Person.objects.get(email=person_email)
        data = {"user": the_person}
    except:
        data = {"user": ""}

    return render(request, 'people/show_modify.html', data)
