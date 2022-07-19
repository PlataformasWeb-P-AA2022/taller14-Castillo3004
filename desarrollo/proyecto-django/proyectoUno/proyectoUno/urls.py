from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from rest_framework import routers
from administrativo import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'propietario', views.PropietarioViewSet)
router.register(r'departamento', views.DepartamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]