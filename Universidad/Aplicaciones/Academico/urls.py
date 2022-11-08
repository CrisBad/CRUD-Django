from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('editarEstudiante/<codigo>', views.editarEstudiante),
    path('edicionEstudiante/', views.edicionEstudiante),
    path('eliminarEstudiante/<codigo>', views.eliminarEstudiante)
]