from django import forms
from django.db.models import fields

from .models import Student


class StudentForm(forms.ModelForm):
    # first_name=forms.CharField(label="Your Name")
    class Meta:
        model = Student
        # fields = ["first_name", "last_name", "number"]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = "My Name"


# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=100, label="Your Name")
#     last_name = forms.CharField(max_length=100, label="Your Surname")
#     number = forms.IntegerField(required=False)
