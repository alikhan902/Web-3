from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  # Главная страница
    path('about/', include('about.urls')),  # Страница "О нас"
    path('ice_cream/', include('ice_cream.urls')),  # Страница мороженого
]