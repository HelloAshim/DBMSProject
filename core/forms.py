from django import forms
from .models import *


class SchoolForm(forms.ModelForm):

    class Meta:
        # specify model to be used
        model = School
 
        # specify fields to be used
        fields = [
            "name",
            'title',
        ]


class DepartmentForm(forms.ModelForm):

    class Meta:
        # specify model to be used
        model = Department
 
        # specify fields to be used
        fields = [
            "name",
            'title',
            'school',
        ]

