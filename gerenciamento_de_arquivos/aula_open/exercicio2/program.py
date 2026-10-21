# Crie um arquivo chamado mensagem.txt com um parágrafo de texto que você inventar. Depois, escreva um script que conte e exiba quantas letras existem nesse texto.

from pathlib import Path

mensagem = Path("gerenciamento_de_arquivos/aula_open/exercicio2/mensagem.txt")
mensagem.touch(exist_ok=True)

with open(mensagem, 'r+', encoding="utf-8") as msg:
    msg.write("Estou aprendendo bastante")
    msg.seek(0)
    conteudo = msg.read()
    print(f'A frase tem {len(conteudo)} letras.')