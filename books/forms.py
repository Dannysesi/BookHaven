from django import forms
from .models import *

class BookSearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100)

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pub_date', 'isbn', 'contributors', 'image']