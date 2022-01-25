<h1 align="center"> Distribuição carteira de clientes para novos vendedores </h1>
<div align="center">
  <img width="150" src="./static/cadastros/images/cerveja.png">
</div>
<h3> Este sistema tem por objetivo gerenciar e distribuir a carteira de clientes para os novos vendedores de acordo com a geolocalização. </h3>
<hr> 
<h2 style="padding: 10px 0px">Ambientação</h2>

<h4>Criar ambiente virtual</h4>

```
virtualenv venv
```

<h4 style="padding: 10px 0px">Ativar ambiente virtual (Linux)<h4>

```
source ./venv/bin/activate
```

<h4 style="padding: 10px 0px">Ativar ambiente virtual (Windows)<h4>

```
./venv/bin/activate
```

<h4 style="padding: 10px 0px">Instalar requerimentos<h4>

```
pip install -r requirements.txt
```

<h2 style="padding: 10px 0px">Execução</h2>

<h4 style="padding: 10px 0px">Executar migrate<h4>

```
python manage.py migrate
```

<h4 style="padding: 10px 0px">Criar super user<h4>

```
python manage.py createsuperuser
```

<h4 style="padding: 10px 0px">Alimentar base de dados<h4>

```
python populate.py
```

<h4 style="padding: 10px 0px">Rodar servidor<h4>

```
python manage.py runserver
```

<br>
<hr>

<h2 style="padding: 10px 0px"> Visão Geral </h2>

<h3> Tela Login </h3>
<img src="./static/cadastros/images/snapshots/login.jpg">

<br>

<h3> Tela Bem-vindo(a) </h3>
<img src="./static/cadastros/images/snapshots/bem-vindo.jpg">

<br>

<h3> Tela Clientes </h3>
<img src="./static/cadastros/images/snapshots/cliente.jpg">

<br>

<h3> Tela Vendedores </h3>
<img src="./static/cadastros/images/snapshots/vendedor.jpg">

<br>

<h3> Tela Edição </h3>
<img src="./static/cadastros/images/snapshots/edição.jpg">