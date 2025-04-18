from hexGame import JogoHex

if __name__ == "__main__":
    print("=== Bem-vindo ao Jogo Hex ===")
    print("O jogador X deve conectar a esquerda à direita")
    print("O jogador O deve conectar o topo à base")
    
    tamanho = 11
    try:
        tamanho_input = int(input("Digite o tamanho do tabuleiro (3-11, padrão: 11): "))
        if 3 <= tamanho_input <= 11:
            tamanho = tamanho_input
        else:
            print("Tamanho inválido! Usando o tamanho padrão de 11x11.")
    except ValueError:
        print("Entrada inválida! Usando o tamanho padrão de 11x11.")
    
    jogo = JogoHex(tamanho)
    jogo.jogar()