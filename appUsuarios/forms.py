from django import forms
from .models import Persona

class FormularioPersona(forms.ModelForm):
   """
   Representa al formulario 
   """
   class Meta:
       model = Persona
       fields = ('nombre', 'apellidos', 'rut', 'sexo', 'email', 'contacto')
