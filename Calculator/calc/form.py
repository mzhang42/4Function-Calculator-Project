from django.forms.forms import Form
from .models import Calculation
from django import forms

class CalculationForm(forms.ModelForm):
    class Meta:
       model = Calculation
       fields = ['num_one', 'num_two']
    calculation_type = forms.IntegerField(widget=forms.Select(
    choices=[(0, "+"), (1, "-"), (2, "*"), (3, "/")]))
    def clean(self):
        operat = self.cleaned_data.get('calculation_type')
        divisor = self.cleaned_data.get('num_two')
        if(operat == 3 and int(divisor) == 0 ):
            self.add_error('num_two', "Cannot divide by zero")

