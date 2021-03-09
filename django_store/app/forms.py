from django import forms


class OrderForm(forms.Form):
    qty = forms.IntegerField(min_value=1)
    customerName = forms.CharField()
    customerPhone = forms.CharField()
    customerAdress = forms.CharField()
