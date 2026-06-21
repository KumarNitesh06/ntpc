from django import forms
from .models import Asset
from django import forms
from .models import Department, Building

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name']


class BuildingForm(forms.ModelForm):

    class Meta:
        model = Building
        fields = ['name']

class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset

        fields = [
            'item_id',
            'item_name',
            'category',
            'department',
            'building'
        ]