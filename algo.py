nc = int(input('Insira o número de computadores:'))
comp = []
con = []
compv = []
conv = []
comp.append(1)
compv.append(0)
for i in range(0, (nc - 2)):
    comp.append(int(input("Insira o número do computador:")))
    compv.append(int(input("Insira o valor do computador: ")))
comp.append(nc)
compv.append(0)
nc = int(input(print('Insira o número de conexões: \nSendo o computador do chef o de número 1 e o servidor o �ltimo n�mero')))    
for i in range(0, nc):
    con.append(input("Insira a conexão: (ComputadorX ComputadorY)"))
    conv.append(int(input("Insira o valor da conexão: ")))
''' 
Somando o valor das conex�es em �ndices diferentes
'''
dist = []
x = 0
for i in range(1, nc):
    if comp[i - 1] + ' ' + comp[i] in con:
        for j in range(1, nc):
            if comp[i] + ' ' + comp[j] in con:
                x += conv[j]
        dist.append(x)
        
print(comp)
print('\n')
print(compv)
print(con)
print('\n')
print(conv)

