import oracledb
import getpass

def cadastrar_professor():
    # nome, pf, senha
    try:
        print('\n=== CADASTRO ===')
        nome = input('Informe o seu nome: ')
        pf = input('Informe o seu PF (Cadastro de Professor)')
        senha = getpass.getpass('Digite uma senha (guarde-a)')
