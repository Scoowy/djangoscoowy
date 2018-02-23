from django.forms import ModelForm
from django import forms
from .models import Post

TOPIC_CHOICES = (
    ('general', 'Consulta General'),
    ('bug', 'Reportar Bug'),
    ('sugestion', 'Suggestion'),
)


class ContactanosForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES, label='Tema')
    mensaje = forms.CharField(
        widget=forms.Textarea, initial="Remplaza esto con tu Comentario o sugerencia", label='Comentario o sugerencia')
    nombre = forms.CharField(
        max_length=40, required=False, label='Nombre')
    sender = forms.EmailField(required=False, label='Correo electronico')
