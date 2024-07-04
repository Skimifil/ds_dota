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

- leagues
- proMatches
- proPlayers
- teams
- teamsMatches
- teamPlayers
- teamHeroes

### Objetivos Gerais

1. **Entender o problema de negócio e identificar os elementos a serem considerados para o planejamento de um Modelo de Data Science:**
   - A ideia é entender quais fatores contribuem para o sucesso de uma equipe em torneios de Dota 2. Elementos a considerar incluem desempenho das equipes, estatísticas dos jogadores, resultados de partidas e características das ligas.

2. **Descrever os dados do problema e as relações entre dados através da Análise Exploratória de Dados:**
   - Isso envolve a coleta de dados das ligas, partidas, equipes e jogadores, seguida pela análise para identificar padrões, correlações e insights importantes. A análise exploratória de dados (EDA) ajudará a entender melhor a distribuição dos dados e as possíveis relações entre variáveis.
     - leagues:
       - Com as ligas, podemos entender o comportamento dos times e jogadores dependendo do tier da liga (amadora, profissional, etc).
     - proMatches:
       - Temos a visão das partidas oficiais de jogos profissionais, dados de duração da partida, dia e horário de começou, times jogando e qual ganhou.
     - proPlayers:
       - Temos as informações dos jogadores para fazer relação com as informações de partidas e ligas que ele(a) jogou.
     - teams:
       - Dados básicas, mas importantes, como vitórias e derrotas do time e o "rating" do time pode nos passar uma ideia de comparação com outros times.
     - teamsMatches:
       - Pegamos dados mais detalhados de partidades que houveram daquele time, duração, data e hora, quem era seu oponente e a liga.
     - teamPlayers:
       - Fazemos referência aos jogadores que estão e passarampor aquele time, entendendo quantos jogos tiveram e quantas vitórias.
     - teamHeroes:
       - Pegando dados de vitórias e quantidade de jogos com determinado herói dentro do jogo, podemos entender o desempenho do time com cada herói.

3. **Construir uma apresentação executiva mostrando os resultados obtidos:**
   - A apresentação deve incluir visualizações claras e concisas dos resultados da análise, insights importantes descobertos, e recomendações baseadas nos dados. Deve ser direcionada a um público executivo, destacando os pontos mais relevantes.
   #TODO - Ja é pra construir uma apresentação? Mas que resultados?

### Objetivos Específicos

1. **Desenvolver as instâncias de Data Acquisition e Data Wrangling em seu trabalho final:**
   - Isso inclui a configuração e utilização da OpenDota API para coletar dados e o processo de limpeza e transformação dos dados para que possam ser utilizados em análises posteriores.
   - Através das funções criadas, foi desenvolvido um código que conecta na API da OpenDora API e armazena em um banco de dados MySQL.

2. **Conseguir uma articulação em equipe e uma divisão de tarefas adequadas aos objetivos:**
   - Definir claramente os papéis e responsabilidades de cada membro da equipe para garantir que todas as partes do projeto sejam cobertas eficientemente.
   - Este projeto esta sendo feito de forma individual, apenas pelo Rafael P de Carvalho.
   * Tarefas:
     * Planejamento e Organização do Projeto
       * Definição do Problema e Objetivos do Projeto 
       * Configuração do Ambiente de Trabalho.
     * Coleta e Aquisição de Dados (Data Acquisition)
       * Conexão à OpenDota API
       * Download de Dados
     * Preparação e Limpeza dos Dados (Data Wrangling)
       * Criação do Banco de Dados
       * Inserção de Dados no Banco de Dados
       * Limpeza de Dados
     * Análise Exploratória de Dados (EDA)
       * Análise Univariada
       * Análise Bivariada
       * Análise Multivariada
     * Modelagem e Análise de Dados
       * Filtragem e Seleção de Dados
       * Modelagem Preditiva
     * Visualização e Apresentação dos Resultados
       * Criação de Visualizações
       * Preparação da Apresentação Executiva
     * Documentação e Relatório Final
       * Documentação do Projeto
       * Elaboração do Relatório Final
     * Revisão e Entrega
       * Revisão do Trabalho
       * Entrega do Projeto

3. **Realizar Filtragem:**
   - Aplicar técnicas de filtragem para isolar os dados mais relevantes para o estudo, como partidas de torneios específicos, jogadores profissionais, etc.
   #TODO - Eu pego tudo que vem da API, basicamente eu tiro o "lixo" ou é mais na hora da analise que faz essa filtragem?

4. **Descrever o que significa cada variável, como se comporta:**
   - Explicar o significado de cada variável coletada (ex: `match_id`, `start_time`, `radiant_team_id`, `dire_team_id`, etc.) e analisar seu comportamento através de estatísticas descritivas e visualizações.

5. **Especificar as distribuições e relações (gêneros, sexo, idade, tributação, tipo de empresa):**
   - Embora essas especificações sejam mais comuns em estudos demográficos, aqui podemos adaptar para incluir distribuições e relações como desempenho das equipes ao longo do tempo, estatísticas de vitórias/derrotas, distribuições de tempo de jogo, etc.

### Pontos de Entrega

1. **Apresentação da empresa ou problema específico:**
   - Introdução ao projeto e a OpenDota API, explicando a importância de analisar os dados de torneios de Dota 2 para entender os fatores de sucesso das equipes.

2. **Perguntas e objetivos da pesquisa:**
   - Quais fatores mais contribuem para o sucesso de uma equipe em torneios de Dota 2?
   - Como as estatísticas individuais dos jogadores influenciam os resultados das partidas?
   - Existem padrões ou tendências que podem prever o desempenho futuro de uma equipe?

3. **Configuração da equipe de trabalho:**
   - Descrever a composição da equipe, incluindo as funções de cada membro (ex: coleta de dados, análise, visualização, apresentação).

4. **Indicação da fonte do dataset e os critérios de seleção (Data Acquisition):**
   - Fonte: OpenDota API. Critérios de seleção podem incluir partidas de torneios, dados de jogadores profissionais e equipes, filtrados para incluir apenas partidas recentes de torneios principais.

5. **Geração do primeiro Data Wrangling e EDA, apontado seus dados (insights) univariados, bivariados e multivariados:**
   - Exemplo de insights univariados: Distribuição de durações de partidas.
   - Insights bivariados: Correlação entre a quantidade de vitórias e a pontuação média da equipe.
   - Insights multivariados: #TODO

6. **Análise de Componentes Principais:**
   - Utilizar PCA para reduzir a dimensionalidade dos dados e identificar as variáveis mais influentes no desempenho das equipes.

7. **Contar a história de seus dados:**
   - Criar uma narrativa em torno dos dados coletados e insights obtidos, mostrando como as análises podem ajudar a prever ou melhorar o desempenho das equipes em torneios futuros.

8. **Filtros aplicados aos dados. Distribuição. Dataset final para analisar:**
   - Detalhar os filtros aplicados, como a seleção de partidas de torneios específicos e a exclusão de dados irrelevantes. Apresentar a distribuição final dos dados após a filtragem.

9. **Analisar objetivos ou objetivo para esses dados:**
   - Reavaliar os objetivos com base nos dados analisados e ajustar as metas do projeto conforme necessário. Fornecer recomendações baseadas nas análises.
