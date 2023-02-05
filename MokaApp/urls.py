from django.urls import path
from MokaApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('mascotas', views.mascotas, name="Mascotas"),
    path('cuidadores', views.cuidadores, name="Cuidadores"),
    path('reservas', views.reservas, name="Reservas"),
    path('info_cuidadores', views.info_cuidadores, name = "Info Cuidadores"),
    path('info_mascotas', views.info_mascotas ,name = "Info Mascotas"),
    path('info_reservas', views.info_reservas, name = "Info Reservas"),
    path('eliminar_cuidadores/<cuidador_nombre>/', views.eliminar_cuidador, name="EliminarCuidador"),
    path('editar_cuidadores/<cuidador_nombre>/', views.editar_cuidador, name="EditarCuidador"),
    path('buscar/', views.buscar),
    path('eliminar_mascotas/<mascota_nombre>/', views.eliminar_mascota, name="EliminarMascota"),
    path('editar_mascotas/<mascota_nombre>/', views.editar_mascota, name='EditarMascota'),
    path('eliminar_reservas/<reserva_nombre>/', views.eliminar_reserva, name="EliminarReserva"),
    path('editar_reservas/<reserva_nombre>/', views.editar_reserva, name='EditarReserva'),
    path('login',views.login_request, name="Login"),
    path('registro', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='MokaApp/logout.html'), name='logout'),
    path('editar_perfil', views.editar_perfil, name="EditarPerfil"),
    path('about', views.about, name="AboutMe")
    

]   