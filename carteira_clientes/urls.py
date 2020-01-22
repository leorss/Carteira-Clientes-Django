from django.contrib import admin
from django.urls import path
from django.urls import include
from cadastros import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('cadastros/', include('cadastros.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

