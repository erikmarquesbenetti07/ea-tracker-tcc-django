from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


class LoginGestorMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.tipo_usuario != "GESTOR":
            logout(request)
            return redirect("usuarios:login-usuario")
        return super().dispatch(request, *args, **kwargs)


class LoginClienteMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.tipo_usuario != "CLIENTE":
            logout(request)
            return redirect("usuarios:login-usuario")
        return super().dispatch(request, *args, **kwargs)


class LoginAssociadoMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.tipo_usuario != "ASSOCIADO":
            logout(request)
            return redirect("usuarios:login-usuario")
        return super().dispatch(request, *args, **kwargs)
