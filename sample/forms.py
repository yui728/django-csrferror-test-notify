from django import forms
from .models import Sample

class SampleForm(forms.ModelForm):
    """サンプルフォーム"""
    class Meta:
        model = Sample
        fields = ('message')
        widgets = {
            'messsage': forms.Textarea(attrs={'placeholder': 'メッセージ'})
        }