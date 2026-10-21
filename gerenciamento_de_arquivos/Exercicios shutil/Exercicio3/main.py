# Considerando o arquivo zip que deixei na sessão de recursos, crie um script que:
# Crie uma pasta chamada extraido/.
# Extraia o conteúdo do .zip dentro da pasta criada.
# Ao final, liste todos os arquivos extraídos.

import shutil
from pathlib import Path

extraido = Path("gerenciamento_de_arquivos/Exercicios shutil/Exercicio3/extraido")
if not extraido.exists():
    extraido.mkdir()

shutil.unpack_archive("gerenciamento_de_arquivos/Exercicios shutil/Exercicio3/arquivos_secretos.zip", "gerenciamento_de_arquivos/Exercicios shutil/Exercicio3/extraido")

for arquivo in extraido.iterdir():
    print(arquivo)