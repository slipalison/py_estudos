# 📚 Curso Intensivo de Python para Arquitetos .NET/C#

## Estrutura do Curso

Organizei seu plano em **8 Módulos** com aulas práticas e progressivas. Cada aula tem objetivos claros, conceitos teóricos mínimos e **muita prática**.

---

## 🎓 MÓDULO 1: Fundamentos e Sintaxe
**Duração:** 2-3 dias | **Foco:** Traduzir seu conhecimento C# para Python

### Aula 1.1 — Ambiente e Primeiros Passos
**Objetivos:**
- Configurar ambiente Python profissional
- Entender o ecossistema Python vs .NET

**Conteúdo:**

| C# / .NET | Python |
|-----------|--------|
| Visual Studio / Rider | PyCharm ✅ |
| NuGet | pip + venv |
| .csproj | requirements.txt / pyproject.toml |
| dotnet run | python script.py |

**Prática:**
- [ ] Verificar instalação: `python --version`
- [ ] Criar ambiente virtual: `python -m venv .venv`
- [ ] Ativar ambiente: `source .venv/bin/activate`
- [ ] Criar primeiro script "Hello, Python!"

---

### Aula 1.2 — Tipos e Variáveis
**Objetivos:**
- Entender tipagem dinâmica com type hints
- Mapear tipos C# → Python

**Comparativo Rápido:**
```csharp
// C#
string nome = "João";
int idade = 30;
bool ativo = true;
List<string> tags = new() { "dev", "senior" };
Dictionary<string, int> scores = new() { {"math", 100} };
```


```python
# Python (com type hints - seu estilo preferido!)
nome: str = "João"
idade: int = 30
ativo: bool = True
tags: list[str] = ["dev", "senior"]
scores: dict[str, int] = {"math": 100}
```


**Prática:**
- [ ] Declarar variáveis de todos os tipos básicos
- [ ] Criar uma lista e um dicionário
- [ ] Experimentar `type()` para verificar tipos

---

### Aula 1.3 — Controle de Fluxo
**Objetivos:**
- Dominar if/for/while em Python
- Entender a importância da **indentação**

**Comparativo:**
```csharp
// C# - chaves definem blocos
if (idade >= 18) {
    Console.WriteLine("Maior de idade");
} else {
    Console.WriteLine("Menor de idade");
}

foreach (var item in lista) {
    Console.WriteLine(item);
}
```


```python
# Python - indentação define blocos (4 espaços!)
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

for item in lista:
    print(item)
```


**💡 Dica de Arquiteto:** Python usa `elif` (não `else if`)

**Prática:**
- [ ] Implementar FizzBuzz em Python
- [ ] Criar loop que percorre dicionário
- [ ] Usar `enumerate()` e `range()`

---

### Aula 1.4 — Funções
**Objetivos:**
- Criar funções com tipagem
- Entender args, kwargs e valores default

**Comparativo:**
```csharp
// C#
public decimal CalcularDesconto(decimal valor, decimal percentual = 0.1m)
{
    return valor * (1 - percentual);
}
```


```python
# Python
def calcular_desconto(valor: float, percentual: float = 0.1) -> float:
    return valor * (1 - percentual)
```


**Prática:**
- [ ] Criar 5 funções utilitárias com type hints
- [ ] Usar parâmetros opcionais
- [ ] Experimentar `*args` e `**kwargs`

---

### Aula 1.5 — Coleções e Compreensões
**Objetivos:**
- Dominar list, dict, set, tuple
- Aprender List Comprehensions (superpoder do Python!)

**🔥 List Comprehensions — Isso não existe em C#!**
```csharp
// C# com LINQ
var pares = numeros.Where(n => n % 2 == 0).Select(n => n * 2).ToList();
```


```python
# Python - List Comprehension (mais conciso!)
pares = [n * 2 for n in numeros if n % 2 == 0]

# Dict Comprehension
quadrados = {n: n**2 for n in range(10)}
```


**Prática:**
- [ ] Converter 5 consultas LINQ para comprehensions
- [ ] Criar dicionário a partir de duas listas com `zip()`
- [ ] Usar `set` para remover duplicatas

---

## 🎓 MÓDULO 2: Python Moderno e Tipado
**Duração:** 3-4 dias | **Foco:** Código de produção com qualidade enterprise

### Aula 2.1 — Sistema de Tipos Avançado
**Objetivos:**
- Usar `typing` como um profissional
- Criar código tão seguro quanto C#

```python
from typing import Optional, Union
from collections.abc import Callable

# Optional = pode ser None (como nullable em C#)
def buscar_usuario(id: int) -> Optional[dict]:
    ...

# Union = múltiplos tipos possíveis
def processar(valor: Union[str, int]) -> str:
    ...

# Callable = delegate/Func em C#
def executar(callback: Callable[[int], str]) -> None:
    ...
```


**Prática:**
- [ ] Tipar 10 funções existentes
- [ ] Configurar mypy para checagem estática
- [ ] Criar alias de tipos complexos

---

### Aula 2.2 — Dataclasses (seu novo Record/Class)
**Objetivos:**
- Substituir classes POCO/DTO por dataclasses
- Entender imutabilidade com `frozen=True`

**Comparativo:**
```csharp
// C# Record
public record Cliente(string Nome, string Email, bool Ativo = true);
```


```python
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    ativo: bool = True

# Imutável (como record em C#)
@dataclass(frozen=True)
class ClienteImutavel:
    nome: str
    email: str
```


**Prática:**
- [ ] Modelar entidades: `Pedido`, `Item`, `Cliente`
- [ ] Criar dataclass com validação no `__post_init__`
- [ ] Testar igualdade e hash automáticos

---

### Aula 2.3 — Módulos e Pacotes
**Objetivos:**
- Estruturar projeto como solução .NET
- Entender imports e `__init__.py`

**Estrutura Recomendada:**
```
meu_projeto/
├── src/
│   └── meu_projeto/
│       ├── __init__.py
│       ├── domain/
│       │   ├── __init__.py
│       │   └── entities.py
│       ├── application/
│       │   ├── __init__.py
│       │   └── services.py
│       └── infrastructure/
│           ├── __init__.py
│           └── repositories.py
├── tests/
│   └── test_entities.py
├── requirements.txt
└── pyproject.toml
```


**Prática:**
- [ ] Criar estrutura de pastas
- [ ] Configurar imports relativos e absolutos
- [ ] Criar `requirements.txt`

---

### Aula 2.4 — Gerenciamento de Dependências
**Objetivos:**
- Dominar pip e venv
- Entender requirements.txt vs pyproject.toml

**Comandos Essenciais:**
```shell script
# Criar ambiente virtual
python -m venv .venv

# Ativar (Linux/Mac)
source .venv/bin/activate

# Instalar pacotes
pip install fastapi uvicorn

# Salvar dependências
pip freeze > requirements.txt

# Instalar de requirements
pip install -r requirements.txt
```


**Prática:**
- [ ] Criar novo projeto do zero com venv
- [ ] Instalar 3 pacotes úteis
- [ ] Gerar e usar requirements.txt

---

## 🎓 MÓDULO 3: OOP e Design Patterns
**Duração:** 4-5 dias | **Foco:** Aplicar padrões que você já domina

### Aula 3.1 — Classes e Herança
**Objetivos:**
- Criar classes Python idiomáticas
- Entender `self` (é o `this` implícito do C#)

```python
class Entidade:
    def __init__(self, id: int):
        self._id = id  # _ = convenção para "protected"
    
    @property
    def id(self) -> int:
        return self._id

class Cliente(Entidade):
    def __init__(self, id: int, nome: str):
        super().__init__(id)
        self.nome = nome
```


**Prática:**
- [ ] Criar hierarquia de entidades
- [ ] Usar `@property` para encapsulamento
- [ ] Implementar `__str__` e `__repr__`

---

### Aula 3.2 — Interfaces com Protocol
**Objetivos:**
- Criar contratos como interfaces C#
- Implementar Dependency Injection

```python
from typing import Protocol

# Equivalente a interface em C#
class IRepositorio(Protocol):
    def obter(self, id: int) -> dict | None: ...
    def salvar(self, entidade: dict) -> None: ...

# Implementação (não precisa declarar que implementa!)
class RepositorioMemoria:
    def __init__(self):
        self._dados: dict[int, dict] = {}
    
    def obter(self, id: int) -> dict | None:
        return self._dados.get(id)
    
    def salvar(self, entidade: dict) -> None:
        self._dados[entidade["id"]] = entidade
```


**💡 Duck Typing:** Se anda como pato e faz quack como pato... é um pato!

**Prática:**
- [ ] Criar 3 Protocols (IRepository, IService, ILogger)
- [ ] Implementar versões concretas
- [ ] Injetar dependências manualmente

---

### Aula 3.3 — Padrões de Projeto em Python
**Objetivos:**
- Implementar padrões comuns de forma Pythonica

**Repository Pattern:**
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    nome: str

class ClienteRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Cliente | None: ...
    
    @abstractmethod
    def save(self, cliente: Cliente) -> None: ...

class ClienteRepositoryMemory(ClienteRepository):
    def __init__(self):
        self._store: dict[int, Cliente] = {}
    
    def get_by_id(self, id: int) -> Cliente | None:
        return self._store.get(id)
    
    def save(self, cliente: Cliente) -> None:
        self._store[cliente.id] = cliente
```


**Prática:**
- [ ] Implementar Repository Pattern
- [ ] Implementar Factory Pattern
- [ ] Implementar Strategy Pattern

---

### Aula 3.4 — Testes com pytest
**Objetivos:**
- Testar código como um profissional
- Entender fixtures (equivalente ao Setup/Teardown)

```python
# tests/test_cliente.py
import pytest
from meu_projeto.domain.entities import Cliente

class TestCliente:
    def test_criar_cliente_valido(self):
        cliente = Cliente(id=1, nome="João")
        assert cliente.nome == "João"
    
    def test_cliente_sem_nome_levanta_erro(self):
        with pytest.raises(ValueError):
            Cliente(id=1, nome="")

# Fixture = Arrange compartilhado
@pytest.fixture
def cliente_valido() -> Cliente:
    return Cliente(id=1, nome="João")

def test_com_fixture(cliente_valido: Cliente):
    assert cliente_valido.id == 1
```


**Prática:**
- [ ] Instalar pytest: `pip install pytest`
- [ ] Escrever 10 testes para suas entidades
- [ ] Usar fixtures para setup

---

## 🎓 MÓDULO 4: Web APIs com FastAPI
**Duração:** 1 semana | **Foco:** Traduzir experiência ASP.NET

### Aula 4.1 — Introdução ao FastAPI
**Objetivos:**
- Criar sua primeira API
- Entender decorators de rota

**Comparativo:**
```csharp
// ASP.NET Minimal API
app.MapGet("/clientes/{id}", (int id) => Results.Ok(new { Id = id }));
```


```python
# FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.get("/clientes/{id}")
def obter_cliente(id: int):
    return {"id": id}
```


**Prática:**
- [ ] Instalar: `pip install fastapi uvicorn`
- [ ] Criar API "Hello World"
- [ ] Executar: `uvicorn main:app --reload`

---

### Aula 4.2 — Modelos com Pydantic
**Objetivos:**
- Validar requests/responses automaticamente
- Criar DTOs robustos

```python
from pydantic import BaseModel, EmailStr, Field

class ClienteCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    idade: int = Field(..., ge=0, le=150)

class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True  # Permite converter de ORM/dataclass
```


**Prática:**
- [ ] Criar modelos de Request e Response
- [ ] Testar validação automática
- [ ] Usar na API

---

### Aula 4.3 — CRUD Completo
**Objetivos:**
- Implementar todas as operações
- Organizar código em camadas

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Simulando banco em memória
db: dict[int, dict] = {}

@app.post("/clientes", status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: ClienteCreate) -> ClienteResponse:
    id = len(db) + 1
    db[id] = {"id": id, **cliente.model_dump()}
    return ClienteResponse(**db[id])

@app.get("/clientes/{id}")
def obter_cliente(id: int) -> ClienteResponse:
    if id not in db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return ClienteResponse(**db[id])

@app.put("/clientes/{id}")
def atualizar_cliente(id: int, cliente: ClienteCreate) -> ClienteResponse:
    if id not in db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db[id] = {"id": id, **cliente.model_dump()}
    return ClienteResponse(**db[id])

@app.delete("/clientes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_cliente(id: int):
    if id not in db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    del db[id]
```


**Prática:**
- [ ] Implementar CRUD para 2 entidades
- [ ] Testar via Swagger UI (automático em `/docs`)
- [ ] Adicionar tratamento de erros

---

### Aula 4.4 — Testes de API
**Objetivos:**
- Testar endpoints com TestClient
- Criar testes de integração

```python
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_criar_cliente():
    response = client.post("/clientes", json={
        "nome": "João",
        "email": "joao@email.com",
        "idade": 30
    })
    assert response.status_code == 201
    assert response.json()["nome"] == "João"


def test_cliente_nao_encontrado():
    response = client.get("/clientes/99999")
    assert response.status_code == 404
```


**Prática:**
- [ ] Instalar: `pip install httpx` (dependência do TestClient)
- [ ] Escrever testes para cada endpoint
- [ ] Testar casos de erro

---

## 🎓 MÓDULO 5: Projeto Final
**Duração:** 1-2 semanas | **Foco:** Consolidação

### Projeto: API de Catálogo de Produtos
**Requisitos:**
- [ ] CRUD de Produtos e Categorias
- [ ] Busca com filtros
- [ ] Paginação
- [ ] Validação robusta
- [ ] Testes com 80%+ cobertura
- [ ] Documentação automática

**Arquitetura Sugerida:**
```
catalogo_api/
├── src/
│   └── catalogo/
│       ├── domain/
│       │   ├── entities.py
│       │   └── repositories.py (protocols)
│       ├── application/
│       │   └── services.py
│       ├── infrastructure/
│       │   └── repositories.py (implementações)
│       └── api/
│           ├── main.py
│           ├── routes/
│           └── schemas/
├── tests/
└── requirements.txt
```


---

## 📋 Checklist de Progresso (Atualizado)

**Status atual:** Aula 2.4 concluída. Próxima: Aula 3.1 — Classes e Herança.

### Semana 1: Fundamentos ⬜
- [x] Aula 1.1 — Ambiente
- [x] Aula 1.2 — Tipos
- [x] Aula 1.3 — Controle de Fluxo
- [x] Aula 1.4 — Funções
- [x] Aula 1.5 — Coleções

### Semana 2: Python Moderno ⬜
- [x] Aula 2.1 — Typing
- [x] Aula 2.2 — Dataclasses
- [x] Aula 2.3 — Módulos
- [x] Aula 2.4 — Dependências

### Semana 3: OOP e Testes ⬜
- [ ] Aula 3.1 — Classes
- [ ] Aula 3.2 — Protocols
- [ ] Aula 3.3 — Design Patterns
- [ ] Aula 3.4 — pytest

### Semana 4: Web API ⬜
- [ ] Aula 4.1 — FastAPI Básico
- [ ] Aula 4.2 — Pydantic
- [ ] Aula 4.3 — CRUD
- [ ] Aula 4.4 — Testes de API

### Semana 5-6: Projeto Final ⬜
- [ ] Definir escopo
- [ ] Implementar
- [ ] Testar
- [ ] Documentar

---

## 🏆 Regras de Ouro

1. **Escreva mais, leia menos** — Aprenda fazendo
2. **Use sempre type hints** — Mantenha a disciplina do C#
3. **Compare constantemente** — C# vs Python acelera o aprendizado
4. **Projetos pequenos completos** — Melhor que tutoriais longos
5. **pytest desde o dia 1** — Qualidade não é opcional

---
