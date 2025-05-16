import oracledb
from professor import cadastrar_professor

def menu_inicial():
    usuario = None
    while usuario is None:
        try:
            print(f'\nSeja bem vindo!')
            print('1. Cadastrar')
            print('2. Login')
            print('3. Sair')

            opcao = input('Escolha uma opção para prosseguir: ').strip().lower()

            if opcao == '1':
                cadastrar_professor()
            elif opcao == '2':
                pass
            elif opcao == '3':
                print('Saindo...')
                exit()
            else:
                print('Opção inválida.')

        except Exception as e:
            print('Ocorreu um erro inesperado. {e}')

    return usuario