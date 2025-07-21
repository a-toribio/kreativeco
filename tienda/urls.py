from django.urls import path
from tienda import views

urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
    # otras urls...
]
