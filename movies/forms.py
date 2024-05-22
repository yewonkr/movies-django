
from django import forms
from django.forms import ModelForm
from .models import Actress

class ActressForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActressForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Actress
        fields = ['__all__']



    # name = forms.CharField(max_length=25)
    # enName = forms.CharField(max_length=50)
    # birth = forms.IntegerField(null=True)
    # height = forms.CharField(max_length=5, null=True)
    # debut = forms.CharField(max_length=10, null=True)
    # info = forms.TextField(null=True, default="NO DATA")


