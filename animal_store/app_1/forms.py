from django import forms


from .models import Animal


class EntryForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ('animalName', 'category', 'imageURl', 'status', 'image', 'tags')