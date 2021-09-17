--
-- File generated with SQLiteStudio v3.3.3 on qui set 16 14:04:34 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: abastecimento
DROP TABLE IF EXISTS abastecimento;

CREATE TABLE abastecimento (
    idAbastecimento INTEGER PRIMARY KEY AUTOINCREMENT,
    data            DATE,
    combustivel     CHAR,
    valorLitro      DOUBLE,
    quantLitro      DOUBLE,
    vTotal          DOUBLE,
    kmAbastecimento INT,
    vcl_idVeiculo   INT     REFERENCES veiculo (idVeiculo) 
                            NOT NULL
);


-- Table: veiculo
DROP TABLE IF EXISTS veiculo;

CREATE TABLE veiculo (
    idVeiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    placa     CHAR    NOT NULL,
    modelo            NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
