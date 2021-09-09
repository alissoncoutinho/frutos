Crie uma pasta para manter seu código e acessando essa pasta em um terminal, crie um ambiente virtual com o seguinte comando:
python3 -m venv ./venv

Ative seu ambiente virtual com o seguinte comando (MAC e Linux):
source venv/bin/activate

Em caso de Windows, utilize o comando:
venv\Scripts\activate.batCOPIAR CÓDIGO

Instale o Django nesse ambiente virtualizado:
pip install django

Crie um projeto chamado setup utilizando o Django admin, para manter toda configuração de nossa aplicação:
django-admin startproject setup .

Para finalizar a configuração do ambiente, na pasta setup, altere no arquivo settings.py o idioma e o horário que usaremos na aplicação, incluindo as seguintes linhas de código:
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'COPIAR CÓDIGO

RODAR O SERVIDOR:
py manage.py runserver

usuário: alisson
senha do admin do django: abc123456

comando para criar o Script de banco de dados ao alterar a model:
python manage.py makemigrations
comando para rodar o script criado acima:
python manage.py migrate

