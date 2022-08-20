from website.models import Person
from django import forms

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('age', 'health', 'employed', 'businessOwner', 'married', 'homeOwner', 'renting', 'student', 'haveChildren')
        widgets = {
            'age': forms.NumberInput(attrs={'class': '_someclass', 'id': 'someid'}),
        }