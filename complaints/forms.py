from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = [
            'asset',
            'description',
            'photo'
        ]


class ComplaintStatusForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            'status'
        ]