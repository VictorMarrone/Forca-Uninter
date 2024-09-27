import jogo as j
import fileHandler as fH

def mostrar_menu():
    print('=' * 30)
    print(' ' * 7 + 'JOGO DA FORCA')
    print('=' * 30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR \n')
    print('=' * 30)

arquivo = 'score.txt'
if fH.existeArquivo(arquivo):
    print('Arquivo foi localizado no computador.')
else:
    print('Arquivo nao existe.')
    fH.criarArquivo(arquivo)

while True:
    mostrar_menu()
    opcao = int(input('Escolha a opcao: (1/2/3):'))

    match opcao:
        case 1: 
            print('iniciar jogo!')
            j.jogar()
            
        case 2:
            print('SCORE')
            dados = fH.listarArquivo('score.txt')
            if not dados:
                print('Score vazio.')
            else:
                i = 1
                for jogador in dados:
                    print(f'{i} -> {jogador[0]}, Pontuação: {jogador[1][:-1]}')
                    i += 1
            
        case 3:
            print('Saindo do jogo. Ate mais!')
            break
        case _:
            print('Opcao invalida!')