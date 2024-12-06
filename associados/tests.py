from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario
from empreendimentos.models import Empreendimento

class AssociadoTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(email="associado@email.com", password="12345678")
        self.empreendimento =  Empreendimento.objects.create(
            id=1,
            nome="Empreendimento teste",
            previsao_entrega="2025-01-01",
        )
        
        self.client = Client()
        self.client.login(username="associado@email.com", password="12345678")


    def test_url_associado_empreendimento_list(self):
        route = reverse("associados:empreendimentos-list")
        self.assertEqual(route, "/associado/empreendimentos/")


    def test_url_associado_empreendimento_detail(self):
        self.assertEqual(
            reverse("associados:empreendimento-detail", kwargs={"pk": self.empreendimento.id}),
            f"/associado/empreendimento/detalhar/{self.empreendimento.id}/"
        )
