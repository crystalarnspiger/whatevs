from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings

from number_one import forms, models, utilities


@utilities.audit_error
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


@utilities.audit_error
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


@utilities.audit_error
def enter_update(request, id=''):
    update = forms.UpdateForm
    person = models.Person.objects.get(nn_id=id)
    print person.nn_id
    context = {
        'person_name': person.name,
        'person_nn_id': person.nn_id,
        'update': update,
    }
    print (context)

    return render(request, 'number_one/update_form.html', context)


@utilities.audit_error
def save_update(request):
    form = forms.UpdateForm(request.POST)
    if form.is_valid():
        person = form.save(commit=False)
        changed_person = models.Person.objects.get(nn_id=request.POST['id'])
        changed_person.name = person.name
        changed_person.save()
    else:
        error = form.errors
        context = {
            'exception_message': error
        }
        return render(request, 'number_one/error.html', context)

    return redirect('models_practice:practice')