"""
URL configuration for edDjSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from games.views import *
from edDjSite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('games.urls')),
    path('user/', include('users.urls')),
    path('api/v1/', include('games.API.urls')),
    path('api/v1/', include('users.API.urls'))


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')),]


handler404 = pageNotFound
