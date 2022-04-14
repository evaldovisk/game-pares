from random import sample


def mostra(lista):
    '''Função que mostra para o usuário a matriz;
    Entrada: list
    Saída: None '''
    for lin in lista:
        for col in lin:
            print(col, end=' ')
        print('')
    return None


def posicao_xy(opcao, lista):
    '''Função que pergunta as coordenas fazendo a verificação pedida;
    Entrada: Str, list
    Saída: int, int '''
    verificado = False
    x, y = 0, 0
    while not verificado:
        posicao = input('\nEscolha a {} posição [x,y]: '.format(opcao)).replace(' ', '')
        x, y = int(posicao[3]), int(posicao[1])
        if x > 3 or x < 0 or y > 3 or y < 0:
            print('\nPosição Invalida. ', end='')
        elif lista[x][y] != '*':
            print('\nPosição Já descoberta. ', end='')
        else:
            verificado = True
    return x, y

def main():
    '''Função principal que executa o jogo da memória;
    Entrada: None
    Saída: None '''

    print('------------------ Bem Vindo ao Jogo da Memória ------------------')
    print('Este é o jogo da memória, siga as instruções e se divirta!\n')

    num = sample([1, 2, 3, 4, 5, 6, 7, 8] * 2, 16)
    numero = [num[0:4], num[4:8], num[8:12], num[12:16]]
    escondido = [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]

    acertos = 0
    jogadas = 0
    while acertos != 8:
        jogadas += 1
        mostra(escondido)

        p1x, p1y = posicao_xy('primeira', escondido)
        escondido[p1x][p1y] = numero[p1x][p1y]
        mostra(escondido)

        p2x, p2y = posicao_xy('segunda', escondido)
        escondido[p2x][p2y] = numero[p2x][p2y]
        mostra(escondido)

        if numero[p1x][p1y] == numero[p2x][p2y]:
            print('\nParabéns!! Você acertou\n')
            acertos += 1
        else:
            print('\nVocê errou... tente de novo.\n')
            escondido[p1x][p1y], escondido[p2x][p2y] = '*', '*'

    print('Parabéns!! Você conseguiu descobrir todas as casas em {} jogadas'.format(jogadas))

main()


#TESTE DE  MESA

'''------------------ Bem Vindo ao Jogo da Memória ------------------
Este é o jogo da memória, siga as instruções e se divirta!

* * * * 
* * * * 
* * * * 
* * * * 

Escolha a primeira posição [x,y]: [5,3]

Posição Invalida. 
Escolha a primeira posição [x,y]: [0,0]
6 * * * 
* * * * 
* * * * 
* * * * 

Escolha a segunda posição [x,y]: [3,3]
6 * * * 
* * * * 
* * * * 
* * * 1 

Você errou... tente de novo.

* * * * 
* * * * 
* * * * 
* * * * 

Escolha a primeira posição [x,y]: [2,2]
* * * * 
* * * * 
* * 8 * 
* * * * 

Escolha a segunda posição [x,y]: [1,1]
* * * * 
* 2 * * 
* * 8 * 
* * * * 

Você errou... tente de novo.

* * * * 
* * * * 
* * * * 
* * * * 

Escolha a primeira posição [x,y]: [3,0]
* * * * 
* * * * 
* * * * 
5 * * * 

Escolha a segunda posição [x,y]: [0,3]
* * * 6 
* * * * 
* * * * 
5 * * * 

Você errou... tente de novo.

* * * * 
* * * * 
* * * * 
* * * * 

Escolha a primeira posição [x,y]: [0,3]
* * * 6 
* * * * 
* * * * 
* * * * 

Escolha a segunda posição [x,y]: [0,0]
6 * * 6 
* * * * 
* * * * 
* * * * 

Parabéns!! Você acertou

6 * * 6 
* * * * 
* * * * 
* * * * 

Escolha a primeira posição [x,y]: [0,1]
6 5 * 6 
* * * * 
* * * * 
* * * * 

Escolha a segunda posição [x,y]: [3,0]
6 5 * 6 
* * * * 
------------------ Bem Vindo ao Jogo da Memória ------------------
Este é o jogo da memória, siga as instruções e se divirta!

* * * * 
* * * * 
* * * * 
* * * * 

Escolha a primeira posição [x,y]: [0,0]
4 * * * 
* * * * 
* * * * 
* * * * 

Escolha a segunda posição [x,y]: [3,3]
4 * * * 
* * * * 
* * * * 
* * * 2 

Você errou... tente de novo.

* * * * 
* * * * 
* * * * 
* * * * 

Escolha a primeira posição [x,y]: [1,1]
* * * * 
* 2 * * 
* * * * 
* * * * 

Escolha a segunda posição [x,y]: [3,3]
* * * * 
* 2 * * 
* * * * 
* * * 2 

Parabéns!! Você acertou

* * * * 
* 2 * * 
* * * * 
* * * 2 

Escolha a primeira posição [x,y]: [3,5]

Posição Invalida. 
Escolha a primeira posição [x,y]: [3,3]

Posição Já descoberta. 
Escolha a primeira posição [x,y]: [0,3]
* * * 7 
* 2 * * 
* * * * 
* * * 2 

Escolha a segunda posição [x,y]: [3,0]
* * * 7 
* 2 * * 
* * * * 
5 * * 2 

Você errou... tente de novo.

* * * * 
* 2 * * 
* * * * 
* * * 2 

Escolha a primeira posição [x,y]: [3,1]
* * * * 
* 2 * * 
* * * * 
* 6 * 2 

Escolha a segunda posição [x,y]: [3,2]
* * * * 
* 2 * * 
* * * * 
* 6 4 2 

Você errou... tente de novo.

* * * * 
* 2 * * 
* * * * 
* * * 2 

Escolha a primeira posição [x,y]: [3,2]
* * * * 
* 2 * * 
* * * * 
* * 4 2 

Escolha a segunda posição [x,y]: [0,0]
4 * * * 
* 2 * * 
* * * * 
* * 4 2 

Parabéns!! Você acertou

4 * * * 
* 2 * * 
* * * * 
* * 4 2 

Escolha a primeira posição [x,y]: [0,1]
4 1 * * 
* 2 * * 
* * * * 
* * 4 2 

Escolha a segunda posição [x,y]: [1,2]
4 1 * * 
* 2 8 * 
* * * * 
* * 4 2 

Você errou... tente de novo.

4 * * * 
* 2 * * 
* * * * 
* * 4 2 

Escolha a primeira posição [x,y]: [2,1]
4 * * * 
* 2 * * 
* 3 * * 
* * 4 2 

Escolha a segunda posição [x,y]: [2,3]
4 * * * 
* 2 * * 
* 3 * 6 
* * 4 2 

Você errou... tente de novo.

4 * * * 
* 2 * * 
* * * * 
* * 4 2 

Escolha a primeira posição [x,y]: [2,3]
4 * * * 
* 2 * * 
* * * 6 
* * 4 2 

Escolha a segunda posição [x,y]: [3,1]
4 * * * 
* 2 * * 
* * * 6 
* 6 4 2 

Parabéns!! Você acertou

4 * * * 
* 2 * * 
* * * 6 
* 6 4 2 

Escolha a primeira posição [x,y]: [1,3]
4 * * * 
* 2 * 8 
* * * 6 
* 6 4 2 

Escolha a segunda posição [x,y]: [1,2]
4 * * * 
* 2 8 8 
* * * 6 
* 6 4 2 

Parabéns!! Você acertou

4 * * * 
* 2 8 8 
* * * 6 
* 6 4 2 

Escolha a primeira posição [x,y]: [0,2]
4 * 3 * 
* 2 8 8 
* * * 6 
* 6 4 2 

Escolha a segunda posição [x,y]: [2,1]
4 * 3 * 
* 2 8 8 
* 3 * 6 
* 6 4 2 

Parabéns!! Você acertou

4 * 3 * 
* 2 8 8 
* 3 * 6 
* 6 4 2 

Escolha a primeira posição [x,y]: [1,0]
4 * 3 * 
1 2 8 8 
* 3 * 6 
* 6 4 2 

Escolha a segunda posição [x,y]: [0,1]
4 1 3 * 
1 2 8 8 
* 3 * 6 
* 6 4 2 

Parabéns!! Você acertou

4 1 3 * 
1 2 8 8 
* 3 * 6 
* 6 4 2 

Escolha a primeira posição [x,y]: [2,0]
4 1 3 * 
1 2 8 8 
5 3 * 6 
* 6 4 2 

Escolha a segunda posição [x,y]: [3,0]
4 1 3 * 
1 2 8 8 
5 3 * 6 
5 6 4 2 

Parabéns!! Você acertou

4 1 3 * 
1 2 8 8 
5 3 * 6 
5 6 4 2 

Escolha a primeira posição [x,y]: [0,3]
4 1 3 7 
1 2 8 8 
5 3 * 6 
5 6 4 2 

Escolha a segunda posição [x,y]: [2,2]
4 1 3 7 
1 2 8 8 
5 3 7 6 
5 6 4 2 

Parabéns!! Você acertou

Parabéns!! Você conseguiu descobrir todas as casas em 13 jogadas'''
