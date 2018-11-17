nc = int(input('Insira o número de computadores:'))
comp = []
con = []
compv = []
conv = []
comp.append(1)
compv.append(0)
for i in range(0,(nc - 2)):
    comp.append(int(input("Insira o número do computador:")))
    compv.append(int(input("Insira o valor do computador: ")))
comp.append(50)
compv.append(0)
nc = int(input(print('Insira o número de conexões: \nSendo o computador do chef o de número 1 e o servidor o de número 50')))    
for i in range(0,nc):
    con.append(input("Insira a conexão: (ComputadorX ComputadorY)"))
    conv.append(int(input("Insira o valor da conexão: ")))
print(comp)
print('\n')
print(compv)
print(con)
print('\n')
print(conv)

