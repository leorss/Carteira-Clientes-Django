from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.urls import path
from django.urls import include
from cadastros import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('vendedor', VendedorViewSet)
router.register('cliente', ClienteViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('cadastros/', include('cadastros.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

