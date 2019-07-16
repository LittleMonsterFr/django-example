from django import forms
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

from example.places.models import Place


class CityForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ("coordinates", "city_hall")
        widgets = {
            'coordinates': GooglePointFieldWidget,
            'city_hall': GoogleStaticOverlayMapWidget,
        }