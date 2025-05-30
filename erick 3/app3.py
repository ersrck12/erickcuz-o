#python
# jogo da velha (tic tac toe) em python
# tabuleiro representado por uma lista de 9 posicoes (inicialmente vazias)
board = ['' for _ in range (9)]
def print_board():
    """
    
    exibe o tabuleiro atual formatado com as marcaçoedos jogadores
    formato:
    | X | o | X |
    | o | o | o |
    | X | o | X |
    """

    #cria cada linha do tabuleiro usando a formaçao de string
    row = '|  {}  |  {}  |  {}  |'.format(board [0], board[1], board[2]) 
    row = '|  {}  |  {}  |  {}  |'.format(board [3], board[4], board[5])
    row = '|  {}  |  {}  |  {}  |'.format(board [6], board[7], board[8])

    # Exibe o tabuleiro completo
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

 def player_move(icon):
       """
       gerencia a jogada de um participante
       :para icon: 'x' ou'0' - simbolo do jogador atual
       """
# determina o numero do jogador baseadono simbolo
       if icon == 'x':
             number == 1
       elif icon == '0':
             number = 2

    print("sua vez, jogador {}".format(number))
# Loop para entrada valida da jogada
while True:
      try:
# converte a entrada  para numero e ajusta para indice 0-8
            choice = int(input("digite sua jogada (1-9):").strip()) - 1

# valida se a posição esta disponivel
         if board[choice] == ' ':
             board[choice] = icon
             break
         else:
             print("nEsta")                  
