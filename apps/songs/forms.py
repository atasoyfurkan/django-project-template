from django import forms
from .models import Song
from django.contrib.admin import widgets


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100, widget=widgets.AdminFileWidget)


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
        widgets = {"name": widgets.AdminTextInputWidget}
