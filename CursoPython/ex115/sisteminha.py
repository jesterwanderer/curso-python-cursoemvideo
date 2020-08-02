from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(["Ver Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Sair do Sistema"])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        nome = input("Informe um nome: ")
        idade = leiaInt("Informe a idade: ")
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cab("BYE ;)")
        break
    else:
        cab("ERRO OPÇÃO INVÁLIDA")
    sleep(2)
