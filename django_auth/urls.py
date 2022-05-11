
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from .views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),