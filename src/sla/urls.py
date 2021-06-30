from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assets/', include('assets.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

admin.site.site_title = "NMS"
admin.site.site_header = "NMS Admin"
