-- Tabela de dimensão Cliente
CREATE TABLE DimCliente (
  idCliente INTEGER PRIMARY KEY,
  nomeCliente VARCHAR(100),
  cidadeCliente VARCHAR(100),
  estadoCliente VARCHAR(100),
  paisCliente VARCHAR(100)
);

-- Tabela de dimensão Carro
CREATE TABLE DimCarro (
  idCarro INTEGER PRIMARY KEY,
  kmCarro INTEGER,
  classiCarro VARCHAR(100),
  marcaCarro VARCHAR(100),
  modeloCarro VARCHAR(100),
  anoCarro INTEGER
);

-- Tabela de dimensão Combustivel
CREATE TABLE DimCombustivel (
  idCombustivel INTEGER PRIMARY KEY,
  tipoCombustivel VARCHAR(100)
);

-- Tabela de dimensão Vendedor
CREATE TABLE DimVendedor (
  idVendedor INTEGER PRIMARY KEY,
  nomeVendedor VARCHAR(100),
  sexoVendedor VARCHAR(100),
  estadoVendedor VARCHAR(100)
);

-- Tabela de fatos Locacao
CREATE TABLE FatLocacao (
  idLocacao INTEGER PRIMARY KEY,
  idCliente INTEGER,
  idCarro INTEGER,
  idCombustivel INTEGER,
  idVendedor INTEGER,
  dataLocacao DATE,
  horaLocacao TIME,
  qtdDiaria INTEGER,
  vlrDiaria DECIMAL(10, 2),
  dataEntrega DATE,
  horaEntrega TIME,
  FOREIGN KEY (idCliente) REFERENCES DimCliente(idCliente),
  FOREIGN KEY (idCarro) REFERENCES DimCarro(idCarro),
  FOREIGN KEY (idCombustivel) REFERENCES DimCombustivel(idCombustivel),
  FOREIGN KEY (idVendedor) REFERENCES DimVendedor(idVendedor)
);

""" VIEWS CRIADAS """

-- Visualização DimCliente
CREATE VIEW vw_DimCliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

-- Visualização DimCarro
CREATE VIEW vw_DimCarro AS
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao;

-- Visualização DimCombustivel
CREATE VIEW vw_DimCombustivel AS
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao;

-- Visualização DimVendedor
CREATE VIEW vw_DimVendedor AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

-- Visualização FatLocacao
CREATE VIEW vw_FatLocacao AS
SELECT idLocacao, idCliente, idCarro, idCombustivel, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao;
