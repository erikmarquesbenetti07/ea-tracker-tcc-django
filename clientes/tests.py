from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario
from empreendimentos.models import Empreendimento

class ClienteTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(email="cliente@email.com", password="12345678")
        self.empreendimento =  Empreendimento.objects.create(
            id=1,
            nome="Empreendimento teste",
            previsao_entrega="2025-01-01",
        )
        
        self.client = Client()
        self.client.login(username="cliente@email.com", password="12345678")


    def test_url_cliente_empreendimento_list(self):
        route = reverse("clientes:empreendimentos-list")
        self.assertEqual(route, "/cliente/empreendimentos/")


    def test_url_cliente_empreendimento_detail(self):
        self.assertEqual(
            reverse("clientes:empreendimento-detail", kwargs={"pk": self.empreendimento.id}),
            f"/cliente/empreendimento/detalhar/{self.empreendimento.id}/"
        )

    def test_url_cliente_associado_list(self):
        route = reverse("clientes:associados")
        self.assertEqual(route, "/cliente/associados/")


    def test_url_cliente_associado_update(self):
        self.assertEqual(
            reverse("clientes:associado-update", kwargs={"pk": self.user.id}),
            f"/cliente/associado/atualizar/{self.user.id}/"
        )


    def test_cliente_associado_create(self):
        response = Usuario.objects.create_user(email="associado@email.com", password="12345678")
        self.assertEqual(response.email, "associado@email.com")


    def test_cliente_associado_update(self):
        Usuario.objects.filter(id=1).update(email="associado2@email.com")
        response = Usuario.objects.filter(id=1).first()
        self.assertEqual(response.email, "associado2@email.com")
