from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
