# 🏋️ TheWay — Sistema de Gestão de Suplementos

**Entrega 3 – Sistema Completo | Desenvolvimento Web**

Sistema web completo para gestão de uma loja de suplementos alimentares, com interface integrada à API REST protegida por JWT.

**Alunos:** João Francisco Torres e Marcus Vinícius R. Bacelar

---

## 📋 Funcionalidades

| Módulo | Descrição |
|---|---|
| 🔐 Autenticação JWT | Login com token de acesso; todas as rotas da API são protegidas |
| 📦 Produtos | CRUD completo com validação de preço e estoque |
| 👥 Clientes | CRUD com validação de CPF (dígitos verificadores), telefone e e-mail |
| 🛒 Vendas | Registro de venda com itens, desconto automático do estoque e cálculo do total |
| 💊 Recomendação | Formulário público de recomendação de suplementos baseado no IMC |
| 📊 Dashboard | Estatísticas em tempo real: produtos, clientes, vendas e faturamento total |

---

## 🛠 Tecnologias

- **Python 3.12** + **Django 5.x**
- **Django REST Framework** — API REST
- **djangorestframework-simplejwt** — Autenticação JWT
- **django-cors-headers** — CORS para consumo da API pelo frontend
- **SQLite** (desenvolvimento) / MySQL (produção)
- **HTML5 + CSS3 + JavaScript Vanilla** — Interface web sem frameworks externos

---

## 🚀 Como executar

### 1. Instalar dependências

```bash
cd TheWay_Projeto
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
```

### 2. Aplicar migrações

```bash
python manage.py migrate
```

### 3. Criar superusuário (necessário para login)

```bash
python manage.py createsuperuser
```

> Sugestão: usuário `admin`, senha `admin123`

### 4. Iniciar o servidor

```bash
python manage.py runserver
```

### 5. Acessar o sistema

| URL | Descrição |
|---|---|
| `http://127.0.0.1:8000/` | Interface web completa (login necessário) |
| `http://127.0.0.1:8000/recomendacao/` | Recomendação de suplementos (público) |
| `http://127.0.0.1:8000/admin/` | Painel administrativo Django |
| `http://127.0.0.1:8000/api/token/` | Obter token JWT (POST) |
| `http://127.0.0.1:8000/api/produtos/` | API de produtos (protegida) |
| `http://127.0.0.1:8000/api/clientes/` | API de clientes (protegida) |
| `http://127.0.0.1:8000/api/vendas/` | API de vendas (protegida) |

---

## 🔐 Autenticação JWT

### Obter token

```http
POST /api/token/
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

**Resposta:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1..."
}
```

### Usar o token nas requisições

```http
GET /api/produtos/
Authorization: Bearer <access_token>
```

### Renovar o token

```http
POST /api/token/refresh/
Content-Type: application/json

{ "refresh": "<refresh_token>" }
```

---

## 📡 Endpoints da API

### Produtos

| Método | URL | Descrição |
|---|---|---|
| GET | `/api/produtos/` | Listar todos os produtos |
| POST | `/api/produtos/` | Criar produto |
| GET | `/api/produtos/{id}/` | Detalhar produto |
| PUT | `/api/produtos/{id}/` | Atualizar produto |
| DELETE | `/api/produtos/{id}/` | Excluir produto |

**Validações:** nome ≥ 2 chars · preço > 0 · estoque ≥ 0

### Clientes

| Método | URL | Descrição |
|---|---|---|
| GET | `/api/clientes/` | Listar todos os clientes |
| POST | `/api/clientes/` | Criar cliente |
| GET | `/api/clientes/{id}/` | Detalhar cliente |
| PUT | `/api/clientes/{id}/` | Atualizar cliente |
| DELETE | `/api/clientes/{id}/` | Excluir cliente |

**Validações:** CPF com dígitos verificadores · telefone 10-11 dígitos · nome ≥ 3 chars

### Vendas

| Método | URL | Descrição |
|---|---|---|
| GET | `/api/vendas/` | Listar vendas |
| POST | `/api/vendas/` | Criar venda (com itens) |
| GET | `/api/vendas/{id}/` | Detalhar venda |

**Exemplo de criação de venda:**
```json
POST /api/vendas/
{
  "cliente": 1,
  "status": "CONCLUIDA",
  "total": 0,
  "itens": [
    { "produto": 2, "quantidade": 3, "preco_unitario": 0, "subtotal": 0 }
  ]
}
```
> Os campos `preco_unitario`, `subtotal` e `total` são calculados automaticamente pelo sistema.

**Regras de negócio:**
- Venda deve ter pelo menos 1 item
- Estoque é verificado antes de concluir (erro HTTP 400 se insuficiente)
- Estoque é decrementado automaticamente ao registrar a venda

---

## 🏗 Arquitetura

```
TheWay_Projeto/
├── config/           # Configurações do projeto (settings, urls, wsgi)
├── core/             # Exceções e handler customizado
├── clientes/         # App: CRUD de clientes + validação de CPF
├── produtos/         # App: CRUD de produtos + validação de preço/estoque
├── vendas/           # App: Registro de vendas com itens e controle de estoque
├── suplementos/      # App: Interface web e recomendação por IMC
└── templates/        # Templates HTML do frontend
```

**Padrão arquitetural:** Camadas (Apresentação → API REST → Regras de Negócio → Persistência)

---

## 🎨 Identidade Visual

| Elemento | Valor |
|---|---|
| Nome do sistema | **TheWay** |
| Cor primária | `#3d0a44` (Roxo escuro) |
| Cor de destaque | `#e5007d` (Rosa vibrante) |
| Fonte | Segoe UI (sans-serif) |

---

## 📁 Estrutura do Repositório

```
TheWay/
├── TheWay_BancoDeDados/    # Script SQL do banco de dados
├── TheWay_Documentacao/    # Documentação e diagramas
├── TheWay_Projeto/         # Código-fonte do sistema
└── README.md               # Este arquivo
```

---

## ✅ Checklist da Entrega 3

- [x] Interface web consumindo a API REST (frontend em HTML/JS)
- [x] Usabilidade e organização visual com identidade TheWay
- [x] Validações de campos no frontend e no backend (serializers)
- [x] Regras de negócio: verificação de estoque, cálculo de total
- [x] API REST funcional (produtos, clientes, vendas)
- [x] API protegida com JWT
- [x] Sistema com nome (TheWay) e esquema de cores próprios
- [x] README completo com instruções de execução
- [x] Projeto versionado no GitHub
