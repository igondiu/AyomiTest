from django.views.generic import CreateView
from .models import Person
from django.views.generic import UpdateView
from people.forms import PersonForm


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'people/person_update_form.html'


class PersonCreateView(CreateView):
    model = Person
    fields = ('last_name', 'first_name', 'email', 'job_title', 'bio')


class PersonLoginView(CreateView):
    model = Person
    fields = 'email'
