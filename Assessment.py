"""
    Questão 03 - 

    Um aplicativo de mensagens precisa buscar um contato pelo nome em uma 
    lista de contatos não ordenada. Implemente o algoritmo de busca linear 
    para encontrar um nome específico e exibir o número de telefone correspondente.

"""


lista_de_contatos = [
    {"nome":"Jose", "numero": "2192839282938"},{"nome":"flavio", "numero": "2192839282938"},{"nome":"roberto", "numero": "2192839282938"},{"nome":"josue", "numero": "2192839282938"},{"nome":"marcos", "numero": "2192839282938"},{"nome":"marcus", "numero": "2192839282938"},{"nome":"joao", "numero": "2192839282938"}
]
print("=-" * 6 + " Questão 03 " + "=-"* 6)
print(f"\nBuscando contato em um total de {len(lista_de_contatos)} contatos...")
def busca_contato(nome_contato):
    for contato in lista_de_contatos:
        if contato["nome"].upper() == nome_contato.upper():
            return contato
    return None

retorno  = busca_contato("roberto")

if retorno:
    print(f"""\nContato encontrado!\n\nNome:{retorno["nome"]}\n\nTelefone:{retorno["numero"]}
""")
else:
    print("Número não encontrado.")
print("=-" * 15)


"""

    Questão 04 - Implemente o algoritmo de busca binária para localizar um ISBN específico em
    uma lista ordenada de 100 mil livros de uma biblioteca digital. Teste o algoritmo e compare 
    o número de iterações com uma busca linear para o mesmo problema.

"""


lista_de_livros = list(range(1, 100001))

def busca_binaria(ISBN):
    inicio = 0
    contador = 0
    fim  = len(lista_de_livros) -1
    while inicio <= fim:
        contador += 1
        meio = (inicio + fim )// 2
        if lista_de_livros[meio] == ISBN:
            return contador
        elif lista_de_livros[meio] < ISBN:
            inicio = meio + 1
        else:
            fim = meio - 1
    return

def busca_linear(ISBN):
    contador = 0
    for i in lista_de_livros:
        
        if i == ISBN:
            return contador
        contador += 1
    return 


interacoes_binaria = busca_binaria(10219)
interacoes_linear = busca_linear(10219)

print(f"""
A busca linear obteve {interacoes_linear} interações.\n\nA busca binária obteve {interacoes_binaria} interações.""")


"""
    Questão 06 - Implemente o Bubble Sort para organizar uma lista de preços de produtos. 
    Teste o algoritmo com 1 mil e 10 mil elementos, meça o tempo de execução e explique 
    por que o desempenho é impactado pelo aumento da quantidade de dados.
"""
import time
import random

precos = [random.randint(1, 1000) for _ in range(1000)]
precos2 = [random.randint(1, 10000) for _ in range(10000)]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
inicio = time.time()
bubble_sort(precos)
fim = time.time()
print("-=" * 15)
print(f"""\nLista com {len(precos)}, demorando {fim-inicio}.""")

inicio = time.time()
bubble_sort(precos2)
fim = time.time()

print(f"""\nLista com {len(precos2)}, demorando {fim-inicio}./n""")
print("-=" * 15)

"""

    Questão 07 - Um programador criou um algoritmo para verificar se há duplicatas em uma lista, 
    mas o algoritmo atual tem complexidade O(n2). Reescreva o código para usar um hashtable e otimize
    o tempo de execução para O(n). Justifique suas escolhas.

"""

def verifica_duplicada(lista):
    lista2 = set()  
    for item in lista:
        if item in lista2:  
            return True  
        lista2.add(item)  
    return False  



"""
    Questão 08 - Crie um algoritmo de Selection Sort para organizar os registros de jogadores por pontuação em um jogo online. 
    Explique cada etapa do algoritmo e sua complexidade em Big O.

"""

def SelectionSort(registros):
    for i in range(len(registros)):
        indice_minimo = i
        for j in range(i+1, len(registros)):
            if registros[j]['points'] < registros[indice_minimo]['points']:
                indice_minimo = j
            registros[i], registros[indice_minimo] = registros[indice_minimo], registros[i]
    
    return registros

registros = [
    {'nick': 'user1', 'points': 0},
    {'nick': 'user2', 'points': 25},
    {'nick': 'user3', 'points': 20},
    {'nick': 'user4', 'points': 73},
    {'nick': 'user5', 'points': 50},
    {'nick': 'user6', 'points': 40},
    {'nick': 'user7', 'points': 1340},
    {'nick': 'user8', 'points': 2},
]
registros_ordenados =  SelectionSort(registros)

print(registros)

"""

    Questão 09 - Um sistema de rede social precisa recuperar rapidamente o perfil de um usuário com base em seu nome de usuário. 
    Implemente uma hashtable para armazenar e recuperar informações de perfil, e mostre como essa abordagem é mais eficiente do que 
    percorrer uma lista sequencialmente.

"""


class redeSocial:
    def __init__(self):
        self.perfis = {}  

    def add(self, nome, perfil):
        self.perfis[nome] = perfil

    def get(self, nome):
        return self.perfis.get(nome)
    
cadastro = redeSocial()

cadastro.add("José Augusto",{"nome": "José Augusto", "idade": 20})
cadastro.add("Lucas",{"nome": "Lucas", "idade": 24})
cadastro.add("Jorge",{"nome": "Jorge", "idade": 45})

perfil = cadastro.get("José Augusto")

"""

    Questão 10 - Implemente uma pilha (stack) para simular um sistema de navegação no navegador,
    onde o usuário pode usar os botões "Voltar" e "Avançar" para navegar entre páginas.

"""

class Navegador:
    def __init__(self):
        self.sites = []  
        self.site_atual = ""

    def ir_para(self, pagina):
        if len(self.sites) > 0:
            index = self.sites.index(self.site_atual)
            for i in range(index , len(self.sites) -1):
                self.sites.pop()
        self.sites.append(pagina)
        self.site_atual = pagina
        

    def voltar(self):
        indice =  self.sites.index(self.site_atual)
        if indice > 0:
            self.site_atual = self.sites[indice - 1]

    def avancar(self):
        indice =  self.sites.index(self.site_atual)
        if indice +1 <= len(self.sites) -1:
            self.site_atual = self.sites[indice + 1]

    def site(self):
        return f"Página atual: {self.site_atual}"

nav = Navegador()
nav.ir_para("www.google.com")
pag_atual = nav.site()
print(pag_atual)
nav.ir_para("www.yahoo.com")
nav.ir_para("www.utorrent-gta6.com")
pag_atual = nav.site()
print(pag_atual)
nav.voltar()
pag_atual = nav.site()
print(pag_atual)
nav.avancar()
pag_atual = nav.site()
print(pag_atual)
nav.voltar()

"""
    Questão 11 - Um sistema de atendimento ao cliente organiza os chamados na ordem em que chegam. 
    Implemente uma fila (queue) para gerenciar essa ordem e simule a inserção e remoção de chamados do sistema.

"""

class chamados:
    def __init__(self):
        self.fila = []  

    def adicionar_chamado(self, chamado):
        self.fila.append(chamado)

    def atender_chamado(self):
        if self.fila:
            chamado = self.fila.pop(0)  
            return chamado
        else:
            return None

    def exibir_fila(self):
        if self.fila:
            print(f"Chamados na fila: {self.fila}")
        else:
            print("A fila está vazia.")


"""

    Questões 12 - Implemente um algoritmo recursivo que percorra todos os subdiretórios de uma pasta e liste somente os arquivos. 
    Explique como a recursão resolve o problema de explorar diretórios aninhados.

"""

import os

def diretorios(caminho):
    pastas = os.listdir(caminho)
    for item in pastas:
        caminho_item = os.path.join(caminho, item)
        if os.path.isfile(caminho_item):
            print(caminho_item)
        elif os.path.isdir(caminho_item):
            diretorios(caminho_item)


"""

"""


def mochila(pesos, valores, capacidade):
    n = len(pesos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(capacidade + 1):
            if pesos[i - 1] <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][c] = dp[i - 1][c]
    
    return dp[n][capacidade]

pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 8

print(mochila(pesos, valores, capacidade))




"""
"""
class BST:
    def __init__(self):
        self.raiz = None

    def insert(self, raiz, valor):
        if valor is None:
            return [valor, None, None]  
        if valor < raiz[0]:
            raiz[1] = self.insert(raiz[1], valor)
        elif valor > raiz[0]:
            raiz[2] = self.insert(raiz[2], valor)
        return raiz

    def search(self, raiz, valor):
        if valor is None:
            return False
        if valor == raiz[0]:
            return True
        if valor < raiz[0]:
            return self.search(raiz[1], valor)
        return self.search(raiz[2], valor)

bst = BST()
prices = [100, 50, 150, 30, 70, 130, 170]
for price in prices:
    bst.root = bst.insert(bst.root, price)


"""

"""

class BST:
    def __init__(self):
        self.valores = None

    def inserir(self, valores, key):
        if valores is None:
            return [key, None, None]  
        if key < valores[0]:
            valores[1] = self.insert(valores[1], key)
        elif key > valores[0]:
            valores[2] = self.insert(valores[2], key)
        return valores

    def min(self, valores):
        if valores is None:
            return None
        while valores[1] is not None:
            valores = valores[1]
        return valores[0]

    def max(self, valores):
        if valores is None:
            return None
        while valores[2] is not None:
            valores = valores[2]
        return valores[0]

bst = BST()
notas = [85, 70, 95, 60, 75, 90, 100]
for nota in notas:
    bst.valores = bst.inserir(bst.valores, nota)

min = bst.min(bst.valores)
max = bst.max(bst.valores)

print(f"Nota mínima: {min}")
print(f"Nota máxima: {max}")



class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valores, chave):
        if valores is None:
            return [chave, None, None]
        if chave < valores[0]:
            valores[1] = self.inserir(valores[1], chave)
        elif chave > valores[0]:
            valores[2] = self.inserir(valores[2], chave)
        return valores

    def encontrar_min(self, valores):
        while valores and valores[1]:
            valores = valores[1]
        return valores[0] if valores else None

    def remover(self, valores, chave):
        if valores is None:
            return None
        if chave < valores[0]:
            valores[1] = self.remover(valores[1], chave)
        elif chave > valores[0]:
            valores[2] = self.remover(valores[2], chave)
        else:
            if valores[1] is None:
                return valores[2]
            if valores[2] is None:
                return valores[1]
            min_valor = self.encontrar_min(valores[2])
            valores[0] = min_valor
            valores[2] = self.remover(valores[2], min_valor)
        return valores

    def em_ordem(self, valores):
        if valores is None:
            return []
        return self.em_ordem(valores[1]) + [valores[0]] + self.em_ordem(valores[2])


bst = BST()
codigos = [45, 25, 65, 20, 30, 60, 70]
for codigo in codigos:
    bst.raiz = bst.inserir(bst.raiz, codigo)

def exibir_arvore(bst, mensagem):
    print(mensagem, bst.em_ordem(bst.raiz))

exibir_arvore(bst, "Árvore inicial:")
bst.raiz = bst.remover(bst.raiz, 20)
exibir_arvore(bst, " (nó folha):")
bst.raiz = bst.remover(bst.raiz, 25)
exibir_arvore(bst, " (nó com um filho):")
bst.raiz = bst.remover(bst.raiz, 45)
exibir_arvore(bst, " (nó com dois filhos):")
