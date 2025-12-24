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
2. **Crie um ambiente virtual:**
   ```bash
   python -m venv .venv
   # No Windows:
   .venv\Scripts\activate
   # No Linux/Mac:
   source .venv/bin/activate
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
4. **Inicie o servidor:**
   ```bash
   uvicorn main:app --reload
### A API estará disponível em http://127.0.0.1:8000. Você pode acessar a documentação interativa em http://127.0.0.1:8000/docs.

## 🌐 Deploy no Render

O deploy foi realizado no Render. Para garantir que a lista de tarefas funcione corretamente em um único processo de memória, o comando de inicialização configurado foi:
      ```bash
      uvicorn main:app --host 0.0.0.0 --port $PORT
      
## ✒️ Desenvolvedor
### João Pedro Dala Dea Mello 
