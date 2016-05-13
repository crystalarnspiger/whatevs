from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings

from number_one import forms, models, utilities


# @utilities.audit_error
def models_practice(request):
    greeting = 'practice'
    manage_people = forms.PersonForm
    context = {
        'greeting': greeting,
        'manage_people': manage_people,
    }

    people = models.Person.objects.all()
    context['people'] = people

    return render(request, 'number_one/models_practice.html', context)


# @utilities.audit_error
def new_person(request):
    form = forms.PersonForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        error = form.errors
        context = {
            'exception_message': error
        }
        return render(request, 'number_one/error.html', context)

    return redirect('models_practice:practice')


# @utilities.audit_error
def update_person(request, nn_id=''):
    person = models.Person.objects.get(nn_id==nn_id)
    context = {
        'person_name': person.name
    }

    return redirect('models_practice:practice')

