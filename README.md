# **EA Tracker - Sistema de Gestão de Empreendimentos**

**EA Tracker** é uma solução inovadora para o setor imobiliário, projetada para facilitar o gerenciamento de empreendimentos, melhorar a comunicação entre construtoras e clientes, e fornecer uma visão completa do progresso das obras. Com recursos avançados e integração com APIs externas, o sistema oferece uma experiência robusta e prática para todos os envolvidos.

---

## **Funcionalidades Principais**

### **Gestor**
- Gerenciamento de empreendimentos (cadastro, edição e exclusão).
- Atualização de status e progresso das obras.
- Upload de fotos e documentos relacionados ao empreendimento.
- Geração de relatórios detalhados.
- Visualização de estatísticas e gráficos interativos.

### **Cliente**
- Acompanhamento do progresso das obras em tempo real.
- Recebimento de notificações de marcos importantes.
- Linha do tempo interativa com o histórico de atualizações.
- Visualização de galeria de fotos e vídeos do empreendimento.

---

## **Tecnologias Utilizadas**

### **Backend**
- **Linguagem:** Python
- **Framework:** Django
- **APIs REST:** Django REST Framework
- **Banco de Dados:** SQLite

### **Frontend**
- **Linguagens:** HTML, CSS, JavaScript
- **Framework CSS:** Bootstrap

### **APIs Externas**
- **Twilio:** Envio de códigos de verificação por SMS para recuperação de senha.
- **ViaCEP:** Consulta e preenchimento automático de endereços com base no CEP.

---

## **Pré-requisitos**

Certifique-se de ter os seguintes requisitos instalados em seu ambiente:
- Python 3.11 ou superior.
- Virtualenv para criação de ambientes virtuais.
- Git para controle de versão.

---

## **Configuração do Projeto**

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/ea-tracker.git
   cd ea-tracker
   ```

2. **Crie um Ambiente Virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as Dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as Migrações do Banco de Dados**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o Servidor**
   ```bash
   python manage.py runserver
   ```

6. **Acesse a Aplicação**
   - No navegador, acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## **Configurações de APIs**

### **Twilio**
1. Crie uma conta no [Twilio](https://www.twilio.com/).
2. Obtenha os seguintes valores:
   - `ACCOUNT_SID`
   - `AUTH_TOKEN`
   - `SERVICE_SID`
3. Adicione essas credenciais no arquivo `.env`:
   ```
   TWILIO_ACCOUNT_SID=seu_account_sid
   TWILIO_AUTH_TOKEN=seu_auth_token
   TWILIO_SERVICE_SID=seu_service_sid
   ```

### **ViaCEP**
- Integração direta via endpoint público: [https://viacep.com.br/](https://viacep.com.br/).

---

## **Estrutura de Diretórios**

```plaintext
ea-tracker/
│
├── config/                # Configurações principais do projeto Django.
├── usuarios/              # Aplicação para autenticação e gestão de usuários.
├── gestores/              # Módulo para funcionalidades de gestores.
├── clientes/              # Portal do cliente para acompanhamento.
├── associados/            # Recursos para associados.
├── empreendimentos/       # Gerenciamento de empreendimentos.
├── dashboard/             # Painel administrativo com gráficos e relatórios.
├── templates/             # Arquivos HTML para renderização.
├── static/                # Arquivos estáticos (CSS, JS, imagens).
├── media/                 # Arquivos enviados pelos usuários.
└── requirements.txt       # Dependências do projeto.
```

---

## **Próximos Passos**

- **Integração com outras APIs:** Expandir as funcionalidades com novas integrações.
- **Melhorias na interface do cliente:** Tornar a experiência do usuário ainda mais fluida.
- **Compatibilidade mobile:** Desenvolver uma aplicação mobile para iOS e Android.

---

## **Contribuição**

Contribuições são bem-vindas! Siga os passos abaixo:
1. Faça um fork do repositório.
2. Crie uma nova branch.
   ```bash
   git checkout -b minha-feature
   ```
3. Envie suas alterações.
   ```bash
   git push origin minha-feature
   ```
4. Abra um Pull Request.

---

## **Licença**

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

## **Contato**

- Autor: [Erik Marques Benetti](erikmarquesbenetti07@gmail.com)
- Projeto no GitHub: [EA Tracker](https://github.com/vxrnxk/ea-tracker-tcc-django)

---
