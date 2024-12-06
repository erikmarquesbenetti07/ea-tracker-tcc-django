from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario
from empreendimentos.models import Empreendimento


class GestorTeste(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(email="gestor@email.com", password="12345678")
        self.empreendimento =  Empreendimento.objects.create(
            id=1,
            nome="Empreendimento teste",
            previsao_entrega="2025-01-01",
        )
        
        self.client = Client()
        self.client.login(username="gestor@email.com", password="12345678")


    def test_url_gestor_empreendimento_list(self):
        route = reverse("gestores:empreendimentos")
        self.assertEqual(route, "/gestor/empreendimentos/")


    def test_url_gestor_empreendimento_create(self):
        route = reverse("gestores:empreendimento-create")
        self.assertEqual(route, "/gestor/empreendimento/cadastrar/")


    def test_url_gestor_empreendimento_update(self):
        self.assertEqual(
            reverse("gestores:empreendimento-update", kwargs={"pk": self.empreendimento.id}),
            f"/gestor/empreendimento/atualizar/{self.empreendimento.id}/"
        )


    def test_url_gestor_cliente_list(self):
        route = reverse("gestores:clientes")
        self.assertEqual(route, "/gestor/clientes/")


    def test_url_gestor_cliente_update(self):
        self.assertEqual(
            reverse("gestores:cliente-update", kwargs={"pk": self.user.id}),
            f"/gestor/cliente/atualizar/{self.user.id}/"
        )


    def test_gestor_empreendimento_create(self):
        response = Empreendimento.objects.create(
            nome="Empreendimento teste",
            previsao_entrega="2025-01-01",
        )
        self.assertEqual(response.nome, "Empreendimento teste")


    def test_gestor_empreendimento_update(self):
        Empreendimento.objects.filter(id=1).update(nome="Empreendimento teste 2")
        response = Empreendimento.objects.filter(id=1).first()
        self.assertEqual(response.nome, "Empreendimento teste 2")


    def test_gestor_cliente_create(self):
        response = Usuario.objects.create_user(email="cliente@email.com", password="12345678")
        self.assertEqual(response.email, "cliente@email.com")


    def test_gestor_cliente_update(self):
        Usuario.objects.filter(id=1).update(email="cliente2@email.com")
        res = Usuario.objects.filter(id=1).first()
        self.assertEqual(res.email, "cliente2@email.com")

