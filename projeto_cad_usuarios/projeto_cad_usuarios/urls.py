
from django.urls import path
from app_cad_usuarios import views
urlpatterns = [
   #rota, view resposável, nome de referêcia
   #padaria.com
   path('',views.home,name='home'), 
    #padaria.com/usuarios
   path('usuarios/',views.usuarios,name='listagem_usuarios')
   
]