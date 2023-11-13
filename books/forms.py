from django import forms
from .models import *

class BookSearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100)

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content', 'pdf_file']
