# Relatório: Normalização do Banco de Dados e Modelo Dimensional

## Identificação das Dependências Funcionais

Para analisar a estrutura da tabela existente, foi realizada uma identificação das dependências funcionais entre as colunas. O objetivo era determinar quais colunas são determinadas por outras colunas e como elas estão relacionadas.

## Aplicação da Primeira Forma Normal (1NF)

Após a análise, verificou-se que cada coluna continha apenas um valor atômico, e não havia repetições de grupos de valores em uma única coluna. Portanto, a tabela já estava em conformidade com a primeira forma normal.

## Aplicação da Segunda Forma Normal (2NF)

Foi verificado se todas as colunas não chave dependiam completamente da chave primária. Caso houvesse dependências parciais, as colunas foram separadas em novas tabelas e relacionadas corretamente com a chave primária. Verificou-se que a tabela já estava em conformidade com a segunda forma normal, pois todas as colunas não chave dependiam completamente da chave primária.

## Aplicação da Terceira Forma Normal (3NF)

Garantiu-se que não havia dependências transitivas, ou seja, nenhuma coluna não chave dependia de outra coluna não chave através de uma terceira coluna não chave. Se necessário, as colunas foram separadas em novas tabelas e estabelecidos relacionamentos apropriados. Foi verificado que a tabela já estava em conformidade com a terceira forma normal, pois não havia dependências transitivas entre as colunas não chave.

## Identificação e Tratamento de Outras Formas Normais

Além da terceira forma normal, considerou-se a possibilidade de aplicar outras formas normais, como a quarta forma normal (4NF) e a quinta forma normal (5NF), dependendo da complexidade e dos requisitos do banco de dados. No entanto, não foi necessário aplicar essas formas normais no momento, pois a tabela já estava em conformidade com a terceira forma normal.

## Definição de Relacionamentos entre as Tabelas

Após a normalização das tabelas, foram estabelecidos relacionamentos entre elas usando chaves primárias e estrangeiras. Esses relacionamentos ajudam a manter a integridade dos dados e permitem consultas e operações eficientes no banco de dados.

## Construção do Modelo Dimensional

Com base nas visualizações criadas anteriormente, foi construído o modelo dimensional. Foram criadas tabelas de dimensão para representar as entidades relevantes, como DimCliente, DimCarro, DimCombustivel e DimVendedor. Cada tabela de dimensão contém colunas representando os atributos específicos da entidade correspondente. Além disso, foi criada uma tabela de fatos chamada FactLocacao, que armazena informações relacionadas às locações. A tabela de fatos inclui as chaves estrangeiras das dimensões, bem como outras informações relevantes sobre as locações.

## Criação dos Jobs em Formato Parquet

Para otimizar o processamento e armazenamento dos dados, foram criados dois jobs em formato Parquet. Um job foi criado para os dados em formato CSV e o outro para os dados em formato JSON. Esses jobs foram configurados para processar e transformar os dados brutos nas tabelas correspondentes no banco de dados.

## Criação das Tabelas no AWS Athena

Após a transformação dos dados, foram criadas duas tabelas no AWS Athena: "filmes" e "atores". Essas tabelas foram criadas com base nos dados processados pelo job anterior. Um script foi utilizado para enviar os dados transformados para o seu bucket no AWS.

