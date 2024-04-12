from django import forms


class QuantumNumberForm(forms.Form):
    quantum_number = forms.IntegerField(
        label="n",
        min_value=0,
        max_value=9,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "n",
                "class": "custom-input",
            }
        ),
    )
