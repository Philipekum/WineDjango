from django import forms


class ElementsInput(forms.Form):
    fixed_acidity = forms.FloatField(min_value=4.6)
    volatile_acidity = forms.FloatField(min_value=0.12)
    citric_acid = forms.FloatField(min_value=0.0, max_value=1.0)
    residual_sugar = forms.FloatField(min_value=0.9, max_value=15.5)
    chlorides = forms.FloatField(min_value=0.012, max_value=0.611)
    free_sulfur_dioxide = forms.FloatField(min_value=1.0, max_value=68.0)
    total_sulfur_dioxide = forms.FloatField(min_value=6.0, max_value=289.0)
    density = forms.FloatField(min_value=0.99, max_value=1.003)
    ph = forms.FloatField(min_value=2.74, max_value=4.01)
    sulphates = forms.FloatField(min_value=0.33, max_value=2.0)
    alcohol = forms.FloatField(min_value=8.4, max_value=14.9)

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        initial['fixed_acidity'] = 8.31
        initial['volatile_acidity'] = 0.53
        initial['citric_acid'] = 0.26
        initial['residual_sugar'] = 2.53
        initial['chlorides'] = 0.08
        initial['free_sulfur_dioxide'] = 15.61
        initial['total_sulfur_dioxide'] = 45.91
        initial['density'] = 0.99
        initial['ph'] = 3.31
        initial['sulphates'] = 0.65
        initial['alcohol'] = 10.44

        kwargs['initial'] = initial
        super(ElementsInput, self).__init__(*args, **kwargs)