from django import forms

from number_one import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['nn_id', 'name']

    # def my_clean(self):
    #     errors = self.errors.as_data()
    #     if errors == {'nn_id': ValidationError([])}

