# RockBandWebsite :guitar:

Este é um projeto sobre uma site de agendamento de shows de banda de rock.

# Como rodar :computer:

P.S - ```É necessário ter o python instalado```

0 - Instale os requisitos

    pip install -r requirements.txt

1 - Va no seu terminal e digite para rodar o programa:

    python manage.py runserver

2 - Fazer migrations:

    python manage.py makemigrations bands
    python manage.py migrate

3 - Testes no shell:

    python manage.py shell

4 - Rota da api:

    http://127.0.0.1:8000/api-bands/
    http://127.0.0.1:8000/api-bands/band/

# Objetivos da tarefa :white_check_mark:

- [x] Utilizar Django
- [x] Utilizar padrões de projeto: Model, View e Template
- [x] No mínimo 3 classes de modelo
- [x] Utilizar, no mínimo um exemplo de tela customizado
- [x] Utilizar bootstrap e site admin do Django
- [x] Criar um API com REST que liste a classe principal do exemplo

# Extras :100:

- [x] Criamos uma rota de admin própria. Com uma estilização própria http://127.0.0.1:8000/band_admin
- [x] Não utilizamos Bootstrap. Estilização feita com css "puro". O que dá mais trabalho.
- [x] Conventional commits. Padrão de nomenclatura de commit.
- [x] Criação de documentação da api. 


# URLS IMPORTANTES

    http://127.0.0.1:8000/api-bands/docs/
    http://127.0.0.1:8000/api-bands/band/
    http://127.0.0.1:8000/band_admin
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/admin/
