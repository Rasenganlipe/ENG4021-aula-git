A primeira coisa necessária para o seu site, é configurar a "SECRET_KEY", já que é a base para todo o funcionamento do Django. Para configurá-la, você deve ir em secrets, nomear a key de "SECRET_KEY" e colocar o value correspondente. Para pegá-lo você deve dar os seguintes comandos na shell:
>python
>import secrets
>secrets.token_urlsafe(32)
Depois, dê "run" na aplicação.
A seguir, você deve ciar um app, através do seguinte comando:
>python3 manage.py startapp <nomedoapp> (coloque o nome desejado)
A seguir é necessário criar um superuser para seu servidor. Para o superuser utilizamos os seguintes comandos:
>python manage.py createsuperuser
Coloque em ordem o username desejado, o endereço de e-mail, a senha e a confirmação da senha. Siga o exemplo a seguir
>Username: admin
>Email address: admin@example.com
>Password: (senha desejada)
>Password (again): (senha desejada)
Ao aparecer a mensagem "Superuser created successfully", significa que você conseguiu criar o superuser, a seguir basta dar o comando:
>python manage.py runserver
A partir de agora, basta acessar o “/admin/” no fim do link que você irá ter acesso a "Tela de login de admin". Colocando seu username e senha, você acessará a página de admin.
Por fim, após de criar suas classes no models.py , você precisa migrar os models. Para isso, use o comando:
>python manage.py makemigrations
>python manage.py migrate
Pronto, o seu Django agora está configurado!