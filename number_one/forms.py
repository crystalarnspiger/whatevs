from django import forms

from number_one import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['nn_id', 'name']

