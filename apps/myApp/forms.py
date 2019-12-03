from django import forms


class LoadFile(forms.Form):
    """
    Formulario para subir un archivo
    """
    process_file = forms.FileField(required=True, label='Archivo',
                                   widget=forms.ClearableFileInput())
