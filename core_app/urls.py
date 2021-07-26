from django.urls import path
from core_app import views
from core_app.apps import CoreAppConfig

app_name = CoreAppConfig.name

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
