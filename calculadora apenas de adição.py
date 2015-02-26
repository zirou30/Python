calc = 0
while True:
    x = float(input("Qual soma deseja efetuar(para sair aperte 0)"))
    if x == 0:
        break
    calc = calc + x
print("Soma: %.2f" %calc)
