from django import forms


class ElementsInput(forms.Form):
    fixed_acidity = forms.FloatField(min_value=4.6, max_value=15.9)
    volatile_acidity = forms.FloatField(min_value=0.12, max_value=1.58)
    citric_acid = forms.FloatField(min_value=0.0, max_value=1.0)
    residual_sugar = forms.FloatField(min_value=0.9, max_value=15.5)
    chlorides = forms.FloatField(min_value=0.012, max_value=0.611)
    free_sulfur_dioxide = forms.FloatField(min_value=1.0, max_value=68.0)
    total_sulfur_dioxide = forms.FloatField(min_value=6.0, max_value=289.0)
    density = forms.FloatField(min_value=0.99, max_value=1.003)
    ph = forms.FloatField(min_value=2.74, max_value=4.01)
    sulphates = forms.FloatField(min_value=0.33, max_value=2.0)
    alcohol = forms.FloatField(min_value=8.4, max_value=14.9)
