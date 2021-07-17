from blogs.views import new
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
   
   path('register',views.register,name="marcador de posición para que los usuarios creen un nuevo registro de usuario"),
   path('login', views.login, name="marcador de posición para que los usuarios inicien sesión"),
   path('new',views.register),
   path('',views.users, name="marcador de posición para luego mostrar toda la lista de usuarios")

   
]
