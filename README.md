🌳 Árvore Binária de Busca – Projeto Acadêmico com Django

Este projeto foi desenvolvido como parte da disciplina de Estrutura de Dados, utilizando conceitos de Árvore Binária de Busca (ABB) e Grafos aplicados dentro de uma aplicação web construída com Django.

O sistema recebe uma lista de números enviada pelo usuário, gera dinamicamente uma Árvore Binária de Busca e exibe sua estrutura visual utilizando SVG nativo, sem dependência de imagens externas. Além disso, o usuário pode realizar operações de:

Inserção de valores

Remoção de valores

Busca de elementos

A cada operação, a árvore é reconstruída e exibida novamente de forma organizada, permitindo compreender visualmente o funcionamento da ABB.

📘 Objetivos do Projeto

Aplicar conceitos fundamentais de estruturas de dados.

Demonstrar entendimento da árvore binária de busca.

Gerar visualização da árvore de forma dinâmica.

Integrar Python + Django na construção de um sistema funcional.

Permitir manipulação da árvore em tempo real.

Apresentar interface simples e instrutiva ao usuário.

🛠️ Tecnologias Utilizadas
Tecnologia	Função
Python 3.12+	Lógica da árvore e backend
Django 5.2	Framework web
HTML5 + CSS3	Interface e layout
SVG	Renderização da árvore binária
Matplotlib (opcional)	Ferramentas gráficas (não obrigatório)
NetworkX (opcional)	Manipulação de grafos (não obrigatório)
🚀 Como Executar o Projeto
✔️ 1. Clonar o repositório
git clone https://github.com/thiago-de-mattos/Arvore-Binaria-de-Busca.git
cd Arvore-Binaria-de-Busca

✔️ 2. Criar e ativar o ambiente virtual
Windows:
python -m venv venv
venv\Scripts\activate

Linux/Mac:
python3 -m venv .venv
source venv/bin/activate

✔️ 3. Instalar dependências

pip install -r requirements.txt

✔️ 4. Realizar migrações do Django
python manage.py migrate

✔️ 5. Rodar o servidor
python manage.py runserver

Acesse:

http://127.0.0.1:8000/

🧬 Arquitetura do Projeto
arvore_binaria/
│── arvore.py            # Classe principal da árvore binária de busca
│── views.py             # Controladores das rotas
│── urls.py              # Mapeamento de URLs
│── templates/
│   ├── index.html       # Página inicial
│   └── arvore.html      # Visualização da árvore em SVG
│── static/
│   └── css/style.css    # Estilos visuais
│── migrations/          # Migrations padrão do Django

📊 Como funciona a Árvore Binária no Projeto

A classe Arvore implementa:

✔️ Inserção (insert)

Insere valores mantendo as propriedades da ABB.

✔️ Busca (search)

Localiza valores de forma recursiva.

✔️ Remoção (delete)

Remove mantendo a estrutura válida da árvore.

✔️ Conversão para estrutura gráfica

Transforma nós em coordenadas para exibição em SVG.

✔️ Renderização em árvore

A árvore é desenhada com:

linhas representando arestas

círculos para os nós

valores centralizados

Tudo implementado manualmente, sem bibliotecas de gráficos obrigatórias.

🎨 Interface do Usuário

A interface HTML permite:

Inserir lista inicial de valores

Visualizar a árvore em SVG

Inserir novo elemento

Remover elemento existente

Pesquisar valor específico

Ver mensagens de feedback (encontrado, removido, inexistente etc.)

🧪 Testes

O projeto utiliza:

testes manuais

logs de depuração

conferência visual da árvore

Se necessário, podem ser adicionados testes unitários.

👨‍🎓 Autor

Thiago de Mattos Azevedo Chaves
Universidade de Vassouras – Campus Maricá
Curso: Engenharia de Software
Disciplina: Estrutura de Dados

📄 Licença

Este projeto é destinado ao uso acadêmico e demonstração do aprendizado.
Sua reprodução é permitida para fins educacionais.
