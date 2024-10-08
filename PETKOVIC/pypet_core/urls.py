
from django.contrib import admin
from django.urls import path, include
from django.conf import settings                
from django.conf.urls.static import static      

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('divulgar/', include('divulgar.urls')),
    path('adotar/', include('adotar.urls')),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = 'PyPet - Sistema de Adocão de Pets'    

admin.site.site_title = 'PyPet'                                          

admin.site.index_title = 'PyPet'                                    


