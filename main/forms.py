from django import forms

class DiseaseDetectionForm(forms.Form):
    symptoms = forms.CharField(widget=forms.Textarea)