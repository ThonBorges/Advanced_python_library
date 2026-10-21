# Crie um arquivo chamado relatorio.txt que contenha a frase "Estou aprendendo Python!
# Inclua no final do arquivo a data e hora de criação do arquivo de forma automática

from pathlib import Path
from datetime import datetime

agora = datetime.now()

relatorio = Path("gerenciamento_de_arquivos/aula_open/exercicio1/relatorio.txt")
relatorio.touch(exist_ok=True)

with open(relatorio, 'r+', encoding="utf-8") as relatorio:
    relatorio.write(agora.strftime("Arquivo criado em %d/%m/%Y - %H:%M"))
    relatorio.seek(0)
    print(relatorio.read())