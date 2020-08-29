from django import forms


class ContactForm(forms.Form):
    """ Form for contact page - sent with emailjs """

    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 8,
            },
        ),
    )


class Meta:

    fields = [
            'name',
            'email',
            'message',
        ]
