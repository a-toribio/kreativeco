from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.

from .models import Producto

def inicio(request):
    return render(request, 'tienda/inicio.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos': productos})

def carrito(request):
    return render(request, 'tienda/carrito.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Envía el correo
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            send_mail(
                f'Mensaje de {nombre} - {email}',
                mensaje,
                email,
                [settings.EMAIL_HOST_USER],
            )
            return redirect('contacto')
            #return HttpResponse('Mensaje enviado correctamente, nos pondremos en contacto contigo pronto.')
    else:
        form = ContactForm()

    return render(request, 'tienda/contacto.html', {'form': form})
