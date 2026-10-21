# Crie um script que:
# Verifica se existe um arquivo chamado relatorio.txt.
# Move esse arquivo para uma pasta chamada relatorios_antigos.
# Durante a movimentação, renomeie o arquivo para relatorio_backup.txt.

import shutil
from pathlib import Path

relatorio = Path("gerenciamento_de_arquivos/Exercicios shutil/Exercicio2/relatorio.txt")
relatorio.touch(exist_ok=True)

relatorios_antigos = Path("gerenciamento_de_arquivos/Exercicios shutil/Exercicio2/relatorios_antigos")
if not relatorios_antigos.exists():
    relatorios_antigos.mkdir()
    
shutil.move("gerenciamento_de_arquivos/Exercicios shutil/Exercicio2/relatorio.txt", "gerenciamento_de_arquivos/Exercicios shutil/Exercicio2/relatorios_antigos/relatorio_backup.txt")