# Baixe o arquivo logs.txt anexado, e escreva um programa que:
# Leia todas as linhas do arquivo
# Peça ao usuário uma palavra-chave (como ERROR, INFO, WARNING, etc...)
# Mostre apenas as linhas que contenham essa palavra-chave.

with open("gerenciamento_de_arquivos/aula_open/exercicio3/acesso.log", encoding="utf-8") as log:
    busca = input('Qual palavra-chave deseja buscar? (ERROR/DEBUG/WARNING/INFO): ')
    for linha in log.readlines():
        if busca.upper() in linha:
            print(linha)
    