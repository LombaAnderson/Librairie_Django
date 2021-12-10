# Librairie_Django
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/LombaAnderson/Librairie_Django/blob/main/LICENSE)

# Sobre o projeto
O projeto Librairie_Django é uma API Django Rest framework onde se pode cadastrar nome, autor, ano que saiu o livro, seu estado, número de páginas e editora. Dessa forma é possível cadastrar os livros, apagá-los, deixá-los registrados. Inicialmente é preciso configurar o settings.py e em seguida é necessário criar as models onde ficarão todas as informações descritas acima. Foram feitos testes manuais e unitários para verificar se está tudo ok e utilizado python decouple com intuito de preservar a chave. Caso seja preciso fornecerei a chave. 

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
-cd librairie

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



