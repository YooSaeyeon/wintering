from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('list/', include('list.urls'), name='list'),
    path('music/', include('music.urls'), name='music'),
]
