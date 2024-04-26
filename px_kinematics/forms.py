from django import forms


class FreeFallForm(forms.Form):
    distance = forms.FloatField(label="distance", min_value=0)
    velocity = forms.FloatField(label="velocity", min_value=0)
