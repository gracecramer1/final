from django import forms
from .models import Name, Topping


class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ["text"]
        labels = {"text": ""}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ["text"]
        labels = {"text": ""}
        # a widget is an html form element, such as a singleline text box,
        # mult-line text area, or drop-down list.
        # customize the input widget for the field 'text' so the text area
        # will be 80 columns wide instead of the default 40
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
