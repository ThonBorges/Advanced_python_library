from pathlib import Path

# Crie a seguinte estrutura: 
# ├──dados/
# │  ├── entrada/
# │  └── saida/
# ├──relatorios/
# Crie todas as pastas em uma única execução do seu código.

dados_entrada_dir = Path("gerenciamento_de_arquivos/dados/entrada")
dados_saida_dir = Path("gerenciamento_de_arquivos/dados/saida")
relatorios_dir = Path("gerenciamento_de_arquivos/relatorios")

dados_entrada_dir.mkdir(exist_ok=True, parents=True)
dados_saida_dir.mkdir(exist_ok=True, parents=True)
relatorios_dir.mkdir(exist_ok=True, parents=True)


# Dentro da pasta entrada/, crie 3 arquivos vazios: 
# dados1.txt
# dados2.txt
# dados3.txt

entrada_file1 = Path("gerenciamento_de_arquivos/dados/entrada/dados1.txt")
entrada_file2 = Path("gerenciamento_de_arquivos/dados/entrada/dados2.txt")
entrada_file3 = Path("gerenciamento_de_arquivos/dados/entrada/dados3.txt")
entrada_file1.touch(exist_ok=True)
entrada_file2.touch(exist_ok=True)
entrada_file3.touch(exist_ok=True)


# Liste todos os arquivos .txt dentro de entrada/. Imprima apenas o nome do arquivo (sem o caminho completo).

for arquivo in dados_entrada_dir.iterdir():
    print(arquivo.stem)
