# 📚 Resumo do Projeto `CifraFacil`

## ✅ **Dia 1 — Git & GitHub**
- Criou repositório `PortfolioApp` ou `CifraFacil`.
- Configurou `.gitignore`.
- Branches: `main`, `develop`, `feature`.
- Fez `git init`, `git remote add origin`.
- Fluxo: `feature` -> `develop` -> `main` via Pull Request (PR).
- README inicial criado com descrição e instruções básicas.

---

## ✅ **Dia 2 — Pytest**
- Ambiente virtual com `venv` ou `pipenv`.
- Instalação do `pytest` e criação da pasta `/tests`.
- Escreveu `validators.py` com função `validar_nivel`.
- Testes unitários: `test_basics.py`.
- Cobertura com `pytest --cov`.

---

## ✅ **Dia 3 — FastAPI**
- Instalou `fastapi` e `uvicorn`.
- Criou `main.py` com `FastAPI()`.
- Rotas `GET` e `POST` para cifras.
- Usou `Pydantic` para validação de schema `Cifra`.
- Testou no `Swagger UI` (`/docs`).

---

## ✅ **Dia 4 — Banco de Dados**
- Usou `PostgreSQL` local + `SQLAlchemy` + `psycopg2`.
- Criou `models.py` com modelo `Cifra`.
- Criou e conectou banco `cifras` via `DATABASE_URL`.
- `POST` e `GET` persistindo dados reais.
- Corrigiu `validators` para funcionar com `Pydantic`.

---

## ✅ **Dia 5 — PUT e Update**
- Adicionou rota `PUT /cifras/{id}`.
- Atualizou `main.py` para incluir `update_cifra`.
- Validou PUT via Postman.
- Branch de segurança criada, merge feito após teste.

---

## ✅ **Dia 6 — Frontend**
- Criou projeto `Angular` com `ng new`.
- Usou `ng generate component` para `cifra-form`.
- Construiu formulário `index.html` para enviar requisição `POST` para a API.
- Conectou com API `FastAPI` (`http://localhost:8000/cifras/`).
- Corrigiu CORS e métodos no backend.
- Testou envio via Frontend **com sucesso**!

---

## 🔜 **Próximos passos (Dia 7 em diante)**
- Revisar testes (`pytest`) cobrindo endpoints reais.
- Versionar tudo (`git add .` ➜ `git commit` ➜ `git push` ➜ `PR` ➜ `merge`).
- Deploy backend (Render/Railway).
- Deploy frontend (Vercel/Netlify).
- Conferir tudo online.
- Atualizar README final com URLs e instruções.

---

## ⚙️ **Tech Stack**
- **Backend:** FastAPI + PostgreSQL + SQLAlchemy
- **Frontend:** Angular
- **Testes:** Pytest
- **Deploy:** Render / Railway / Vercel
- **Versionamento:** Git, GitHub (branches `main`, `develop`, `feature`)

---

# 🚀 **Status**
✅ Local: OK  
✅ API: OK  
✅ Frontend: OK  
🔜 Deploy

---

**Qualquer dúvida, abre nova conversa e cola isso!**

---
