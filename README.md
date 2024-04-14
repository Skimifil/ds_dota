## Ideia
Coleta as informações da API da [OpenDota](https://api.opendota.com) para avaliar os times de Dota 2 em campeonatos.

## Fluxo
1. Conecta na API
2. Através dos endpoints, coleta as informações dos times, sendo:
   - Jogos
   - Times
   - Jogadores
   - Heróis
3. Armazena em um banco de dados
4. Através de um Notebook Jupyter, faz a analise com Machine Learning


## Pré-reqs
É preciso ter uma banco de dados MySQL para armazenamento dos dados. Criei um 'docker-compose.yml' para subir um MySQL no Docker pra facilitar o trabalho em teste e homologação.

Com o banco funcional, crie o arquivo 'config.py' dentro da pasta 'src/' e adicione o trecho abaixo no arquivo (caso queira trocar os dados de acesso, lembre-se de avaliar o 'docker-compose.yml' também).

```shell
MYSQL_CONFIG = {
    'MYSQLUSER': 'myuser',
    'MYSQLPASSWORD': 'mypassword',
    'MYSQLSERVER': '172.19.0.2',
    'MYSQLDB': 'dota_tournaments',
}
```

## Endpoints de referência na API
Open Dota API - https://docs.opendota.com/#section/Introduction

- proMatches
- proPlayers
- teams
- teamsMatches
- teamPlayers
- teamHeroes
