🌳 Árvore Binária de Busca – Projeto Acadêmico com Django

Este projeto foi desenvolvido como parte da disciplina de Estrutura de Dados, utilizando conceitos de Árvore Binária de Busca (ABB) aplicados dentro de uma aplicação web construída com Django.

O sistema recebe uma lista de números enviada pelo usuário, gera dinamicamente uma Árvore Binária de Busca e exibe sua estrutura visual utilizando SVG, sem necessidade de imagens externas.

O usuário pode realizar:

✔ Inserção de valores

✔ Remoção de valores

✔ Busca de elementos

A cada operação, a árvore é reconstruída e renderizada novamente, permitindo compreender visualmente o funcionamento de uma ABB.

📘 Objetivos do Projeto

Aplicar conceitos fundamentais de estruturas de dados

Demonstrar entendimento da árvore binária de busca

Gerar uma visualização dinâmica da árvore

Integrar Python + Django em um sistema funcional

Permitir manipulação da árvore em tempo real

Apresentar interface simples, limpa e intuitiva

🛠️ Tecnologias Utilizadas
Tecnologia	Função
Python 3.12+	Lógica da árvore e backend
Django 5.2	Framework web
HTML5 + CSS3	Interface e layout
SVG	Renderização gráfica da árvore
Matplotlib (opcional)	Ferramentas gráficas
NetworkX (opcional)	Manipulação de grafos
🚀 Como Executar o Projeto
✔️ 1. Clonar o repositório
git clone https://github.com/thiago-de-mattos/Arvore-Binaria-de-Busca.git
cd Arvore-Binaria-de-Busca

✔️ 2. Criar e ativar o ambiente virtual

Windows

python -m venv venv
venv\Scripts\activate


Linux/Mac

python3 -m venv venv
source venv/bin/activate

✔️ 3. Instalar dependências
pip install -r requirements.txt

✔️ 4. Realizar migrações
python manage.py migrate

✔️ 5. Rodar o servidor
python manage.py runserver


Acesse no navegador:
👉 http://127.0.0.1:8000/

🧬 Arquitetura do Projeto
arvore_binaria/
│── arvore.py            # Classe principal da árvore binária de busca
│── views.py             # Rotas e lógica das requisições
│── urls.py              # Mapeamento de URLs
│── templates/
│   ├── index.html       # Página inicial
│   └── arvore.html      # Renderização da árvore em SVG
│── static/
│   └── css/style.css    # Estilos da interface
│── migrations/          # Migrations do Django
requirements.txt
manage.py

📊 Funcionamento da Árvore Binária

A classe Arvore implementa:

✔ Inserção (insert)

Insere valores respeitando as regras da ABB.

✔ Busca (search)

Procura elementos de forma recursiva.

✔ Remoção (delete)

Remove valores mantendo a estrutura válida da árvore.

✔ Conversão para coordenadas

Gera posições organizadas para cada nó ser exibido no SVG.

✔ Renderização

Linhas = arestas

Círculos = nós

Texto centralizado = valor

Tudo implementado manualmente, sem dependência de bibliotecas externas de gráficos.

🎨 Interface do Usuário

Na interface é possível:

Inserir lista inicial de valores

Visualizar a árvore binária

Inserir novos elementos

Remover elementos existentes

Pesquisar um valor

Receber feedback (achado, não encontrado, removido, duplicado etc.)

🧪 Testes

O projeto utiliza:

Testes manuais

Logs e mensagens de depuração

Conferência visual da árvore renderizada

Se desejado, podem ser criados testes unitários com pytest ou unittest.

👨‍🎓 Autor

Thiago de Mattos Azevedo Chaves
Universidade de Vassouras – Campus Maricá
Curso: Engenharia de Software
Disciplina: Estrutura de Dados

📄 Licença

Este projeto é destinado ao uso acadêmico e demonstração do aprendizado.
Reprodução permitida para fins educacionais.
