# Existem dois tipos de paths(caminhos), absoluto e relativo. O relativo se diz respeito ao arquivo que esta na pasta da aplicação e é chamado somente com seu nome. O absoluto é chamado a partir do primeiro diretório do computador, assim como em um terminal linux.

# O "r" dentro do variavel caminho_absoluto, ignora caracteres especiais como o contra-barra e não da problema para buscar o caminho. Sempre que relacionar path a caminho absoluto, colocar o r antes.

from pathlib import Path

caminho = Path("arquivo.txt")
caminho_absoluto = Path(r"C:\Users\Celthon Borges\Documents\doc de teste")
caminho2 = caminho.absolute() # pega todo o caminho do arquivo.txt, tranformando ele em absoluto.

print(caminho)
print(caminho_absoluto)
print(caminho2)

# --------------------------------------------------------------------------------------------------------

caminho = Path("arquivo.txt")
if caminho.exists(): # verifica se o arquivo na variável caminho existe.
    print("Existe!")
else:
    print("Não existe!")

# --------------------------------------------------------------------------------------------------------

caminho = Path("arquivo.txt")

if caminho.is_file(): # verifica se caminho recebe um arquivo
    print ("É arquivo")
elif caminho.is_dir(): # verifica se caminho recebe uma pasta/diretorio
    print("É uma pasta")

# --------------------------------------------------------------------------------------------------------

nova_pasta = Path("NovaPasta") # Inicio uma variável com o nome da nova pasta que será criada.
nova_pasta.mkdir(exist_ok=True) # .mkdir irá criar a nova pasta informada na variavel e o parametro exist_ok=True, checa se a pasta existe ou não, e se caso ela ja existir, não retorna erro na aplicação.

# --------------------------------------------------------------------------------------------------------

nova_pasta = Path("NovaPasta/outraPasta/terceiraPasta") # declara uma variável que terá uma pasta dentro da outra
nova_pasta.mkdir(exist_ok=True, parents=True) # o parametro parents=True, condiciona essa criação ao sistema

# --------------------------------------------------------------------------------------------------------

arquivo = Path("arquivo.txt")
novapasta = Path("NovaPasta")

arquivo.unlink() # variavel.unlink() é utilizado para deletar documentos do tipo arquivo/file
novapasta.rmdir() # variavel.rmdir() é utilizado para deletar documentos do tipo pasta/diretorio

# --------------------------------------------------------------------------------------------------------

doc_teste = Path("gerenciamento_de_arquivos/arquivo.txt")
doc_teste.write_text("input externo") # o comando write_text possibilita escrever no arquivo especificado. Obs.: Se o arquivo não estiver vazio, esse comando irá sobrescrever o conteúdo com o texto enviado como parãmetro.
texto_doc = doc_teste.read_text() # comando read_text() lê o conteudo do arquivo
print(texto_doc)

# --------------------------------------------------------------------------------------------------------

pasta = Path() # o Path() vazio vai capturar tudo do diretório atual em que estamos
for arquivo in pasta.iterdir(): # o comando .iterdir() possibilita listar o conteudo da pasta através do loop for.
    print(arquivo)

# --------------------------------------------------------------------------------------------------------

pasta = Path()
for arquivo in pasta.glob(".txt"): # assim como o comando grep, o glob() serve para filtrarmos arquivos dentro de um diretorio através do padrão passado como parâmetro.
    print(arquivo)

# --------------------------------------------------------------------------------------------------------

caminho = Path("gerenciamento_de_arquivos/arquivo.txt")
print(caminho) # retorna o caminho até o arquivo
print(caminho.name) # retorna o nome do arquivo e sua extensão
print(caminho.stem) # retorna somente o nome do arquivo
print(caminho.suffix) # retorna somente a extensão do arquivo

# --------------------------------------------------------------------------------------------------------

arquivo = Path("meu_arquivo.txt")
arquivo.touch() # o comando .touch() possibilita criar um novo arquivo vazio no diretório atual