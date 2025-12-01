class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class Arvore:
    def __init__(self):
        self.raiz = None
    
    def adicionar_numero(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._descer_e_inserir(self.raiz, valor)
    
    def _descer_e_inserir(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._descer_e_inserir(no_atual.esquerda, valor)
        else: 
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._descer_e_inserir(no_atual.direita, valor)
    
    def procurar_numero(self, valor):
        return self._descer_e_procurar(self.raiz, valor)
    
    def _descer_e_procurar(self, no_atual, valor):
        if no_atual is None:
            return False  
        
        if no_atual.valor == valor:
            return True  
        
        elif valor < no_atual.valor:
            return self._descer_e_procurar(no_atual.esquerda, valor)
        else:
            return self._descer_e_procurar(no_atual.direita, valor)

    def remover_numero(self, valor):
        self.raiz = self._descer_e_remover(self.raiz, valor)

    def _descer_e_remover(self, no_atual, valor):
        if no_atual is None:
            return None
        
        if valor < no_atual.valor:
            no_atual.esquerda = self._descer_e_remover(no_atual.esquerda, valor)
        
        elif valor > no_atual.valor:
            no_atual.direita = self._descer_e_remover(no_atual.direita, valor)
        
        else:
            if no_atual.esquerda is None:
                return no_atual.direita 
            
            elif no_atual.direita is None:
                return no_atual.esquerda 

            menor_da_direita = self._achar_menor_no(no_atual.direita)
            
            no_atual.valor = menor_da_direita.valor

            no_atual.direita = self._descer_e_remover(no_atual.direita, menor_da_direita.valor)
        
        return no_atual

    def _achar_menor_no(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def listar_numeros_ordenados(self):
        lista_numeros = []
        self._percorrer_em_ordem(self.raiz, lista_numeros)
        return lista_numeros   
    
    def _percorrer_em_ordem(self, no_atual, lista_numeros):
        if no_atual is not None:
            self._percorrer_em_ordem(no_atual.esquerda, lista_numeros)

            lista_numeros.append(no_atual.valor)

            self._percorrer_em_ordem(no_atual.direita, lista_numeros)

    def reorganizar_arvore_balanceada(self):
        numeros = self.listar_numeros_ordenados()

        self.raiz = None

        self._inserir_lista_balanceada(numeros)

    def _inserir_lista_balanceada(self, numeros):

        if len(numeros) == 0:
            return
        
        meio = len(numeros) // 2
        self.adicionar_numero(numeros[meio])
        
        self._inserir_lista_balanceada(numeros[:meio])
        
        self._inserir_lista_balanceada(numeros[meio + 1:])

    def converter_para_json(self):

        return self._converter_no_para_dicionario(self.raiz)

    def _converter_no_para_dicionario(self, no):
   
        if no is None:
            return None
        
        return {
            'valor': no.valor,
            'esquerda': self._converter_no_para_dicionario(no.esquerda),
            'direita': self._converter_no_para_dicionario(no.direita)
        }