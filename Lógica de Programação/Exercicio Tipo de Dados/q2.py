altura = float(input("Digite a altura da sala em metros: "))
comprimento = float(input("Digite o comprimento da sala em metros: "))
largura = float(input("Digite a largura da sala em metros: "))

area_piso = largura * comprimento
volume_sala = altura * comprimento * largura
area_paredes = 2 * altura * largura + 2 * altura * comprimento

print(f"A área do piso da sala é: {area_piso:.2f} metros quadrados.")
print(f"O volume da sala é: {volume_sala:.2f} metros cúbicos.")
print(f"A área das paredes da sala é: {area_paredes:.2f} metros quadrados.")
