from django import forms

from .models import Items, TmaRequests


class ItemsForm(forms.ModelForm):
   class Meta:
        model = Items
        fields = ['item_group',
                  'unit_of_measurement',
                  'quantity',
                  'price_without_vat',
                  'status',
                  'storage_location',
                  'contact_person']

class DenyRequestForm(forms.ModelForm):
    class Meta:
        model = TmaRequests
        fields = ['comment',
                  'status']
        exclude = ['status']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_group',
                  'unit_of_measurement',
                  'quantity',
                  'price_without_vat',
                  'status']
        exclude = ['status']