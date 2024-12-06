from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("", view=views.LoginFormView.as_view(), name="login-usuario"),
    path("login/", views.LoginFormView.as_view(), name="login-usuario"),
    path("sair/", views.LogoutView.as_view(), name="logout-usuario"),
    path("recupera-senha/", views.RecuperaSenhaView.as_view(), name="recupera-senha-usuario"),
    path("verificar-codigo/", views.VerificarCodigoView.as_view(), name="verificar_codigo"),
]
