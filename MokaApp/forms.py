from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class cuidador_formulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    zona= forms.CharField(max_length=30)
    
class mascota_formulario(forms.Form):   
    nombre_mascota = forms.CharField(max_length=30)
    codigo_mascota = forms.IntegerField()
    email_dueño= forms.EmailField()
    zona = forms.CharField(max_length=30)

class reserva_formulario(forms.Form):
    numero_reserva = forms.IntegerField() 
    nombre_reserva= forms.CharField(max_length=30)
    fecha_reserva = forms.DateField()  
    confirmacion = forms.BooleanField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
            model = User
            fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

