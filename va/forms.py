from django import forms
from .models import VerbalAutopsy

class VerbalAutopsyForm(forms.ModelForm):
    class Meta:
        model = VerbalAutopsy
        fields = "__all__"
        
        widgets = {
            "deceased_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "sex": forms.Select(
                attrs={"class": "form-control"}
            ),
            "age_at_death": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "date_of_death": forms.DateInput(
                attrs={"class": "form-control"}
            ),
            "place_of_death": forms.Select(
                attrs={"class" : "form-control"}
            ),
            "respondent_name": forms.TextInput(
                attrs={"class" : "form-control"}
            ),
            "respondent_relationship": forms.TextInput(
                attrs={"class" : "form-control"}
            ),
            "interview_date": forms.DateInput(
                attrs={"class" : "form-control"}
            ),
            "symptoms": forms.Textarea(
                attrs={"class" : "form-control"}
            ),
            "probable_cause_of_death": forms.TextInput(
                attrs={"class" : "form-control"}
            ),
        }