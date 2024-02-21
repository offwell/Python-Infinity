CREATE DATABASE IF NOT EXISTS RegistroPessoal;

USE RegistroPessoal;

CREATE TABLE IF NOT EXISTS Pessoa (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeCompleto VARCHAR(100),
    Idade INT,
    Genero VARCHAR(20),
    Nacionalidade VARCHAR(50),
    Email VARCHAR(100),
    EstadoCivil VARCHAR(20),
    NomePai VARCHAR(100),
    NomeMae VARCHAR(100)
);

INSERT INTO Pessoa (NomeCompleto, Idade, Genero, Nacionalidade, Email, EstadoCivil, NomePai, NomeMae)
VALUES 
('João Silva', 30, 'Masculino', 'Brasileiro', 'joao@example.com', 'Solteiro', 'José Silva', 'Maria Silva'),
('Maria Santos', 25, 'Feminino', 'Brasileira', 'maria@example.com', 'Casada', 'Pedro Santos', 'Ana Santos'),
('Carlos Ferreira', 40, 'Masculino', 'Português', 'carlos@example.com', 'Divorciado', 'Manuel Ferreira', 'Sofia Ferreira');

UPDATE Pessoa
SET Email = 'nova_email_maria@example.com', EstadoCivil = 'Divorciada'
WHERE ID = 2;

DELETE FROM Pessoa
WHERE ID = 3;
