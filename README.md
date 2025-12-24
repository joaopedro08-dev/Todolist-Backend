# 🎯 To-Do List - Backend (FastAPI)

Este é o servidor (API) da aplicação To-Do List. Ele foi desenvolvido em Python utilizando o framework **FastAPI** para gerenciar o CRUD de tarefas.

> **Nota:** Atualmente, esta API utiliza armazenamento em **memória volátil (RAM)**. Isso significa que os dados são redefinidos sempre que o servidor for reiniciado ou entrar em modo de repouso no Render.

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI**: Framework moderno e de alta performance.
* **Uvicorn/Gunicorn**: Servidores ASGI para produção.
* **Pydantic**: Para validação de dados e esquemas.
* **CORS Middleware**: Configurado para permitir acesso do frontend.

## 🛠️ Funcionalidades

* `GET /tasks`: Lista todas as tarefas.
* `POST /tasks`: Cria uma nova tarefa.
* `PUT /tasks/{id}`: Atualiza título, descrição ou status de uma tarefa existente.
* `DELETE /tasks/{id}`: Remove uma tarefa da lista.

## 📥 Como rodar o projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/todolist-backend.git](https://github.com/seu-usuario/todolist-backend.git)
   cd todolist-backend
