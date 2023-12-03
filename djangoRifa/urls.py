
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from miApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index,),
    path('comprar/<int:id>', views.comprar, name='comprar'),
    path('ticket/<int:id>', views.Ticket, name='ticket'),
    path('detallepremio/<int:rifas_id>/', views.detalle_premio, name='detalle_premio'),
    path('sorteo/', views.sorteo, name='sorteo'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$',serve, {
            'document_root':settings.MEDIA_ROOT,
        })
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)