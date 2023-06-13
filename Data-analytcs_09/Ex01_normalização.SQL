-- Tabela "Clientes"
CREATE TABLE Clientes2 (
  idCliente INTEGER PRIMARY KEY,
  nomeCliente TEXT,
  cidadeCliente TEXT,
  estadoCliente TEXT,
  paisCliente TEXT
);

-- Tabela "Carros"
CREATE TABLE Carros2 (
  idCarro INTEGER PRIMARY KEY,
  kmCarro INTEGER,
  classiCarro TEXT,
  marcaCarro TEXT,
  modeloCarro TEXT,
  anoCarro INTEGER,
  idCombustivel INTEGER,
  FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);


-- Tabela "Combustivel"
CREATE TABLE Combustivel2 (
  idCombustivel INTEGER PRIMARY KEY,
  tipoCombustivel TEXT
);

-- Tabela "Locacoes"
CREATE TABLE Locacoes2 (
  idLocacao INTEGER PRIMARY KEY,
  idCliente INTEGER,
  idCarro INTEGER,
  dataLocacao DATE,
  horaLocacao TIME,
  qtdDiaria INTEGER,
  vlrDiaria DECIMAL,
  dataEntrega DATE,
  horaEntrega TIME,
  idVendedor INTEGER,
  FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),
  FOREIGN KEY (idCarro) REFERENCES Carros(idCarro),
  FOREIGN KEY (idVendedor) REFERENCES Vendedores(idVendedor)
);

-- Tabela "Vendedores"
CREATE TABLE Vendedores2 (
  idVendedor INTEGER PRIMARY KEY,
  nomeVendedor TEXT,
  sexoVendedor TEXT,
  estadoVendedor TEXT
);
