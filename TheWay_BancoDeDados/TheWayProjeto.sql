USE TheWayProjeto;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    perfil ENUM('ADMIN','FUNCIONARIO') NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE,
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(200)
);

CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    qtd_estoque INT DEFAULT 0
);

CREATE TABLE objetivo_suplementacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

CREATE TABLE produto_objetivo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prioridade INT,
    observacao TEXT,
    produto_id INT,
    objetivo_id INT,
    FOREIGN KEY (produto_id) REFERENCES produto(id),
    FOREIGN KEY (objetivo_id) REFERENCES objetivo_suplementacao(id)
);

CREATE TABLE venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME NOT NULL,
    status ENUM('ABERTA','CONCLUIDA','CANCELADA'),
    total DECIMAL(10,2),
    cliente_id INT,
    usuario_id INT,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE item_venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2),
    produto_id INT,
    venda_id INT,
    FOREIGN KEY (produto_id) REFERENCES produto(id),
    FOREIGN KEY (venda_id) REFERENCES venda(id)
);