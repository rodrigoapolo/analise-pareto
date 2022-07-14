#Autor: Rodrigo Apolo
#github: https://github.com/rodrigoapolo

# Programa irá executar a análise de Pareto através de entrada de dados txt

#remove duplicatas
def remove_duplicatas(lista):
    """ recebe lista como argumento, remove duplicatas e altera contador """
    print(1)
    d = []
    con=0
    for i in lista:
        if i not in d:
            d.append(i)
        else:
            con = con+1
    d.sort()
    return d
    
# Criar uma matriz 
def criar_matriz (n_linhas, n_colunas):
    print(2)
    matriz = []

    for _ in range(n_linhas+1):
        matriz.append( [0] * n_colunas )

    matriz[n_linhas][0]='Total'
    return matriz

#Gerar uma Tabela
def gerar_matriz(defeito = [],cantidade = []):
    
    print(3)
    tabela = criar_matriz(len(defeito),4)
    #tabela = [[0]*4]*len(vetor)
    x = 0
    for i in defeito:
        tabela[x][0] = i
        x += 1
    
    x=0
    for i in cantidade:
        tabela[x][1] = i
        x += 1
    
    return tabela
    
#Somar Total de defeito
def somaTotal (lista):
    print(4)
    somaTotal = 0
    for i in range(0,len(lista)):
        somaTotal += lista[i][1]
    
    lista[(len(lista)-1)][1]=somaTotal
    
#Percentual dos Defeitos
def percentualDefeitos(lista):
    print(5)
    for i in range(0,len(lista)):
        lista[i][2]=(lista[i][1]/lista[(len(lista)-1)][1])*100

### Execução começa por aqui ###

#Ler o arquivo
dados = open("dados.txt", "r")

#Coloca o arquivo em uma lista, separando um conceito por linha 
Lista = dados.read().split('\n')

# criar registros únicos retornados 
vetor = remove_duplicatas(Lista)

contador = []

#Conta a quantidade de defeito
for i in vetor:
    contador.append(Lista.count(i))
       
#Cria a tabela 
tabela = gerar_matriz(vetor,contador)
        
#Ordenada a tabela
ListaOrdenada = sorted(tabela,key=lambda l:l[1], reverse=True)

#Soma o total de defeito
somaTotal(ListaOrdenada)

#ADD o percentual do defeitos 
percentualDefeitos(ListaOrdenada)

#Soma da frequênci acumulativa
for i in range(0,len(ListaOrdenada)-1):
    
    if i==0:
        ListaOrdenada[0][3] =ListaOrdenada[0][2]
    else:
        ListaOrdenada[i][3] =ListaOrdenada[(i)-1][3]+ListaOrdenada[i][2]


#formatando os numeros em %
for i in range(0,len(ListaOrdenada)-1):
    
    ListaOrdenada[i][2] =f'{ListaOrdenada[i][2]:.2f}%'
    ListaOrdenada[i][3] =f'{ListaOrdenada[i][3]:3.2f}%'
    
  
#Formatando os defeitos
tamanhString = 0
for i in range(0,len(ListaOrdenada)-1):
    
    valor = int(len(ListaOrdenada[i][0]))
    if tamanhString<valor:
        tamanhString = valor
        
        
for i in range(0,len(ListaOrdenada)):
    
    valor = int(len(ListaOrdenada[i][0]))
    if tamanhString>valor:
        for j in range(0,tamanhString-valor):
            ListaOrdenada[i][0] = ListaOrdenada[i][0]+" "
            
#formatando Quantidade      
tamanhoQuantidade = 0
for i in range(0,len(ListaOrdenada)):
    
    valor =  len(str(ListaOrdenada[i][1]))
    if tamanhoQuantidade<valor:
        tamanhoQuantidade = valor

for i in range(0,len(ListaOrdenada)):
    
    valor = len(str(ListaOrdenada[i][1]))
    if tamanhoQuantidade>valor:
        for j in range(0,tamanhoQuantidade-valor):
            ListaOrdenada[i][1] = f'0{ListaOrdenada[i][1]}'
            


ListaOrdenada[len(ListaOrdenada)-1][1] = f'{ListaOrdenada[len(ListaOrdenada)-1][1]}'
ListaOrdenada[len(ListaOrdenada)-1][2] = f'{ListaOrdenada[len(ListaOrdenada)-1][2]:.1f}%'
ListaOrdenada[len(ListaOrdenada)-1][3] = ListaOrdenada[len(ListaOrdenada)-2][3]

#Mosta o resultado
for i in ListaOrdenada:
   print(i)  
    
 


    


