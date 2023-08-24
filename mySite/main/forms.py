from django import forms
from .models import list_item

class ItemForm(forms.ModelForm):

  class Meta:
    model = list_item
    fields = "__all__"

