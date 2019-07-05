from django import forms
from django.core import validators
from compobulator_app.models import Mp_archetype, Mp_element

class mp_archetype_model_form(forms.ModelForm):
    class Meta:
        model = Mp_archetype
        fields = '__all__'

    def clean(self):
        all_clean_data = super().clean()

class mp_element_model_form(forms.ModelForm):
    class Meta:
        model = Mp_element
        fields = '__all__'

    def clean(self):
        all_clean_data = super().clean()
