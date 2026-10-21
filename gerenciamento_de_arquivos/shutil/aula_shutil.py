import shutil
from pathlib import Path

# shutil.copy2("gerenciamento_de_arquivos/shutil/arq.txt", "gerenciamento_de_arquivos/shutil/backup/arq_backup.txt")
# # A diferença entre copy e copy2, é que o copy2 copia até os metadados do arquivo original.

# -----------------------------------------------------------------------------------------------------------------------

# shutil.copytree("gerenciamento_de_arquivos/shutil/meus_arquivos", "gerenciamento_de_arquivos/shutil/meus_arquivos_backup", dirs_exist_ok=True)
# # A função copytree, vai pegar tudo que tem dentro da pasta e copiar em outro local. o parâmetro dirs_exist_ok, verifica se o local já existe e não gera erro quebrando o programa.

# -----------------------------------------------------------------------------------------------------------------------

# arquivo_teste = Path("gerenciamento_de_arquivos/arq_teste.txt")
# shutil.move(arquivo_teste, "gerenciamento_de_arquivos/shutil/meus_arquivos")
# # O .move serve tanto para mover, quanto para renomear um arquivo, igual aos terminais linux

# -----------------------------------------------------------------------------------------------------------------------

# shutil.rmtree("gerenciamento_de_arquivos/shutil/meus_arquivos_backup")
# # A função .rmtree, serve para deletar um diretório ou arquivo.

# -----------------------------------------------------------------------------------------------------------------------

# shutil.make_archive("gerenciamento_de_arquivos/shutil/meus_arquivos", "zip", "gerenciamento_de_arquivos/shutil/meus_arquivos")
# # A função .make_achive zipa um diretório ou pasta sendo (arquivo que será zipado, formato, novo nome do arquivo/pasta)

# -----------------------------------------------------------------------------------------------------------------------

# shutil.unpack_archive("gerenciamento_de_arquivos/shutil/meus_arquivos.zip")
# # a função .unpack_archive descompacta o conteudo do arquivo zip e mantem uma copia do arquivo zipado original
# Bonus: Voce consegue indicar aonde deseja que seja descompactado o conteudo, passando como segundo argumento, o local de destino.

# --------------------------------------CASO DE USO EXEMPLO -----------------------------------------------------

arquivos = Path("gerenciamento_de_arquivos/shutil/arquivos")
arquivos_backup = Path("gerenciamento_de_arquivos/shutil/arquivos_backup")

if not arquivos_backup.exists():
    arquivos_backup.mkdir()

shutil.copytree("gerenciamento_de_arquivos/shutil/arquivos", "gerenciamento_de_arquivos/shutil/arquivos_backup")
