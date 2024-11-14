def pesquisa_binaria(lista, item):  #Define a função, sendo seu nome pesquisa_binaria e seus parâmetros lista e item
    baixo = 0 #Estabelece o começo da lista. Este 0 é a posição do termo
    alto = len(lista) - 1 #Define o "final" da lista, o último termo dela. O "-1" serve para igualar o contador, porque se conta a lista a partir do 0
    contador = 0

    while baixo <= alto:
        contador += 1
        
        meio = int((baixo + alto) / 2) #O filtro da lista, sendo o começo da pesquisa binária
        chute = lista[meio] #Armazena o meio da lista de forma já filtrada, ou seja, o resultado da conta. A posição do número buscado
        resto = alto - meio
        print(f'Contador: {contador} Resto: {resto}')

        if chute == item:
            return meio
            #"Se chute for igual o item, retornar o resultado (item) para a variável meio"
        
        if chute > item:
            alto = meio - 1
            #"Se chute for maior que item, ajusta o índice alto para buscar na metade inferior da lista"
            #Meio que o valor de alto se torna o resultado da conta meio (linha 9), refazendo a conta até conseguir achar a posição do número chutado
        else:
            baixo = meio + 1
            #"Se chute for menor que item, ajusta o índice baixo para buscar na metade superior da lista"
            #Meio que o valor de baixo se torna o resultado da conta meio (linha 9)

    return -1

listaComCem= [6,8,15,16,27,36,44,44,50,51,68,82,89,99,105,108,111,128,129,141,150,151,153,162,180, 197,213,239,252,264,273,275,293,322,340,343,348,351,353,356,357,368,370,381,387,387,410,42,8,432,437,474,500,535,544,551,568,569,580,584,594,605,625,650,653,659,667,673,685,691,698,720,744,745,749,782,791,797,806,817,819,821,822,850,850,870,870,885,908,912,913,91,7,917,926,931,944,966,972,991,998, 1000]

print(f"O Index do número buscado é: {pesquisa_binaria(listaComCem, 998)}")