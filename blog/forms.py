from django import forms

class requestForm(forms.Form):
    title = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={"placeholder":'Title'})
    )
    context = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Enter Context"}))