from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
   # path('admin/', admin.site.urls),
   
   
   path('blogs',views.root ),
   path('/',views.index ,name='marcador de posición para luego mostrar una lista de todos los blogs'),
   path('/new',views.new, name='marcador de posición para mostrar un nuevo formulario para crear un nuevo blog'),
   path('/create',views.create),
   path('/<int:val>',views.show , name='marcador de posición para mostrar el número de blog: {val}'),
   path('/<int:val>/edit',views.edit , name='marcador de posición para editar el blog {{val}}'),
   path('/json',views.json)
   
   ]
   