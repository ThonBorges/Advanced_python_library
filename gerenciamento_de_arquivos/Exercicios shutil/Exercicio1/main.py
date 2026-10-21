# Crie um script que:
# Crie uma pasta imagens.
# Coloque 2 arquivos fictícios .png dentro dela
# Copie todos os arquivos .png da pasta imagens para uma nova pasta chamada backup.


import shutil
from pathlib import Path

image01 = Path("gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/01.png")
image02 = Path("gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/02.png")
image01.touch(exist_ok=True)
image02.touch(exist_ok=True)

imagens = Path("gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/imagens")
if not imagens.exists():
    imagens.mkdir()

shutil.move("gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/01.png", "gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/imagens")
shutil.move("gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/02.png", "gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/imagens")

shutil.copytree("gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/imagens", "gerenciamento_de_arquivos/Exercicios shutil/Exercicio1/imagens_backup", dirs_exist_ok=True)

