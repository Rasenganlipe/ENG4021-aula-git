"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from FanClub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('album/criar/', views.forms_albuns),
    path('musica/criar/', views.forms_musicas),
    path('album/edit/<album_id>', views.update_album),
    path('album/delete/<album_id>', views.delete_album),
    path('musica/edit/<musica_id>', views.update_musica),
    path('musica/delete/<musica_id>', views.delete_musica),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
