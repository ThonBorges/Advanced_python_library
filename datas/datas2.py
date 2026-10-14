from datetime import datetime, timedelta

# hoje = datetime.now()
# um_dia = timedelta(days=1)

# amanha = hoje + um_dia
# ontem = hoje - um_dia

# print(amanha)
# print(ontem)

# -------------------------------------------------------------------

# prazo = datetime(2025, 11, 25)
# hoje = datetime.now()

# if hoje > prazo:
#     print("Prazo Vencido!")
# else:
#     print("Ainda esta no prazo!")

# -------------------------------------------------------------------

# agora = datetime.now()
# futuro = datetime(2027, 9, 23)
# dias_restantes = futuro - agora

# print(dias_restantes)
# print(dias_restantes.days)

# -------------------------------------------------------------------

aniversario = datetime(2026, 10, 14)
hoje = datetime.now()
dias_restantes = aniversario - hoje

if aniversario.day == hoje.day and aniversario.month == hoje.month:
    print("O aniversario eh hoje!")
elif aniversario > hoje:
    print(f'Faltam {dias_restantes.days} dias para o aniversario!')
elif aniversario < hoje:
    print("Aniversario ja ocorreu.")
