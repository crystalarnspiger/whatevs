from django.shortcuts import render
from django.conf import settings

from number_one import forms, models, utilities


# @utilities.audit_error
def models_practice(request):
    greeting = 'practice'
    form1 = forms.PersonForm
    context = {
        'greeting': greeting,
        'form1': form1,
    }
    if request.POST:
        form1 = forms.PersonForm(request.POST)
        if form1.is_valid():
            form1.save()

    people = models.Person.objects.all()
    context['people'] = people

    return render(request, 'number_one/models_practice.html', context)
