## 📌 Desafio
O mundo como o conhecemos caiu em um cenário apocalíptico. Um vírus produzido em laboratório está transformando seres humanos e animais em zumbis, famintos por carne fresca. Você, como membro da resistência aos zumbis (e o último sobrevivente que sabe codificar), foi designado para desenvolver um sistema para compartilhar recursos entre humanos não infectados.

## 🔎 Link deploy

- https://desafio-sobrevivencia-zumbi.app.com


## 📋 Exigências
 - Linguagens: Python, Css, JavaScript, Html;
 - Frameworks: Django e Django Rest;
 - Banco de dados: Postgres;
 - Controle de versões: Git;

## 📚 Casos de uso
 - Adicionar sobrevivente ao banco de dados;
 - Atualizar local do sobrevivente;
 - Sinalizar sobrevivente como infectado;
 - Trocar itens entre os sobreviventes;
 - Exibir relatórios;

## 🔒 Regras de negócio
 - Um sobrevivente é marcado como infectado quando pelo menos outros 3 sobreviventes sinalizam sua contaminação;
 - Os sobreviventes não podem adicionar/remover itens do inventário;
 - Um sobrevivente infectado não pode negociar com outros sobreviventes;
 - Um sobrevivente infectado não pode acessa/manipular seu inventário;
 - Os pontos dos itens de troca devem ser equivalente;
 - Os itens do sobreviente deve ser declarados quando forem registrados no sistema;

## 📂 Documentação API

### 🪖 Sobreviventes (representa os usuários)
 - Irá exibir uma lista contendo todos os usuários:
    - __GET /survivors/__
 - Irá listar dados do sobrevivente passado:
    - __GET /survivors/details/{id_survivor}/__
 - Irá cadastrar um novo sobrevivente no sistema, juntamente com seus itens do inventário:
    - __POST /survivors/create/__
 - Irá atualizar a latitude e longitude do sobrevivente:
    - __PUT /survivors/update/{id_survivor}/local/__
 - Irá deletar o sobrevivente:
    - __DELETE /survivors/delete/{id_survivor}/__
 - O sobrevivente com __id_survivor_1__ sinaliza que o sobrevivente com __id_survivor_2__ está infectado:
    - __PUT /survivors/{id_survivor_1}/infected/{id_survivor_2}/__
 - Irá fonece dados de relátorio:
    - __GET /survivors/reports/__

### 📦 Inventários (representa o local onde estão os itens dos usuários)
 - Irá exebir uma lista contendo os inventários de todos os sobeviventes:
    - __PUT /inventories/__
 - Irá listar os recursos que um determinado sobrevivente possui em seu inventário:
    - __GET /inventories/survivor/{id_survivor}/__

### 📎 Itens (representa os itens dos usuários)
 - Irá exibir uma lista contendo todos os itens cadastrados no sistema:
    - __GET /items/__
 - Adicionar um novo item no sistema:
    - __POST /items/create/__

### 🛟 Negócios (representa a troca de itens entre os sobreviventes)
 - Realizar troca de itens informados para cada sobrevivente:
    - __POST /business/__