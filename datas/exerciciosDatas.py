from datetime import datetime

# Mostre a hora atual no terminal, mas com a seguinte regra: Se a hora for antes das 12h, imprima: "Bom dia!", Se estiver entre 12h e 18h: "Boa tarde!", Depois disso: "Boa noite!"

horaAtual = datetime.now().hour

if horaAtual < 12 and horaAtual > 3:
    print('Bom dia!')
elif horaAtual >= 12 and horaAtual < 18:
    print('Boa tarde!')
else:
    print('Boa noite!')

print(f"Agora sao {horaAtual} horas.")

# Crie um programa que exiba quantos meses faltam para o ano acabar. Exemplo: Hoje eh o 4(quarto) mes do ano. Ainda faltam 8 meses para terminar o ano!

mesesAno = 12
mesAtual = datetime.now().month

mesesRestante = mesesAno - mesAtual

print(f'Hoje é o {mesAtual}º mês do ano. Ainda faltam {mesesRestante} meses para acabar o ano!')

# Crie uma funcao que receba como argumento um nome, e exiba uma assinatura desta forma: Assinatura gerada por [SEU NOME] em 24 de abril de 2025 as 15:02. A data e horario devem ser do momento atual da assinatura

def assinatura(nome):
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dataHora = datetime.now()

    nomeMes = meses[dataHora.month - 1]
    print(f'Assinatura gerada por {nome} em {dataHora.strftime("%d de")} {nomeMes} {dataHora.strftime("de %Y as %H:%M")}')

nome = input("Assine seu nome para concluir o contrato: ")

assinatura(nome)