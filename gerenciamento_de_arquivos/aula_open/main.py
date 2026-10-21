
# Nesse primeiro exemplo, sempre que abrir um arquivo com open, sempre lembra de fechar ele com close
arq = open("gerenciamento_de_arquivos/aula_open/arq.txt")
conteudo = arq.read()

print(conteudo)
arq.close()

# ---------------------------------------------------------------

# Neste segundo exemplo, utilizamos o with para abrir um arquivo, pois, ao final da execção, o close já será utilizado automaticamente.
with open("gerenciamento_de_arquivos/aula_open/arq.txt") as arquivo:
    print(arquivo.read())
    print(arquivo.readlines()) # função readlines retorna uma lista com todas as linhas do arquivo

# ---------------------------------------------------------------

# No exemplo abaixo, o segundo argumento 'w', está permitindo que escrevamos no arquivo. Por padrão, todo arquivo entra no modo read apenas. Outra curiosidade do modo w, é que se o arquivo não existe, ele cria um arquivo com o texto informado.
with open("gerenciamento_de_arquivos/aula_open/arq.txt", 'w', encoding="utf-8") as arquivo:
    arquivo.write("Olá mundo!")

# O modo 'a', permite escrever textos adicionando ao texto existente, enquanto o w, sobrescreve o conteudo. Uma forma de quebrar a linha adicionando, é sempre colocar o \n no final do texto que irá adicionar.
with open("gerenciamento_de_arquivos/aula_open/arq.txt", 'a', encoding="utf-8") as arquivo:
    arquivo.write("testando")

# No exemplo abaixo, passamos como argumento o 'r+' para deixar o documento como read e write ao mesmo tempo. Depois de escrever, usamos a função .seek(0) para reiniciar o ponteiro do mouse na primeira posição do arquivo. Isso ocorre porque depois de escrever, o cursor do pyton fica na ultima posição e precisamos resetar ele.
with open("gerenciamento_de_arquivos/aula_open/arq.txt", 'r+', encoding="utf-8") as arquivo:
    arquivo.write("testando")
    arquivo.seek(0)
    print(arquivo.read())

# Um ponto importante, se voce utilizar o seek e depois escrever mais alguma coisa, o que está escrito antes será perdido. Então caso for escrever e depois escrever denovo, não utilize o seek. Somente se precisar ler a partir da primeira linha, sem escrever mais nada.
