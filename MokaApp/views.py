from django.shortcuts import render
from MokaApp.models import Mascotas, Cuidadores,Reservas 
from MokaApp.forms import cuidador_formulario, mascota_formulario, reserva_formulario,UserRegisterForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def about(request):
      return render(request,"MokaApp/about.html")

@login_required
def inicio(request):
      return render(request, "MokaApp/inicio.html")


def mascota(request):
      return render(request, "MokaApp/mascotas.html")
def reserva(request):
      return render(request, "MokaApp/reservas.html")

def mascotas(request):
      if request.method == 'POST':
            formulario = mascota_formulario(request.POST) #aquí me llega toda la información del html
            print(formulario)
            if formulario.is_valid:   #Si pasó la validación de Django
                  informacion = formulario.cleaned_data
                  mascota = Mascotas(nombre_mascota=informacion['nombre_mascota'], codigo_mascota=informacion['codigo_mascota'],
                  email_dueño=informacion['email_dueño'], zona=informacion['zona']) 
                  mascota.save()
                  return render(request, "MokaApp/inicio.html") #Vuelvo al inicio
      else: 
            formulario= mascota_formulario() #Formulario vacio para construir el html
      return render(request, "MokaApp/mascotas.html", {"formulario":formulario})

def cuidadores(request):
      if request.method == 'POST':
            formulario = cuidador_formulario(request.POST) #aquí me llega toda la información del html
            print(formulario)
            if formulario.is_valid:   #Si pasó la validación de Django
                  informacion = formulario.cleaned_data
                  cuidador = Cuidadores(nombre=informacion['nombre'], apellido=informacion['apellido'],
                  email=informacion['email'], zona=informacion['zona']) 
                  cuidador.save()
                  return render(request, "MokaApp/inicio.html") #Vuelvo al inicio
      else: 
            formulario= cuidador_formulario() #Formulario vacio para construir el html
      return render(request, "MokaApp/cuidadores.html", {"formulario":formulario})

def reservas(request):
      if request.method == 'POST':
            formulario = reserva_formulario(request.POST) #aquí me llega toda la información del html
            print(formulario)
            if formulario.is_valid:   #Si pasó la validación de Django
                  informacion = formulario.cleaned_data
                  reserva = Reservas(numero_reserva=informacion['numero_reserva'], nombre_reserva=informacion['nombre_reserva'],
                  fecha_reserva=informacion['fecha_reserva'], confirmacion=informacion['confirmacion']) 
                  reserva.save()
                  return render(request, "MokaApp/inicio.html") #Vuelvo al inicio
      else: 
            formulario= reserva_formulario() #Formulario vacio para construir el html
      return render(request, "MokaApp/reservas.html", {"formulario":formulario})

def info_cuidadores(request):
      cuidadores = Cuidadores.objects.all() #trae todos los cuidadores
      contexto= {"cuidadores":cuidadores} 
      return render(request, "MokaApp/info_cuidadores.html",contexto)

def info_mascotas(request):
      mascotas = Mascotas.objects.all() #trae todas las mascotas
      contexto= {"mascotas":mascotas} 
      return render(request, "MokaApp/info_mascotas.html",contexto)

def info_reservas(request):
      reservas = Reservas.objects.all() #trae todas las reservas
      contexto= {"reservas":reservas} 
      return render(request, "MokaApp/info_reservas.html",contexto)

def buscar(request):
      if  request.GET["numero_reserva"]:
            numero_reserva = request.GET['numero_reserva'] 
            reservas = Reservas.objects.filter(numero_reserva__exact=numero_reserva)
            return render(request, "MokaApp/inicio.html", {"reservas":reservas, "numero_reserva":numero_reserva})
      else:
            respuesta = "No enviaste datos"
      return render(request, "MokaApp/inicio.html", {"respuesta":respuesta})



def eliminar_cuidador(request, cuidador_nombre):
      cuidadores = Cuidadores.objects.get(nombre=cuidador_nombre)
      cuidadores.delete()
      # vuelvo al menú
      cuidadores = Cuidadores.objects.all()  # trae todos los cuidadores
      contexto = {"cuidadores": cuidadores}
      return render(request, "MokaApp/info_cuidadores.html", contexto)

def editar_cuidador(request, cuidador_nombre):
    cuidadores = Cuidadores.objects.get(nombre=cuidador_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # info html
        formulario = cuidador_formulario(request.POST)
        print(formulario)
        if formulario.is_valid:  # Si pasó la validación de Django

            informacion = formulario.cleaned_data

            cuidadores.nombre = informacion['nombre']
            cuidadores.apellido = informacion['apellido']
            cuidadores.email = informacion['email']
            cuidadores.zona = informacion['zona']

            cuidadores.save()
            return render(request, "MokaApp/inicio.html")
    # En caso que no sea post
    else:
        formulario = cuidador_formulario(initial={'nombre': cuidadores.nombre, 'apellido': cuidadores.apellido,
                                                   'email': cuidadores.email, 'profesion': cuidadores.zona})

    # Voy al html que me permite editar
    return render(request, "MokaApp/editar_cuidadores.html", {"formulario": formulario, "cuidador_nombre": cuidador_nombre})

def eliminar_mascota(request, mascota_nombre):
      mascotas = Mascotas.objects.get(nombre_mascota=mascota_nombre)
      mascotas.delete()
      # vuelvo al menú
      mascotas = Mascotas.objects.all()  # trae todos los cuidadores
      contexto = {"mascotas": mascotas}
      return render(request, "MokaApp/info_mascotas.html", contexto)

def editar_mascota(request, mascota_nombre):
    mascotas = Mascotas.objects.get(nombre_mascota=mascota_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # info html
        formulario = mascota_formulario(request.POST)
        print(formulario)
        if formulario.is_valid:  # Si pasó la validación de Django

            informacion = formulario.cleaned_data

            mascotas.nombre_mascota = informacion['nombre_mascota']
            mascotas.codigo_mascota = informacion['codigo_mascota']
            mascotas.email_dueño = informacion['email_dueño']
            mascotas.zona = informacion['zona']

            mascotas.save()
            return render(request, "MokaApp/inicio.html")
    # En caso que no sea post
    else:
        formulario = mascota_formulario(initial={'nombre_mascota': mascotas.nombre_mascota, 'codigo_mascota': mascotas.codigo_mascota,
                                                   'email_dueño': mascotas.email_dueño, 'zona': mascotas.zona})

    # Voy al html que me permite editar
    return render(request, "MokaApp/editar_mascotas.html", {"formulario": formulario, "mascota_nombre": mascota_nombre})

def eliminar_reserva(request, reserva_nombre):
      reservas = Reservas.objects.get(nombre_reserva=reserva_nombre)
      reservas.delete()
      # vuelvo al menú
      reservas = Reservas.objects.all() 
      contexto = {"reservas": reservas}
      return render(request, "MokaApp/info_reservas.html", contexto)

def editar_reserva(request, reserva_nombre):
    reservas = Reservas.objects.get(nombre_reserva=reserva_nombre)
    if request.method == 'POST':
        # info html
        formulario = reserva_formulario(request.POST)
        print(formulario)
        if formulario.is_valid:  # Si pasó la validación de Django

            informacion = formulario.cleaned_data

            reservas.numero_reserva = informacion['numero_reserva']
            reservas.nombre_reserva = informacion['nombre_reserva']
            reservas.fecha_reserva = informacion['fecha_reserva']
            reservas.confirmacion = informacion['confirmacion']

            reservas.save()
            return render(request, "MokaApp/inicio.html")
    # En caso que no sea post
    else:
        formulario = reserva_formulario(initial={'numero_reserva': reservas.numero_reserva, 'nombre_reserva': reservas.nombre_reserva,
                                                   'fecha_reserva': reservas.fecha_reserva, 'confirmacion': reservas.confirmacion})

    # Voy al html que me permite editar
    return render(request, "MokaApp/editar_reservas.html", {"formulario": formulario, "reserva_nombre": reserva_nombre})

#login,logout,signin
def register(request):

      if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"MokaApp/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
                   
            form = UserRegisterForm()     

      return render(request,"MokaApp/registro.html" ,  {"form":form})

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "MokaApp/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "MokaApp/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "MokaApp/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "MokaApp/login.html", {"form": form})


def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':

        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "MokaApp/inicio.html",{"mensaje": "Usuario editado correctamente!"})

    else:

        formulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "MokaApp/editar_perfil.html", {"formulario": formulario, "usuario": usuario})







      
      