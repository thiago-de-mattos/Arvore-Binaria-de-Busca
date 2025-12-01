from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .arvore import Arvore, No  # seu arquivo de classes
import json

# ----- Helpers para converter JSON <-> Arvore (usa suas classes No e Arvore) -----
def reconstruir_no(json_no):
    """Converte dicionário (gerado por converter_para_json) para instância No recursivamente."""
    if json_no is None:
        return None
    no = No(json_no['valor'])
    no.esquerda = reconstruir_no(json_no.get('esquerda'))
    no.direita = reconstruir_no(json_no.get('direita'))
    return no

def reconstruir_arvore_de_json(json_root):
    arv = Arvore()
    if json_root is None:
        return arv
    arv.raiz = reconstruir_no(json_root)
    return arv

# ----- Função que monta lista de nós + arestas com posições para SVG -----
def construir_nos_e_arestas(json_root, width=1000, level_height=100):
    """
    Retorna dict:
      {
        'nodes': [{'id': id, 'valor': v, 'x': x, 'y': y}],
        'edges': [{'from': parent_id, 'to': child_id}]
      }
    Estrutura baseada na travessia inorder para definir x (posição horizontal).
    """

    nodes = []
    edges = []
    id_counter = {'v': 0}
    inorder_index = {'v': 0}

    # cria uma estrutura de objetos intermediários para atribuir ids
    def criar_ids(e):
        if e is None:
            return None
        id_counter['v'] += 1
        myid = id_counter['v']
        # retorna tupla (id, json_node, left, right) - vamos armazenar temporariamente
        left = criar_ids(e.get('esquerda'))
        right = criar_ids(e.get('direita'))
        return {'id': myid, 'node': e, 'left': left, 'right': right, 'depth': None, 'inorder': None}

    raiz = criar_ids(json_root)

    # atribuir profundidade (depth)
    def atribuir_depth(obj, depth=0, parent_id=None):
        if obj is None:
            return
        obj['depth'] = depth
        obj['parent_id'] = parent_id
        atribuir_depth(obj['left'], depth + 1, obj['id'])
        atribuir_depth(obj['right'], depth + 1, obj['id'])

    atribuir_depth(raiz)

    # inorder traversal para definir indices horizontais
    def inorder_atribuir(obj):
        if obj is None:
            return
        inorder_atribuir(obj['left'])
        inorder_index['v'] += 1
        obj['inorder'] = inorder_index['v']
        inorder_atribuir(obj['right'])

    inorder_atribuir(raiz)

    total = inorder_index['v'] if inorder_index['v'] > 0 else 1
    padding = 40
    usable_width = max(width - 2 * padding, 100)

    # gerar nodes com posições x,y
    def coletar(obj):
        if obj is None:
            return
        # x baseado no inorder index
        x = padding + (obj['inorder'] * (usable_width / (total + 1)))
        y = padding + (obj['depth'] * level_height)
        nodes.append({
            'id': obj['id'],
            'valor': obj['node']['valor'],
            'x': round(x, 2),
            'y': round(y, 2),
            'parent_id': obj.get('parent_id')
        })
        if obj.get('parent_id') is not None:
            edges.append({'from': obj.get('parent_id'), 'to': obj['id']})
        coletar(obj['left'])
        coletar(obj['right'])

    coletar(raiz)

    return {'nodes': nodes, 'edges': edges, 'width': width, 'height': ( (max([n['y'] for n in nodes]) + padding) if nodes else 200 )}

# ----- Views -----
def index(request):
    # Página inicial com textarea
    return render(request, 'index.html')

def gerar_arvore(request):
    if request.method == 'POST':
        numeros_texto = request.POST.get('numeros', '').strip()
        if not numeros_texto:
            return render(request, 'index.html', {'erro': 'Insira pelo menos um número.'})

        try:
            lista = [int(x) for x in numeros_texto.split()]
        except ValueError:
            return render(request, 'index.html', {'erro': 'A entrada deve conter apenas números separados por espaço.'})

        arv = Arvore()
        for n in lista:
            arv.adicionar_numero(n)

        # balanceia
        arv.reorganizar_arvore_balanceada()

        # salva na sessão como JSON (serializável)
        request.session['arvore'] = arv.converter_para_json()
        request.session.modified = True

        return redirect('arvore')
    return redirect('index')

def ver_arvore(request):
    arv_json = request.session.get('arvore')
    # construir nodes+edges para SVG
    svg_data = construir_nos_e_arestas(arv_json)
    return render(request, 'arvore.html', {'svg': svg_data})

def executar_acao(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        try:
            valor = int(request.POST.get('valor'))
        except (ValueError, TypeError):
            return redirect('arvore')

        arv_json = request.session.get('arvore')
        arv = reconstruir_arvore_de_json(arv_json)

        msg = ''
        if tipo == 'inserir':
            arv.adicionar_numero(valor)
            msg = f'Valor {valor} inserido.'
        elif tipo == 'remover':
            arv.remover_numero(valor)
            msg = f'Valor {valor} removido (se existia).'
        elif tipo == 'buscar':
            encontrado = arv.procurar_numero(valor)
            msg = f'Valor {valor} {"encontrado" if encontrado else "não encontrado"}.'
            # não precisa alterar a árvore ao buscar
            request.session['arvore'] = arv.converter_para_json()
            request.session.modified = True
            svg_data = construir_nos_e_arestas(request.session.get('arvore'))
            return render(request, 'arvore.html', {'svg': svg_data, 'mensagem': msg})

        # após inserir/remover, balancear e salvar
        arv.reorganizar_arvore_balanceada()
        request.session['arvore'] = arv.converter_para_json()
        request.session.modified = True

        svg_data = construir_nos_e_arestas(request.session.get('arvore'))
        return render(request, 'arvore.html', {'svg': svg_data, 'mensagem': msg})

    return redirect('arvore')