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
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [

    
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


    path('api/v3/login/', UsuarioLogin.as_view(), name='login'),
    path('api/v3/logout/', UsuarioLogout.as_view(), name='logout'),


    path('', include('usuarios.urls',)),
    path('api/v3/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('', include('laboratorios.urls',)),
    path('', include('reservas.urls',)),
    path('admin/', admin.site.urls),
]
