from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from . import views 

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
]