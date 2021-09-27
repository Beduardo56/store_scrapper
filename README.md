# store_scrapper

## Descrição geral.
Este repositorio tem como objetivo construir datasets que informam o periodo de operação de lojas de shoppings.
## Descrição das tabelas geradas
 - dados_de_loja.csv -> Tabela contendo o id, nome, categoria, telefone e shopping origem
 - horario_de_funcionamento.csv -> Tabela contendo as informações: id da loja, dia da semana, periodo de funcionamento
## Como ajudar a popular o dataset de horario de funcionamento:
 - Crie um scrapper para as lojas de um determinado shopping (como feito para o shopping vitoria), adicione mais dados a dados_de_loja (informaçes obrigatorias: nome da loja e shopping/rua)
 - cria uma env usando as dependencias criadas pelo poetry
 - Rode a função que busca as informaçes de periodos de funcionamento:
```python
from store_scrapper.periodos_de_operacao.handler import find_hour_operation
store_data = # pega novos dados de dados_de_loja e joga em um dataframe
periods_information = find_hour_operation(store_data)
# concatena o resultado em horario_de_funcionamento
```
