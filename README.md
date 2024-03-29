Distribuição carteira de clientes para novos vendedores
=======================================================

<div align="center">
  <img width="150" src="./static/cadastros/images/cerveja.png">
</div>

### Este sistema tem por objetivo gerenciar e distribuir a carteira de clientes para os novos vendedores de acordo com a geolocalização.

* * *
Tecnologias
-----------
- Python
- Django
- SQL Lite

Ambientação
-----------

#### Criar ambiente virtual

```
python -m virtualenv venv
```

#### Ativar ambiente virtual (Windows)

``` 
./venv/Scripts/activate
```

#### Instalar requerimentos

``` 
pip install -r requirements.txt
```

Instalação
--------

#### Executar migrate

``` 
python manage.py migrate 
```

#### Criar super user

``` 
python manage.py createsuperuser 
```

#### Popular base de dados
```
python populate.py
```

Execução
--------

#### Rodar servidor


```
python manage.py runserver
```

Acesso Usuário
```
http://127.0.0.1:8000
```

Acesso Administrador
```
http://127.0.0.1:8000/admin
```

* * *

Visão Geral
-----------

### Tela Login

![](./static/cadastros/images/snapshots/login.jpg)  

### Tela Bem-vindo(a)

![](./static/cadastros/images/snapshots/bem-vindo.jpg)  

### Tela Clientes

![](./static/cadastros/images/snapshots/cliente.jpg)  

### Tela Vendedores

![](./static/cadastros/images/snapshots/vendedor.jpg)  

### Tela Edição

![](./static/cadastros/images/snapshots/edição.jpg)
