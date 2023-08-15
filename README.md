Distribuição carteira de clientes para novos vendedores
=======================================================

<div align="center">
  <img width="150" src="./static/cadastros/images/cerveja.png">
</div>

### Este sistema tem por objetivo gerenciar e distribuir a carteira de clientes para os novos vendedores de acordo com a geolocalização.

* * *

Ambientação
-----------

#### Criar ambiente virtual

```
virtualenv venv
```


#### Ativar ambiente virtual (Linux)

``` 
source ./venv/bin/activate 
```

#### Ativar ambiente virtual (Windows)

``` 
./venv/bin/activate 
```

#### Instalar requerimentos

``` 
pip install -r requirements.txt 
```

Execução
--------

#### Executar migrate

``` 
python manage.py migrate 
```

#### Criar super user

``` 
python manage.py createsuperuser 
```

#### Alimentar base de dados
```
python populate.py
```

#### Rodar servidor


```
python manage.py runserver
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
