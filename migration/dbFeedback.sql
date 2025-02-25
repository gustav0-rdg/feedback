CREATE DATABASE IF NOT EXISTS dbFeedback;
USE dbFeedback;

CREATE TABLE IF NOT EXISTS tbComentarios(
	idComentario INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(30) NOT NULL,
    comentarios TEXT NOT NULL,
    dataHora DATETIME NOT NULL
    );