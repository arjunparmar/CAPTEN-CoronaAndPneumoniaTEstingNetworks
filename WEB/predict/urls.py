from django.contrib import admin
from django.urls import path
from .  import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'predict'

urlpatterns = [
    path('form/',views.formpage,name = 'form'),
    path('predict/', views.predict_menu,name = 'menu')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)