# 🗂️ My Enginner -  Sistema de Anúncios Imobiliários

![Python](https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![License](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Versão](https://img.shields.io/badge/versão-1.0-blue)

---

## 📌 Descrição
O **My Enginner** é uma aplicação web simples e intuitiva para anúncios imobiliários diários, desenvolvida com **Python**, **Django** e **Bootstrap**.  

O sistema permite que usuários façam novos anúncios de forma eficiente através de um **CRUD completo de anúncios**.

---

## 📖 Detalhes
Este projeto foi desenvolvido com o objetivo de **praticar conceitos de desenvolvimento web fullstack**, como:  
- Integração entre **frontend e backend**  
- Persistência de dados com **ORM e PostgreSQL**  
- Templates dinâmicos com **Django**  

É ideal para **equipes que desejam centralizar seus anúncios de imóveis em um ambiente simples e eficiente**. 

## ✨ Funcionalidades

### ✅ CRUD Completo

**Create**  
Adicionar novos anúncios com título, descrição, preço, endereço, e fotos.

**Read**  
Visualizar a lista de todos os anúncios cadastrados.

**Update**  
Editar informações de anúncios existentes.

**Delete**  
Remover anúncios concluídos ou indesejados.

---

## 🚀 Tecnologias Utilizadas

**Backend**
- Python
- Django

**Frontend**
- HTML5
- Bootstrap 5

**Banco de Dados**
- PostgreSQL (Desenvolvimento)

**Outros**
- Bootstrap Icons
- Git
- GitHub

---

## 📌 Campos do Anúncio

| Camada         | Tecnologias /Ferramentas                |
|----------------|----------------------------|
| Backend        | Python, Django             |
| Frontend       | HTML5, CSS3, Javascript    | 
| UI / Estilo    | Bootstrap                  | 
| Banco de Dados | PostgreSQL                 |

---

## 📁 Estrutura do Projeto

my_enginner/
├── manage.py
├── requirements.txt
├── .gitignore
├── anuncios/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Modelo Task
│ ├── views.py # Funções salvar, lista, editar, deletar
│ ├── urls.py # Rotas da aplicação
│ ├── migrations/
│ └── templates/
│ ├── base.html
│ └── criar_anuncio.html
| ├── detalhe_anuncio.html
| ├── edit.html
| ├── home.html
└── config/
├── init.py
├── settings.py
├── urls.py
└── wsgi.py


---

# 🖥️ Como Executar o Projeto

## Pré-requisitos

- Python 3.8+
- Git
- PostgreSQL (opcional)

---

## ⚙️ Instalação e Execução

```bash
# 1. Clone o repositório
git clone https://github.com/JhonataLuis/my_enginner.git

# 2. Entre na pasta do projeto
cd my_enginner

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Ative o ambiente virtual

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Execute as migrações
python manage.py migrate

# 7. Inicie o servidor
python manage.py runserver

# 8. Acesse no navegador
👉 http://127.0.0.1:8000

🔄 Rotas da Aplicação

| URL                  | Método     | Função  | Descrição              |
| -------------------- | ---------- | ------- | ---------------------- |
| `/`                  | GET        | lista   | Lista todas os anúncios|
| `/criar/`            | POST       | salvar  | Cria novo anúncio      |
| `/detalhes/`         | GET        | salvar  | Detalhes novo anúncio  |
| `/editar/<int:id>/`  | GET / POST | editar  | Edita anúncio          |
| `/delete/<int:id>/`  | GET        | deletar | Remove anúncio         |

🔑 Funcionalidades

✅ Lista de Anúncios

Visualização em tabela com todas as tarefas e seus status.

✅ Criação de Anuncio

Formulário simples para cadastro de novos anúncios.

✅ Edição

Formulário preenchido automaticamente para atualização de dados.

✅ Exclusão

Remoção com confirmação para evitar exclusões acidentais.

🤝 Contribuições

Contribuições são sempre bem-vindas!

Faça um fork do projeto

Crie uma branch para sua feature

git checkout -b feature/nova-feature

Commit suas mudanças

git commit -m "Adiciona nova feature"

Envie para sua branch

git push origin feature/nova-feature

Abra um Pull Request

👨‍💻 Autor

Jhonata Luis

💼 LinkedIn: https://www.linkedin.com/in/jhonataluisdesenvolvedorjava/

🐙 GitHub: https://github.com/JhonataLuis
