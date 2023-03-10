from netflix import *
from time import sleep

netflix = Netflix()

while True:
    print('-'*30)
    print('Sistema Pobreflix'.center(30, ' '))
    print('-'*30)
    print('Informe o que deseja fazer:\n'
          '1 - Cadastro\n'
          '2 - Assistir video\n'
          '3 - Sair')
    try:
        opcao = int(input('> '))
        if opcao > 3 or opcao < 1:
            print('Opção Inválida.')
            sleep(3)
        if opcao == 1:
            print('O que deseja cadastrar?\n'
                  '1 - Plano de assinatura\n'
                  '2 - Usuário\n'
                  '3 - Video')
            cadastrar = int(input('> '))
            if cadastrar == 1:
                netflix.cadastrarPlano()
            elif cadastrar == 2:
                netflix.cadastrarUsuario()
            elif cadastrar == 3:
                netflix.cadastrarVideo()
        elif opcao == 2:
            netflix.assistirVideo()
        elif opcao == 3:
            print('Saindo...')
            sleep(2)
            break
    except ValueError:
        print('Informe um valor válido...')
        sleep(3)
    except NameError:
        print('Algo deu errado, tente denovo...')
        sleep(3)
