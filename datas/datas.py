from datetime import datetime

# agora = datetime.now()

# print(agora)
# print(agora.day)
# print(agora.month)
# print(agora.year)
# print(agora.hour)
# print(agora.minute)
# print(agora.second)
# print(agora.microsecond)


# aniversario = datetime(2000, 5, 20)
# print(aniversario)

agora = datetime.now()
print(agora.strftime("Hoje eh dia %d do mes %m do ano %Y")) # a funcao strftime tranforma todo o argumento date time em string e retorna depois das "%" a letra correspondente a informacao desejada. Ex.: %d = dia da variavel 'agora'.
print(agora.strftime("Agora sao %H horas e %M minutos"))
print(agora.strftime("%d/%m/%Y"))

data_str = "20/04/2026"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y") # A funcao strptime faz o inverso, convertendo uma string em datetime.
print(data_convertida)