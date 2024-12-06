from random import randint
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from usuarios.models import Usuario
from twilio.rest import Client
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, View
import requests
from requests.auth import HTTPBasicAuth
from django.contrib.auth.hashers import make_password

account_sid = 'AC096ee1b976f85bdb4bc7921fda390e39'
auth_token = '1fe587a5c6ce629ada1356cdbcfc6a33'
service_sid = 'VA1b015b5419fadce8ef5fdc1cc5f23915' 
twillio_number = '+14173101228'

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "auth/login.html"
    success_url = "/gestor/empreendimentos/"

    def get_success_url(self):
        return self.request.GET.get("next", self.success_url)

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if user.tipo_usuario == "GESTOR":
            success_url = reverse("gestores:empreendimentos")
        elif user.tipo_usuario == "CLIENTE":
            success_url = reverse("clientes:empreendimentos")
        elif user.tipo_usuario == "ASSOCIADO":
            success_url = reverse("associados:empreendimentos")
        else:
            success_url = self.success_url
        return redirect(success_url)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("usuarios:login-usuario")


def enviar_codigo_sms(numero_telefone):
    """Envia um código de verificação SMS via Twilio Verify."""
    verification = client.verify.services(service_sid).verifications.create(
        to=numero_telefone,
        channel='sms'
    )
    return verification.status


def verificar_codigo_sms(numero_telefone, codigo, password):
    usuarios = Usuario.objects.filter(codigo_verificacao=codigo)
    is_valid = usuarios.count() > 0

    if is_valid:
        usuario = usuarios.first()
        usuario.password =  make_password(password) 
        usuario.codigo_verificacao = None
        usuario.save()
    
    return is_valid


class RecuperaSenhaView(View):
    def get(self, request):
        return render(request, "auth/recuperar-senha.html")

    def post(self, request):
        url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'

        verification_code = f"{randint(1000, 9999)}"

        telefone_input = request.POST.get("telefone")
        telefone = "+55" + telefone_input.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")

        usuarios = Usuario.objects.filter(telefone=telefone_input)        

        if usuarios.count() > 0:
            usuario = usuarios.first()
            usuario.codigo_verificacao = verification_code
            usuario.save()

            data = {
                'To': telefone,
                'From': twillio_number,
                'Body': f"Olá {usuario.nome_sobrenome}, seu código de verificação: {verification_code}"
            }

            response = requests.post(url, data=data, auth=HTTPBasicAuth(account_sid, auth_token))
            if response.status_code == 201:
                messages.success(request,"Seu código de verificação foi enviado com sucesso!")
            return redirect("usuarios:verificar_codigo")


        return redirect("usuarios:recupera-senha-usuario")


class VerificarCodigoView(View):
    def get(self, request):
        return render(request, "auth/verificar-codigo.html")

    def post(self, request):
        codigo = request.POST.get("codigo")
        password = request.POST.get("senha")

        print(password)

        if codigo != "":
            is_valid = verificar_codigo_sms(None, codigo, password)

            if is_valid:
                messages.success(request, "Seu Codigo foi validado com sucesso!")
            
            if is_valid == False:
                messages.error(request, "Seu Codigo esta incorreto!")

            return redirect("usuarios:login-usuario")
