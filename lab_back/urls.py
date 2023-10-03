"""
URL configuration for lab_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuarioLogin, UsuarioLogout, UsuarioRegistro

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    # path('api/v3/register/', UsuarioRegistro.as_view(), name='register'),
    path('api/v3/login/', UsuarioLogin.as_view(), name='login'),
    path('api/v3/logout/', UsuarioLogout.as_view(), name='logout'),


    path('', include('usuarios.urls',)),
    path('api/v3/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('', include('laboratorios.urls',)),
    path('', include('reservas.urls',)),
    path('admin/', admin.site.urls),
]
