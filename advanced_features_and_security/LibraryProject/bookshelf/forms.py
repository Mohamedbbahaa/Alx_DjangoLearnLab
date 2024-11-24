from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=True)

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, help_text="Enter the title of the book.")
    author = forms.CharField(max_length=100, required=True, help_text="Enter the author's name.")
    published_date = forms.DateField(required=False, help_text="Enter the published date (YYYY-MM-DD).")
