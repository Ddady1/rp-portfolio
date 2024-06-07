#book/forms.py

from django import forms

class SearchBook(forms.Form):
    bookname = forms.TextInput()
    author = forms.CharField()
