from django import forms
from .models import Sample

class SampleForm(forms.ModelForm):
    """サンプルフォーム"""
    class Meta:
        model = Sample
        fields = ('message',)
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'メッセージ'})
        }