# Librairie_Django
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/LombaAnderson/Librairie_Django/blob/main/LICENSE)

# Sobre o projeto
O projeto Librairie_Django é uma API de cadastro e gerenciamento de pacientes onde há a preocupação de disponibilizar uma plataforma de agendamentos e históricos de pacientes. Minha mãe trabalhou muitos anos em clínicas e hospitais e algumas vezes acompanhava seu trabalho, sei o quanto é importante ter um software semelhante ao que foi desenvolvido aqui com o poderoso Framework Django REST que permite a construção de APIs Rest utilizando o Django e nos coloca na "cara do gol" em relação à APIs. Inicialmente, para criar djangoAPI-clinica se configurou tudo o que foi implementado em um terminal. Nele é instalado o ambiente virtual Python e em seguida o Django.
Houve a preocupação em organizar os 'apps' na criação das pastas e demais funcionalidades de agendamentos, pacientes e histórico. O 'app' pacientes tem a funcionalidade de editar, cadastrar,incluir e apagar novo paciente. Dentro de pacientes é preciso criar uma pasta chamada api onde são incluídos mais dois arquivos: serializers.py e viewsets.py onde foi desenvolvida a API em si. Em todos além de seguir o mesmo que foi explicado sobre o 'app' anterior, é necessário a estruturação do 'models.py'.
Houve essencialmente a preocupação de testar tudo o que foi feito em três tipos de testes diferentes. O primeiro foi o teste manual, depois com a utilização do software Insomnia e por último foram realizados testes unitários.  Foi instalado e configurado o Python decouple por motivo de segurança, caso haja algum intrave no momento de analisar o projeto fornecerei a chave de acesso.

## Imagem da
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/145520946-99122343-e0f7-425c-b78f-2df14ce928be.png" width="700" />
</div>

# Tecnologias utilizadas
- Python
- API Django Rest
-Django==4.0
-django-admin==2.0.1
-django-excel-base==1.0.4
-django-excel-response2==3.0.2
-django-six==1.0.4
-djangorestframework==3.12.4

# Testes unitários e manual
- Python

# Instruções para compilar, testar e rodar o projeto

```bash
# Clonar repositório
git clone https://github.com/LombaAnderson/Librairie_Django

# Criação e acesso da pasta do projeto
-mkdir librairie
-cd clinica

# Criação do ambiente de desenvolvimento do Python
-python -m venv venv

# Ativar o ambiente de desenvolvimento(venv)
-source venv/Scripts/activate

# Instalação do Django (Atenção: instalar somente após a ativação da venv)
-pip install django

# Instalação do pacote do Django Rest Framework
-pip install django djangorestframework
 
# Comando de criação do projeto
-django-admin startproject librairie .

# Criação do servidor
-python manage.py runserver

# Instalação do pytz(timezone)
pip install pytz

# Acesso ao servidor Django
http://127.0.0.1:8000/

# Apps 
-django-admin startapp livres

# Preparação das migrations
- python manage.py makemigrations

# Envio das migrations configuradas para o banco de dados
- python manage.py migrate

```

# Autor

Anderson Lomba de Oliveira

Linkedin

https://www.linkedin.com/in/anderson-lomba-140279142/

Portfólio

https://www.lombanderson.epizy.com

# Agradecimentos

Agradeço ao meu Deus que sempre me ajuda e a minha esposa que amo muito! Agradeço também ao professor Wagner que explicou muito bem o funcionamento de uma API rest Django



