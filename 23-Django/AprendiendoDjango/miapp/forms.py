from django import forms
from django.core import validators

class FormArticle(forms.Form):
    
    title = forms.CharField(
        label="Titulo",
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete el titulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'el titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ+´ ]*$','Usas caracteres invalidos','invalid_title')
        ]
    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea(
            attrs={
                'placeholder':'Ingresa el contenido',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100,'Demasiados Caracteres')
        ]
    )

    
    
    public = forms.ChoiceField(
        label="¿Deseas publicarlo?",
        choices = [
            (1,'Si' ),
            (0,'No')
        ],
        widget=forms.RadioSelect,
        initial=1
    )
