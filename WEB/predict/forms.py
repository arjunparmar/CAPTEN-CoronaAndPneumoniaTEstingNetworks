from django import forms
from .models import Image
# from .models import segment

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields =  '__all__'

class TempForm(forms.Form):
    select_choices = [
        ('yes','Yes'),
        ('no','No')
    ]
    predictIt = forms.CharField(label = "Click button to predict", widget = forms.RadioSelect(choices = select_choices))

