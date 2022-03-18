import datetime as dt

hora_inicial = int(input("Informe a hora do inicio do jogo: "))
minuto_inicial = int(input("Informe os minutos do inicio do jogo: "))
hora_final = int(input("Informe a hora do final do jogo: "))
minuto_final = int(input("Informe os minutos do final do jogo: "))

horainicio = dt.timedelta(hours=hora_inicial)
horafinal = dt.timedelta(hours=hora_final)
minutosinicio = dt.timedelta(minutes=minuto_inicial)
minutosfinal = dt.timedelta(minutes=minuto_final)


conta_hora = horafinal - horainicio
conta_final = minutosfinal - minutosinicio

print(f"O tempo de duração do jogo foi {conta_hora} horas and {conta_final} minutos.")