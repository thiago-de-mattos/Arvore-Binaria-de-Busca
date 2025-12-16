# 🌳 Árvore Binária de Busca (ABB) com Django

Projeto acadêmico desenvolvido para a disciplina de **Estrutura de Dados**, com o objetivo de aplicar e visualizar na prática os conceitos de **Árvore Binária de Busca (ABB)** em uma aplicação web construída com **Django**.

A aplicação permite que o usuário insira, remova e busque valores em uma árvore binária, com **renderização visual dinâmica em SVG**, sem uso de imagens externas.

---

## 🎯 Funcionalidades

* Inserção de valores na árvore
* Remoção de valores mantendo a estrutura válida da ABB
* Busca de elementos
* Renderização visual automática da árvore após cada operação
* Feedback ao usuário (valor encontrado, não encontrado, removido, duplicado, etc.)

---

## 📘 Objetivos do Projeto

* Aplicar conceitos fundamentais de Estruturas de Dados
* Demonstrar entendimento prático de Árvores Binárias de Busca
* Gerar uma visualização clara e didática da ABB
* Integrar Python + Django em um sistema funcional
* Permitir manipulação da árvore em tempo real
* Desenvolver uma interface simples, limpa e intuitiva

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia            | Função                         |
| --------------------- | ------------------------------ |
| Python 3.12+          | Lógica da árvore e backend     |
| Django 5.2            | Framework web                  |
| HTML5 + CSS3          | Interface e layout             |
| SVG                   | Renderização gráfica da árvore |
| Matplotlib (opcional) | Ferramentas gráficas           |
| NetworkX (opcional)   | Manipulação de grafos          |

---

## 📂 Estrutura do Projeto

```
arvore_binaria/
│── arvore.py            # Classe principal da Árvore Binária de Busca
│── views.py             # Lógica das requisições e controle da árvore
│── urls.py              # Mapeamento de URLs
│── templates/
│   ├── index.html       # Página inicial
│   └── arvore.html      # Renderização da árvore em SVG
│── static/
│   └── css/style.css    # Estilos da interface
│── migrations/          # Migrations do Django
│
├── requirements.txt     # Dependências do projeto
└── manage.py            # Comando principal do Django
```

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/thiago-de-mattos/Arvore-Binaria-de-Busca.git
cd Arvore-Binaria-de-Busca
```

### 2️⃣ Criar e ativar o ambiente virtual

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar migrações

```bash
python manage.py migrate
```

### 5️⃣ Rodar o servidor

```bash
python manage.py runserver
```

Acesse no navegador:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Para **parar o servidor**, utilize:

```bash
Ctrl + C
```

---

## 🧬 Funcionamento da Árvore Binária

A classe `Arvore` implementa:

### ✔ Inserção (`insert`)

Insere valores respeitando as regras da ABB.

### ✔ Busca (`search`)

Realiza a busca de elementos de forma recursiva.

### ✔ Remoção (`delete`)

Remove valores mantendo a estrutura válida da árvore.

### ✔ Conversão para coordenadas

Calcula posições organizadas para cada nó ser exibido corretamente no SVG.

### ✔ Renderização

* Linhas: arestas da árvore
* Círculos: nós
* Texto centralizado: valores

Toda a renderização é feita manualmente, sem dependência de bibliotecas gráficas externas.

---

## 🎨 Interface do Usuário

A interface permite:

* Inserir uma lista inicial de valores
* Visualizar a árvore binária em tempo real
* Inserir novos elementos
* Remover elementos existentes
* Buscar valores específicos
* Receber mensagens de feedback sobre cada operação

---

## 🧪 Testes

O projeto utiliza:

* Testes manuais
* Logs e mensagens de depuração
* Conferência visual da árvore renderizada

Opcionalmente, podem ser adicionados testes unitários com `pytest` ou `unittest`.

---

## 👨‍🎓 Autor

**Thiago de Mattos Azevedo Chaves**
Universidade de Vassouras – Campus Maricá
Curso: Engenharia de Software
Disciplina: Estrutura de Dados

---

## 📄 Licença

Projeto destinado ao **uso acadêmico e demonstração de aprendizado**.
Reprodução permitida para fins educacionais.
