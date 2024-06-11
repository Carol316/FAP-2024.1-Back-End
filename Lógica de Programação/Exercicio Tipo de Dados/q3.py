hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

total_segundos = hora * 3600 + minutos * 60 + segundos

print(f"Total de segundos desde a meia-noite: {total_segundos} segundos.")
