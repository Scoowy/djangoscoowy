from django import forms

TOPIC_CHOICES = (
    ('general', 'Consulta General'),
    ('bug', 'Reportar Bug'),
    ('sugestion', 'Suggestion'),
)


class ContactanosForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    mensaje = forms.CharField(widget=forms.Textarea)
    nombre = forms.CharField(max_length=40, required=False)
    sender = forms.EmailField(required=False)
