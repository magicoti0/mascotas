from django import forms
from .models import Persona, Animal, Consulta, Medicina
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre','apellido','apellido','direccion','telefono',)

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('idTipoAnimal', 'idDueno', 'nombreAnimal','fechaNacimiento','raza','sexo','peso','observaciones','imagen')

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('idAnimal','sintomas','observaciones','diagnostico','fechaConsulta','receta')

    def __init__ (self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        self.fields["receta"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["receta"].queryset = Medicina.objects.all()

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']