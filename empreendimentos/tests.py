from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario
from empreendimentos.models import Empreendimento


class EmpreendimentoTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(email="usuarioteste@email.com", password="12345678")
        self.empreendimento =  Empreendimento.objects.create(
            id=1,
            nome="Empreendimento teste",
            previsao_entrega="2025-01-01",
        )
        
        self.client = Client()
        self.client.login(username="usuarioteste@email.com", password="12345678")


    # def test_url_gestor_empreendimento_list(self):
    #     route = reverse("gestores:empreendimentos")
    #     self.assertEqual(route, "/gestor/empreendimentos/")


    # def test_url_gestor_empreendimento_create(self):
    #     route = reverse("gestores:empreendimento-create")
    #     self.assertEqual(route, "/gestor/empreendimento/cadastrar/")


    # def test_url_gestor_empreendimento_update(self):
    #     self.assertEqual(
    #         reverse("gestores:empreendimento-update", kwargs={"pk": self.empreendimento.id}),
    #         f"/gestor/empreendimento/atualizar/{self.empreendimento.id}/"
    #     )

    # def test_url_gestor_empreendimento_detail(self):
    #     self.assertEqual(self.empreendimento.nome, "Empreendimento teste")

    def test_create_empreendimento(self):
        response = Empreendimento.objects.create(
            # id=1,
            nome="Empreendimento teste",
            previsao_entrega="2025-01-01",
        )
        # self.assertEquals(response.get_absolute_url(), '/empreendimento/atualizar/1/')
        # self.assertEqual(Empreendimento.objects.count(), 2)  # Verifica se o empreendimento foi criado
        self.assertEqual(response.nome, 'Empreendimento teste')

    # def test_date_of_death_label(self):
    #     author=Author.objects.get(id=1)
    #     field_label = author._meta.get_field('date_of_death').verbose_name
    #     self.assertEquals(field_label, 'died')

    # def test_first_name_max_length(self):
    #     author = Author.objects.get(id=1)
    #     max_length = author._meta.get_field('first_name').max_length
    #     self.assertEquals(max_length, 100)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     author = Author.objects.get(id=1)
    #     expected_object_name = f'{author.last_name}, {author.first_name}'
    # #     self.assertEquals(expected_object_name, str(author))

    # def test_get_absolute_url(self):
    #     author = Usuario.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEquals(author.get_absolute_url(), '/catalog/author/1')
