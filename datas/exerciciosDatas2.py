from datetime import datetime, timedelta

# Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.

anoNovo = datetime(datetime.now().year, 12, 31) #.year: captura o ano atual, sem deixar 2026 fixo.

dias_restantes = (anoNovo.date() - datetime.now().date()).days #.date(): considera somente a data, ignorando horas, minutos e segundos.

print(f'Faltam {dias_restantes} dias para 31 de dezembro!')

# Peca ao usuario que digite uma data de um evento. Mostre se o evento ja aconteceu, se esta acontecendo hoje, ou quantos dias faltam.

dataEvento = datetime.strptime(input("Digite a data do evento no formato DD/MM/YYYY: "), "%d/%m/%Y").date() # Nunca esquecer que strptime recebe dois argumentos (o que quero converter, formato)
dataHoje = datetime.now().date() #.date(): considera somente a data, ignorando horas, minutos e segundos.

dias_restantes_evento = (dataEvento - dataHoje).days

if dataEvento == dataHoje: # Utilizando a funcao .date(), a necessidade de cercar dia, mes e ano fica inibida.
    print('O evento ocorre hoje!')
elif dataEvento > dataHoje:
    print(f'Faltam {dias_restantes_evento} dias para o evento!')
elif dataEvento < dataHoje:
    print('O evento ja ocorreu!')

# Peca ao usuario para informar a data de fabricacao de um produto. Considere que ele vence em 180 dias. Mostre: A data de validade, Se o produto ainda esta valido ou ja venceu, Quantos dias faltam ou ha quanto tempo passou do prazo.

dataFabricacao = datetime.strptime(input("Informe a data de fabricacao no formato DD/MM/YYYY: "), "%d/%m/%Y").date()
dataAtual = datetime.now().date()
vencimentoProd = dataFabricacao + timedelta(days=180)
diasRestantes = (vencimentoProd - dataAtual).days

print(f'Vencimento do produto: {vencimentoProd.strftime("%d/%m/%Y")}')

if diasRestantes == 0:
    print('O produto vence hoje!')
elif diasRestantes > 0:
    print(f"Produto dentro do prazo de validade!")
    print(f"Faltam {diasRestantes} dias para vencer.")
else:
    print("Produto vencido!")
    print(f"O produto venceu ha {abs(diasRestantes)} dias.")