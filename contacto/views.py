from .forms import FormularioContacto
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from smtplib import SMTP

# Create your views here.

def enviarCorreo(asunto, mensaje):

    message = 'Subject: {}\n\n{}'.format(asunto, mensaje)

    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login("bravomartin178@gmail.com", "avenged sevenfold")
    smtp.sendmail("bravomartin178@gmail.com", "bravomartin178@gmail.com", message)
    smtp.quit()

def contacto(request):

    formulario_contacto=FormularioContacto()

    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            # email=EmailMessage("Mensaje de Web Django", 
            # "El usuario {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre, email1, contenido), 
            # "", ["bravomartin178@gmail.com"], reply_to=[email1])

            asunto = "Mensaje de la Web Django"
            mensaje="El usuario {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido)

            # infoForm=formulario_contacto.cleaned_data
            try:
            #     send_mail('Mensaje de Web Django', 'El usuario {} con la direccion {} escribe lo siguiente:\n\n {}'.format(nombre, email, contenido), '', ['bravomartin178@gmail.com'],)
                # email.send()
                enviarCorreo(asunto, mensaje)

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
