from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
   # path('admin/', admin.site.urls),
   
   
   path('',views.root),
   path('/',views.index),
   path('/new',views.new),
   path('/create',views.create),
   path('/<int:val>',views.show),
   path('/<int:val>/edit',views.edit),
   path('/json',views.json)
   
   ]
   