from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
   
   path('',views.index , name="marcador de posición para mostrar todas las encuestas creadas"),
   path('new',views.new, name='marcador de posición para que los usuarios agreguen una nueva encuesta')
]
