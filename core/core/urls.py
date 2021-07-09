"""core URL Configuration

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
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("app/", include("app.urls")),
    path('assets/', include('assets.urls')),
    path('storage/', include('storage.urls')),
    path('servers/', TemplateView.as_view(template_name='assets/servers.html')),
    path('reports/', include('reports.urls')),
    path('snippets/', include('snippets.urls')),
    path('polls/', include('polls.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

admin.site.site_title = "NMS"
admin.site.site_header = "NMS Admin"