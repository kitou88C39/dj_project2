from django import froms
from .models import Club, Deparment

class SearchForm(froms.Form):
    club = forms.ModelChoiceField(
        queryset=Club.object, label='サークル', required=False)
    
    department = forms.ModelChoiceField(
        queryset=Deparment.objects, label='部署', required=False)
    